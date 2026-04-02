#!/usr/bin/env python3
import sys
import os
import json
import re
import argparse

import pdfplumber
import ollama


PIN_SECTION_RE = re.compile(
    r'(pinout|pinouts|pin map|pin assignment|package pinout|pin list|ball map|pin diagram)',
    re.I
)
ALT_SECTION_RE = re.compile(
    r'(alternate pin functions|alternate functions|pin mux|mux table|functional pin)',
    re.I
)
PACKAGE_HINT_RE = re.compile(
    r'(tqfp|qfn|qfp|wlcsp|bga|ssop|soic|dip|lqfp|pqfp|sop|csp|tssop)',
    re.I
)
PORT_PIN_RE = re.compile(
    r'^(P\d+\.\d{1,2}|P\d+\.\d{2}|VDDA|VSSA|VDDD|VSSD|VCCD|VDD[A-Z0-9]*|VSS[A-Z0-9]*|XRES|RESET|NC)\b',
    re.I
)
PACKAGE_PIN_RE = re.compile(r'^\d+$')


def debug(msg, enabled):
    if enabled:
        print(f"[DEBUG] {msg}", file=sys.stderr)


def normalize(s):
    if s is None:
        return ''
    s = str(s).replace('\xa0', ' ').replace('–', '-').replace('—', '-')
    return re.sub(r'\s+', ' ', s).strip()


def escape_md(s):
    return normalize(s).replace('|', '\\|')


def canonical_port_pin(s):
    s = normalize(s).upper().replace(' ', '')
    m = re.match(r'^(P\d+\.\d{1,2})', s)
    if m:
        return m.group(1)
    return s


def score_page(text, package=None):
    t = text or ''
    score = 0
    if PIN_SECTION_RE.search(t):
        score += 4
    if package and package.lower() in t.lower():
        score += 3
    if PACKAGE_HINT_RE.search(t):
        score += 1
    if ALT_SECTION_RE.search(t):
        score -= 1
    return score


def llm_json(text, model, prompt):
    try:
        resp = ollama.generate(
            model=model,
            prompt=prompt + '\nTEXT:\n' + text,
            options={'temperature': 0}
        )
        content = (resp.get('response') or '').strip()
        s = content.find('[')
        e = content.rfind(']')
        if s != -1 and e != -1:
            return json.loads(content[s:e + 1])
    except Exception as e:
        print(f'[LLM ERROR] {e}', file=sys.stderr)
    return []


def llm_extract_port_pins(text, model, part=None, package=None):
    prompt = (
        'Extract only alternate-function pin rows for symbol metadata. JSON array only. '
        'Each item: pin, name, description, type, aliases. '
        f'Part: {part or "UNKNOWN"}. Package: {package or "UNKNOWN"}. '
        'Do not invent pins. Use port pins like P0.0, P1.0, VDDA, XRES.'
    )
    return llm_json(text[:12000], model, prompt)


def llm_extract_package_pinout(text, model, part=None, package=None):
    prompt = (
        'Extract only the selected package pinout rows from the table. JSON array only. '
        'Each item: package_pin, signal, note. '
        f'Part: {part or "UNKNOWN"}. Package: {package or "UNKNOWN"}. '
        'Use numeric package pin numbers from the selected package column only. '
        'Do not return port-function rows.'
    )
    return llm_json(text[:12000], model, prompt)


def dedupe(rows, key_fields):
    seen = set()
    out = []
    for r in rows:
        key = tuple(r.get(k, '') for k in key_fields)
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def escape_cell(v):
    return escape_md(v)


def split_raw_lines(text):
    return [normalize(line) for line in (text or '').splitlines() if normalize(line)]


def render_md_block(title, text):
    lines = [title, '', '```text']
    lines.extend(split_raw_lines(text))
    lines.append('```')
    lines.append('')
    return lines


def render_port_functions(rows):
    lines = ['### Port Functions', '']
    lines.append('| pin | name | description |')
    lines.append('|---|---|---|')
    for r in rows:
        lines.append(
            f"| {escape_cell(r.get('pin', ''))} | "
            f"{escape_cell(r.get('name', ''))} | "
            f"{escape_cell(r.get('description', ''))} |"
        )
    lines.append('')
    return lines


