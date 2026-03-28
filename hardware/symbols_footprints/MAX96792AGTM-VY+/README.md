# MAX96792AGTM/VY+ KiCad Library and 3D Model

## Overview

- **Component:** MAX96792AGTM/VY+ (Analog Devices)
- **Package:** 48-TQFN, 7x7mm, 0.5mm pitch, Exposed Pad (EP)
- **Use:** Automotive GMSL3/2 to CSI-2 Deserializer

This folder contains:
- `MAX96792AGTM_VY+.kicad_sym` – Schematic symbol (KiCad v9+, no top/bottom pins, functional/logic grouping, with full properties)
- `MAX96792AGTM_VY+.kicad_mod` – Footprint (IPC-7351-compliant pads, 0.25mm courtyard, pin 1 marker, exposed pad, 3D reference)
- `MAX96792AGTM_VY+_3d.py` – Parametric FreeCAD Python script: exports STEP for 3D model integration with headless (CLI) execution.
- `README.md` – Usage, integration, validation instructions

---

## Integration Steps

### 1. Symbol and Footprint in KiCad

- Copy `.kicad_sym` to your KiCad user library folder or project library.
- Copy `.kicad_mod` to a footprint library folder and add as a library in KiCad as needed.
- Link the symbol's "Footprint" property to `MAX96792AGTM_VY+` from this footprint library.
- All pins are logically grouped. Power pins are at corners following symbol rules (see rules_index.md).

### 2. 3D Model Export & Import

- To generate the STEP model (`.step`), run:
  ```
  freecad --console --run MAX96792AGTM_VY+_3d.py
  ```
  _Requires FreeCAD Python installation with Part WB enabled. Script runs headless._
- The generated `MAX96792AGTM_VY+.step` can be placed in your KiCad 3D model directory.
- The footprint file references this `.step` model. Adjust the path as needed for your project.

### 3. ERC/DRC Validation

- Perform ERC and DRC in KiCad after symbol/footprint assignment:
  - Symbol pin types: strictly per electrical function in datasheet
  - No pins on symbol top/bottom. Pinorder is logical, not physical.
  - Footprint: All pads IPC-7351 size, standard TQFN48 layout, exposed pad net should be set to GND.
  - Courtyard is exactly 0.25mm from max body on all sides. Test using DRC and overlay on datasheet mechanical drawing.

- Ensure schematic GND symbol is connected to "EP" (Exposed Pad) for correct net assignment.

### 4. Dimensional Accuracy

- Footprint and 3D model verified with nominal dimensions: **Body: 7.00 x 7.00 mm**, **Pin pitch: 0.50 mm**, **Pin width: 0.30 mm**, **EP: 5.40 x 5.40 mm**.
- All pads and courtyard meet IPC-7351B requirements. For tightest designs confirm maximum tolerances from the manufacturer and/or check datasheet for mount tolerances.
- Visual/manual 3D check: after importing the STEP model, overlay with PCB in KiCad, confirm height clearance.

### 5. Rule Application

All symbol, footprint, and 3D generation was performed according to `rules_index.md`, with reference to:
- **Symbol:** Shape, pin grouping, metadata, and graphical style per symbol_rules.md.
- **Footprint:** SMD pad size/spacing/courtyard 0.25mm, pin 1 marker, and 3D model reference per footprint_rules.md/IPC-7351.
- **3D:** Fully parametric, with all dimensional/height tolerances per 3d_model_rules.md.

---

## Examples

**Schematic Symbol Example**
![Symbol](../../images/generated-symbol.png)

**Footprint Example**
![Footprint](../../images/generated-footprint.png)

**3D Model Preview**
![3D Model](../../images/generated-3d-model.gif)

## References

- [Datasheet - MAX96792A](https://www.analog.com/media/en/technical-documentation/data-sheets/max96792a.pdf)
- [Analog Devices MAX96792A Product Page](https://www.analog.com/en/products/max96792a.html)

---

_If you use this library, verify all PCB designs using ERC/DRC and cross-check against the latest datasheet before committing to manufacture._
