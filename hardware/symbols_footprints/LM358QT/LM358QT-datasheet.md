LM158, LM258, LM358, LM158A, LM258A, LM358A

Low-power dual operational amplifiers

Datasheet - production data

Related products
- See LM158W for enhanced ESD ratings
- See LM2904 and LM2904W for automotive grade versions

## Description
These circuits consist of two independent, high-gain, internally frequency-compensated op amps, specifically designed to operate from a single power supply over a wide range of voltages. The low-power supply drain is independent of the magnitude of the power supply voltage.

Application areas include transducer amplifiers, DC gain blocks and all the conventional op amp circuits, which can now be more easily implemented in single power supply systems. For example, these circuits can be directly supplied with the standard 5 V, which is used in logic systems and will easily provide the required interface electronics with no additional power supply.

In linear mode, the input common-mode voltage range includes ground and the output voltage can also swing to ground, even though operated from only a single power supply voltage.

## Features
- Frequency compensation implemented internally
- Large DC voltage gain: 100 dB (temperature compensated)
- Wide bandwidth (unity gain): 1.1 MHz
- Very low supply current per channel essentially independent of supply voltage
- Low input bias current: 20 nA (temperature compensated)
- Low input offset voltage: 2 mV
- Low input offset current: 2 nA
- Input common-mode voltage range includes negative rails
- Differential input voltage range equal to the power supply voltage
- Large output voltage swing: 0 V to (VCC+ - 1.5 V)

## Schematic diagram
*Schematic image omitted for brevity.*

## Package pin connections

**DFN8 2x2 (LM358QT Pinout, Top View):**

| Pin | Name   | Description      |
|-----|--------|------------------|
| 1   | OUT1   | Output 1         |
| 2   | -IN1   | Inverting In 1   |
| 3   | +IN1   | Non-inverting 1  |
| 4   | VCC-   | Negative V (GND) |
| 5   | +IN2   | Non-inverting 2  |
| 6   | -IN2   | Inverting In 2   |
| 7   | OUT2   | Output 2         |
| 8   | VCC+   | Positive V       |
| EPAD| —      | Exposed Pad (optional GND connection) |

Note: The exposed pad of the DFN8 2x2 can be left floating or connected to ground.

## Absolute maximum ratings
- Supply voltage: ±16 or 32V (±32V differential input)
- Operating range: 3 to 30V (typical)
- Operating temperature (LM358): 0°C to 70°C

## DFN8 2x2 package dimensions

| Ref | Millimeters (Min) | Typ | Max |
|-----|-------------------|-----|-----|
| A   | 0.51              |0.55 |0.60 |
| A1  | 0.18              |0.15 |0.05 |
| A3  | 0.15              |0.25 |0.30 |
| b   | 0.18              |0.25 |0.30 |
| D   | 1.85              |2.00 |2.15 |
| D2  | 1.45              |1.60 |1.70 |
| E   | 1.85              |2.00 |2.15 |
| E2  | 0.75              |0.90 |1.00 |
| e   | 0.50              |0.50 |0.50 |
| L   | 0.30              |0.40 |0.50 |
| ddd | —                 |0.08 |—    |

## DFN8 2x2 recommended footprint
*See datasheet Figure 31 for recommended footprint (to be used for footprint file).*

## Ordering information (for LM358QT)
| Order code | Package     | Marking | Packaging     |
|------------|-------------|---------|--------------|
| LM358QT    | DFN8 2x2    | K4E     | Tape & reel  |

## Source
STMicroelectronics, "LM158, LM258, LM358 Series Datasheet", November 2017, DocID2163 Rev 15