def extract_port_functions(page, text, model, part=None, package=None):
    rows = []
    for t in page.extract_tables() or []:
        if not t or len(t) < 2:
            continue
        joined = ' '.join(' '.join(normalize(c) for c in r) for r in t[:5])
        if ALT_SECTION_RE.search(joined) or re.search(r'P\d+\.\d', joined):
            for r in t[1:]:
                cells = [normalize(c) for c in r]
                if not cells or not cells[0]:
                    continue
                pin = canonical_port_pin(cells[0])
                if not PORT_PIN_RE.match(pin):
                    continue
                rows.append({
                    'pin': pin,
                    'name': cells[1] if len(cells) > 1 else '',
                    'description': ' | '.join(cells[2:]) if len(cells) > 2 else '',
                    'type': 'multiplexed',
                    'aliases': [],
                    'source': 'table'
                })

    if rows:
        return rows

    if ALT_SECTION_RE.search(text) or re.search(r'\bP\d+\.\d{1,2}\b', text):
        llm_rows = llm_extract_port_pins(text, model, part, package)
        out = []
        for item in llm_rows:
            pin = canonical_port_pin(item.get('pin', ''))
            if PORT_PIN_RE.match(pin):
                out.append({
                    'pin': pin,
                    'name': normalize(item.get('name', '')),
                    'description': normalize(item.get('description', '')),
                    'type': normalize(item.get('type', 'multiplexed')) or 'multiplexed',
                    'aliases': item.get('aliases', []) or [],
                    'source': 'llm'
                })
        return out

    return []


def extract_tables_as_text(page):
    out = []
    tables = page.extract_tables() or []
    for t in tables:
        if not t or len(t) < 2:
            continue
        rows = []
        for r in t:
            cells = [normalize(c) for c in r]
            if any(cells):
                rows.append(cells)
        if rows:
            out.append(rows)
    return out


def render_table_as_markdown(rows):
    if not rows:
        return []
    max_cols = max(len(r) for r in rows)
    normalized = [r + [''] * (max_cols - len(r)) for r in rows]
    lines = []
    headers = normalized[0]
    lines.append('| ' + ' | '.join(escape_cell(h) for h in headers) + ' |')
    lines.append('|' + '|'.join(['---'] * max_cols) + '|')
    for r in normalized[1:]:
        lines.append('| ' + ' | '.join(escape_cell(c) for c in r) + ' |')
    return lines


def package_key(s):
    return normalize(s).lower().replace(' ', '').replace('-', '')


def package_matches_label(label, package):
    if not package:
        return False
    l = package_key(label)
    p = package_key(package)
    return bool(l and p and (l == p or p in l or l in p))


def extract_package_groups_from_header(header0):
    groups = []
    for i, cell in enumerate(header0):
        c = normalize(cell)
        if c and any(k in c.lower() for k in ['qfn', 'tqfp', 'qfp', 'ssop', 'tssop', 'csp', 'bga', 'wlcsp']):
            groups.append((i, c))
        elif re.search(r'\b\d+\s*-\s*pin\b|\b\d+\s*-\s*ball\b', c, re.I):
            groups.append((i, c))
    return groups


def parse_package_matrix_table(table, selected_package=None):
    if not table or len(table) < 3:
        return []

    header0 = [normalize(c) for c in table[0]]

    package_labels = []
    for _, label in extract_package_groups_from_header(header0):
        package_labels.append(label)

    if not package_labels:
        package_labels = [normalize(c) for c in header0 if normalize(c)]

    chosen = None
    if selected_package:
        for idx, label in enumerate(package_labels):
            if package_matches_label(label, selected_package):
                chosen = idx
                break

    out = []

    for row in table[2:]:
        cells = [normalize(c) for c in row]
        if not any(cells):
            continue

        max_groups = min(len(cells) // 2, len(package_labels) if package_labels else len(cells) // 2)
        if max_groups <= 0:
            continue

        for g in range(max_groups):
            if selected_package and chosen is not None and g != chosen:
                continue

            pin_idx = g * 2
            name_idx = pin_idx + 1
            if pin_idx >= len(cells):
                continue

            pin_cell = cells[pin_idx]
            name_cell = cells[name_idx] if name_idx < len(cells) else ''

            if PACKAGE_PIN_RE.match(pin_cell):
                out.append({
                    'package_pin': int(pin_cell),
                    'signal': name_cell,
                    'note': '',
                    'package': selected_package or (package_labels[g] if g < len(package_labels) else ''),
                    'source': 'table'
                })

    return dedupe(out, ['package_pin', 'signal', 'package'])


def extract_package_pinout_from_page(page, text, package=None, model='llama3.2:latest', part=None):
    tables = page.extract_tables() or []

    best = None
    best_score = -1

    for t in tables:
        if not t or len(t) < 3:
            continue
        header0 = ' '.join(normalize(c) for c in t[0])
        header1 = ' '.join(normalize(c) for c in t[1])
        score = 0
        if 'packages' in header0.lower():
            score += 20
        if package and package.lower() in (header0 + ' ' + header1).lower():
            score += 30
        if PIN_SECTION_RE.search(header0) or PIN_SECTION_RE.search(header1):
            score += 5
        if PACKAGE_HINT_RE.search(header0) or PACKAGE_HINT_RE.search(header1):
            score += 5
        if score > best_score:
            best_score = score
            best = t

    if best is not None:
        rows = parse_package_matrix_table(best, selected_package=package)
        if rows:
            return rows

    for t in tables:
        if not t or len(t) < 2:
            continue
        header = ' '.join(normalize(c) for c in t[0]).lower()
        if not (PIN_SECTION_RE.search(header) or PACKAGE_HINT_RE.search(header) or (package and package.lower() in header)):
            continue
        rows = []
        for r in t[1:]:
            cells = [normalize(c) for c in r]
            if not cells:
                continue
            if PACKAGE_PIN_RE.match(cells[0]):
                rows.append({
                    'package_pin': int(cells[0]),
                    'signal': cells[1] if len(cells) > 1 else '',
                    'note': ' | '.join(cells[2:]) if len(cells) > 2 else '',
                    'package': package or '',
                    'source': 'table'
                })
        if rows:
            return dedupe(rows, ['package_pin', 'signal', 'package'])

    if score_page(text, package) >= 3:
        llm_rows = llm_extract_package_pinout(text, model, part, package)
        out = []
        for item in llm_rows:
            p = normalize(item.get('package_pin', ''))
            if PACKAGE_PIN_RE.match(p):
                out.append({
                    'package_pin': int(p),
                    'signal': normalize(item.get('signal', '')),
                    'note': normalize(item.get('note', '')),
                    'package': package or '',
                    'source': 'llm'
                })
        return dedupe(out, ['package_pin', 'signal', 'package'])

    return []


def extract(pdf_path, part=None, package=None, model='llama3.2:latest', verbose=False):
    result = {
        'file': os.path.basename(pdf_path),
        'part_number': part,
        'package': package,
        'package_pinout': [],
        'port_functions': []
    }

    md = [
        '# Extracted Datasheet',
        '',
        f'Part: {part or "UNKNOWN"}',
        f'Package: {package or "ANY"}',
        ''
    ]

    pkg_rows = []
    port_rows = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            debug(f"Processing page {i}", verbose)
            text = page.extract_text() or ''
            sc = score_page(text, package)

            should_include = sc >= 2 or bool(
                re.search(r'P\d+\.\d|\b\d+\s+(P\d+\.\d|VDD|VSS|VDDA|VSSA|VDDD|VSSD|VCCD)', text)
            )
            if not should_include:
                continue

            md.append(f'## Page {i}')
            md.append('')
            md.extend(render_md_block('### Raw Page Text', text))

            tables = extract_tables_as_text(page)
            if tables:
                md.append('### Extracted Tables')
                md.append('')
                for ti, table in enumerate(tables, start=1):
                    md.append(f'#### Table {ti}')
                    md.append('')
                    md.extend(render_table_as_markdown(table))
                    md.append('')

            p = extract_package_pinout_from_page(page, text, package=package, model=model, part=part)
            if p:
                for r in p:
                    r['page'] = i
                pkg_rows.extend(p)

            f = extract_port_functions(page, text, model, part, package)
            if f:
                for r in f:
                    r['page'] = i
                port_rows.extend(f)
                md.extend(render_port_functions(f[:200]))

    result['package_pinout'] = dedupe(pkg_rows, ['package_pin', 'signal', 'package'])
    result['port_functions'] = dedupe(port_rows, ['pin', 'name', 'description'])
    return result, '\n'.join(md)


def extract_full_markdown(pdf_path):
    md = [
        '# Full PDF Extract',
        '',
        f'Source file: {os.path.basename(pdf_path)}',
        ''
    ]

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ''
            md.append(f'## Page {i}')
            md.append('')
            md.extend(render_md_block('### Raw Page Text', text))

            tables = extract_tables_as_text(page)
            if tables:
                md.append('### Extracted Tables')
                md.append('')
                for ti, table in enumerate(tables, start=1):
                    md.append(f'#### Table {ti}')
                    md.append('')
                    md.extend(render_table_as_markdown(table))
                    md.append('')

    return '\n'.join(md)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input_pdf')
    ap.add_argument('--out', default=None)
    ap.add_argument('--part', default=None)
    ap.add_argument('--package', default=None, help='Package name like SSOP-28, TQFP-48, TSSOP-20')
    ap.add_argument('--model', default='llama3.2:latest')
    ap.add_argument('--verbose', default='no', choices=['yes', 'no'])
    args = ap.parse_args()

    verbose = args.verbose == 'yes'

    if not os.path.exists(args.input_pdf):
        print('File not found')
        sys.exit(1)

    prefix = args.out or os.path.splitext(args.input_pdf)[0]
    data, md = extract(args.input_pdf, part=args.part, package=args.package, model=args.model, verbose=verbose)
    full_md = extract_full_markdown(args.input_pdf)

    with open(prefix + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(prefix + '.md', 'w', encoding='utf-8') as f:
        f.write(md)

    with open(prefix + '-full.md', 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f'✅ JSON: {prefix}.json')
    print(f'✅ Markdown: {prefix}.md')
    print(f'✅ Full Markdown: {prefix}-full.md')


if __name__ == '__main__':
    main()