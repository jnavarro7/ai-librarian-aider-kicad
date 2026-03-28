LM158, LM258, LM358,
LM158A, LM258A, LM358A

Low-power dual operational amplifiers

Datasheet - production data

Related products



See LM158W for enhanced ESD ratings
See LM2904 and LM2904W for automotive
grade versions

Description
These circuits consist of two independent, high-
gain, internally frequency-compensated op amps,
specifically designed to operate from a single
power supply over a wide range of voltages. The
low-power supply drain is independent of the
magnitude of the power supply voltage.

Application areas include transducer amplifiers,
DC gain blocks and all the conventional op amp
circuits, which can now be more easily
implemented in single power supply systems. For
example, these circuits can be directly supplied
with the standard 5 V, which is used in logic
systems and will easily provide the required
interface electronics with no additional power
supply.

In linear mode, the input common-mode voltage
range includes ground and the output voltage can
also swing to ground, even though operated from
only a single power supply voltage.

Features


Frequency compensation implemented
internally

Large DC voltage gain: 100 dB
  Wide bandwidth (unity gain): 1.1 MHz









(temperature compensated)
Very low supply current per channel
essentially independent of supply voltage
Low input bias current: 20 nA (temperature
compensated)
Low input offset voltage: 2 mV
Low input offset current: 2 nA
Input common-mode voltage range includes
negative rails

  Differential input voltage range equal to the



power supply voltage
Large output voltage swing
0 V to (VCC

+ - 1.5 V)

November 2017

DocID2163 Rev 15

This is information on a product in full production.

1/25

www.st.com

Contents

Contents

LM158, LM258, LM358, LM158A, LM258A,
LM358A

1

2

3
4

5

6

7

8

9

Schematic diagram .......................................................................... 3

Package pin connections ................................................................ 4

Absolute maximum ratings ............................................................. 5
Electrical characteristics ................................................................ 7

Electrical characteristic curves ...................................................... 9

Typical applications ...................................................................... 13

Package information ..................................................................... 16
SO8 package information ................................................................ 17

7.1

7.2

7.3

MiniSO8 package information ......................................................... 18

DFN8 2x2 package information ....................................................... 19

7.4

TSSOP8 package information ......................................................... 21
Ordering information ..................................................................... 22

Revision history ............................................................................ 23

2/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Schematic diagram

1

Schematic diagram

Figure 1: Schematic diagram (1/2 LM158)

DocID2163 Rev 15

3/25

6A4AQ2Q3Q4Q1InvertinginputNon-invertinginputQ8Q9Q10Q11Q1250AQ13OutputQ7Q6Q5RSCVCCCCGNDµµµAµ100

Package pin connections

LM158, LM258, LM358, LM158A, LM258A,
LM358A

2

Package pin connections

Figure 2: Pin connections (top view)

1.  The exposed pad of the DFN8 2x2 can be left floating or connected to ground

4/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Absolute maximum ratings

3

Absolute maximum ratings

Table 1: Absolute maximum ratings

Symbol

Parameter

LM158,A

LM258,A

LM358,A  Unit

VCC

Supply voltage

Vi

Vid

Input voltage

Differential input voltage

Output short-circuit duration (1)

Iin

Input current (2)

±16 or 32

-0.3 to 32

±32

Infinite

5 mA in DC or 50 mA in AC
(duty cycle = 10 %, T = 1 s)

Toper

Operating free-air temperature range

-55 to 125

-40 to 105

0 to 70

Tstg

Tj

Storage temperature range

Maximum junction temperature

Rthja

Thermal resistance junction to ambient
(3)

SO8

MiniSO8

DFN8 2x2

TSSOP8

SO8

Rthjc

Thermal resistance junction to case (3)

MiniSO8

TSSOP8

HBM: human body model (4)

ESD

MM: machine model (5)

CDM: charged device model (6)

-65 to 150

150

125

190

57

120

40

39

37

300

200

1.5

V

mA

°C

°C/W

V

kV

Notes:
(1)Short-circuits from the output to VCC can cause excessive heating if VCC > 15 V. The maximum output current is approximately
40 mA independent of the magnitude of VCC. Destructive dissipation can result from simultaneous short circuits on all amplifiers.
(2)This input current only exists when the voltage at any of the input leads is driven negative. It is due to the collector-base junction
of the input PNP transistor becoming forward-biased and thereby acting as input diode clamp. In addition to this diode action,
there is NPN parasitic action on the IC chip. This transistor action can cause the output voltages of the op amps to go to the VCC
voltage level (or to ground for a large overdrive) for the time during which an input is driven negative. This is not destructive and
normal output is restored for input voltages above -0.3 V.
(3)Short-circuits can cause excessive heating and destructive dissipation. Rth are typical values.
(4)Human body model: a 100 pF capacitor is charged to the specified voltage, then discharged through a 1.5 kΩ resistor between
two pins of the device. This is done for all couples of connected pin combinations while the other pins are floating.
(5)Machine model: a 200 pF capacitor is charged to the specified voltage, then discharged directly between two pins of the device
with no external series resistor (internal resistor < 5 Ω). This is done for all couples of connected pin combinations while the other
pins are floating.
(6)Charged device model: all pins and the package are charged together to the specified voltage and then discharged directly to
the ground through only one pin. This is done for all pins.

DocID2163 Rev 15

5/25

Absolute maximum ratings

Symbol

Parameter

VCC

Supply voltage

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Table 2: Operating conditions

Value

3 to 30

Unit

Vicm

Common mode input voltage range Tamb = 25°C (1)

(VCC-) to (VCC+ - 1.5)

V

Common mode input voltage range (Tmin ≤ Tamb ≤ Tmax) (2)

(VCC-) to (VCC+ - 2)

Toper

Operating free air temperature range

LM158

LM258

LM358

-55 to 125

-40 to 105

0 to 70

°C

Notes:
(1)When used in comparator, the functionality is guaranteed as long as at least one input remains within the operating common
mode voltage range.
(2)When used in comparator, the functionality is guaranteed as long as at least one input remains within the operating common
mode voltage range.

6/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Electrical characteristics

4

Electrical characteristics

Table 3: Electrical characteristics for VCC+ = 5 V, VCC- = Ground, Vo = 1.4 V, Tamb = 25 °C
(unless otherwise specified)

Min.  Typ.  Max.  Unit

Symbol

Vio

Input offset voltage (1)

Parameter

LM158A

LM258A, LM358A

LM158, LM258

LM358

Tmin ≤ Tamb ≤ Tmax

LM158, LM258

LM158A, LM258A, LM358A

ΔVio/ΔT

Input offset voltage drift

Input offset current

Iio

Tmin ≤ Tamb ≤ Tmax

ΔIio/ΔT

Input offset current drift

Input bias current (2)

Iib

Tmin ≤ Tamb ≤ Tmax

LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

LM158A, LM258A, LM358A

LM158, LM258, LM358

Avd

Large signal voltage gain

SVR

Supply voltage rejection
ratio

VCC

+ = 15 V, RL = 2 kΩ, Vo = 1.4 V to 11.4 V

Tmin ≤ Tamb ≤ Tmax

VCC

+ = 5 V to 30 V, Rs ≤ 10 kΩ

Tmin ≤ Tamb ≤ Tmax

ICC

Supply current, all amp,
no load

Tmin ≤ Tamb ≤ Tmax VCC

+ = 5 V

Tmin ≤ Tamb ≤ Tmax VCC

+ = 30 V

CMR

Common mode rejection
ratio

Rs ≤ 10 kΩ

Tmin ≤ Tamb ≤ Tmax

Isource

Output current source

VCC

+ = 15 V, Vo = 2 V, Vid = 1 V

Isink

Output sink current

VCC

+ = 15 V, Vo = 2 V, Vid = -1 V

VCC

+ = 15 V, Vo = 0.2 V, Vid = -1 V

50

25

65

65

70

60

20

10

12

DocID2163 Rev 15

2

3

5

7

4

7

9

15

30

10

30

30

40

200

300

50

150

100

200

1

2

7

7

2

2

10

10

20

20

100

100

0.7

1.2

2

60

85

40

20

50

mV

µV/°C

nA

pA/°C

nA

V/mV

dB

mA

dB

mA

mA

µA

7/25

Electrical characteristics

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Symbol

Parameter

Min.  Typ.  Max.  Unit

VOH

High level output voltage

VCC+ = 30 V, RL = 2 kΩ connected to VCC-,
Tamb = 25 °C

26

27

VCC+ = 30 V, RL = 2 kΩ connected to VCC-,
Tmin ≤ Tamb ≤ Tmax

26

VCC+ = 30 V, RL = 10 kΩ connected to VCC-,
Tamb = 25 °C

27

28

VCC+ = 30 V, RL = 10 kΩ connected to VCC-,
Tmin ≤ Tamb ≤ Tmax

VCC+ = 5 V, RL = 2 kΩ connected to VCC-,
Tamb = 25 °C

VCC+ = 5 V, RL = 2 kΩ connected to VCC-,
Tmin ≤ Tamb ≤ Tmax

27

3.5

3

VOL

Low level output voltage

SR

Slew rate

RL = 10 kΩ connected to VCC-

Tmin ≤ Tamb ≤ Tmax
VCC
CL = 100 pF, unity gain

+ = 15 V, Vi = 0.5 to 3 V, RL = 2 kΩ,

GBP

Gain bandwidth product

+ = 30 V, f = 100 kHz, Vin = 10 mV,

VCC
RL = 2 kΩ, CL = 100 pF

5

20

20

0.3

0.6

0.7

1.1

V

mV

V/µs

MHz

THD

Total harmonic distortion

f = 1 kHz, Av = 20 dB, RL = 2 kΩ, Vo = 2 Vpp,
CL = 100 pF, VO = 2 Vpp

0.02

%

en

Equivalent input noise
voltage

f = 1 kHz, Rs = 100 Ω, VCC

+ = 30 V

Vo1/Vo2  Channel separation (3)

1 kHz ≤ f ≤ 20 kHz

55

120

dB

Notes:
(1)Vo = 1.4 V, Rs = 0 Ω, 5 V < VCC
(2)The direction of the input current is out of the IC. This current is essentially constant, independent of the state of the output so
there is no change in the load on the input lines.
(3)Due to the proximity of external components, ensure that stray capacitance between these external parts does not cause
coupling. Typically, this can be detected because this type of capacitance increases at higher frequencies.

+ < 30 V, 0 < Vic < VCC

+ - 1.5 V

8/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Electrical characteristic curves

5

Electrical characteristic curves

Figure 3: Open-loop frequency response

Figure 4: Large signal frequency response

Figure 5: Voltage follower pulse response with
VCC = 15 V

Figure 6: Voltage follower pulse response with
VCC = 30 V

DocID2163 Rev 15

9/25

VOLTAGE GAIN (dB)1.010      100      1k       10k     100k     1M    10MVCC = +10 to +15 V &FREQUENCY (Hz)10 MVIVCC/2VCC = 30 V &-55°C0.1FVCCVO-+-55°CTamb+125°C140120100806040200Tamb+125°CΩµ-+OUTPUT SWING (Vpp)1k                   10k                       100k                 1MFREQUENCY (Hz)100 kVI1 kVO201510502 k +15 V +7 VΩΩΩINPUTVOLTAGE (V)TIME (s)RL2 kOUTPUTVOLTAGE (V)43210321VCC = +15 V0            10             20             30           40ΩμInputOutput50pFUPTUOTVOLT)Vm(EGA012345678eITamb=+25°CVCC=30V500450400350300250eOTIME(+-

Electrical characteristic curves

Figure 7: Input current

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Figure 8: Output voltage vs sink current

Figure 9: Output voltage vs source current

Figure 10: Current limiting

10/25

DocID2163 Rev 15

nA

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Electrical characteristic curves

Figure 11: Input voltage range

Figure 12: Open-loop gain

Figure 13: Supply current

Figure 14: Input current

Figure 15: Gain bandwidth product

Figure 16: Power supply rejection ratio

DocID2163 Rev 15

11/25

VOLTAGE GAIN (dB)POSITIVE SUPPLY VOLTAGE (V)0    10          20    30          401204016080ΩRL = 20 kRL = 2 kΩ

Electrical characteristic curves

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Figure 17: Common-mode rejection ratio

Figure 18: Phase margin vs. capacitive load

12/25

DocID2163 Rev 15

Phase margin at Vcc = 15 V andVicm = 7.5 Vvs. Iout and capacitive load valuePhase margin (°)50403020100-10001002003004005006007008009001000Iout (µA)Source for positive values/Sink for negative values70 pF, 103 pF, 138 pF, 170 pF, 220 pF, 290 pFCapacitive load valuesCI = 70 pFCI = 290 pFT = 25 °C

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Typical applications

6

Typical applications
Single supply voltage VCC = 5 VDC.

Figure 19: AC-coupled inverting amplifier

Figure 20: Non-inverting DC amplifier

Figure 21: AC-coupled non-inverting amplifier

Figure 22: DC summing amplifier

DocID2163 Rev 15

13/25

Typical applications

Figure 23: High input Z, DC differential amplifier

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Figure 24: High input Z adjustable gain DC
instrumentation amplifier

Figure 25: Using symmetrical amplifiers to reduce input
current

Figure 26: Low drift peak detector

14/25

DocID2163 Rev 15

ΩµΩΩµµΩ

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Typical applications

Figure 27: Active band-pass filter

DocID2163 Rev 15

15/25

Package information

LM158, LM258, LM358, LM158A, LM258A,
LM358A

7

Package information
In order to meet environmental requirements, ST offers these devices in different grades of
ECOPACK® packages, depending on their level of environmental compliance. ECOPACK®
specifications, grade definitions and product status are available at: www.st.com.
ECOPACK® is an ST trademark.

16/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A
7.1

SO8 package information

Figure 28: SO8 package outline

Package information

Table 4: SO8 mechanical data

Dimensions

Ref.

Millimeters

Min.

Typ.

A

A1

A2

b

c

D

E

E1

e

h

L

L1

k

ccc

0.10

1.25

0.28

0.17

4.80

5.80

3.80

0.25

0.40

0°

4.90

6.00

3.90

1.27

1.04

Max.

1.75

0.25

0.48

0.23

5.00

6.20

4.00

0.50

1.27

8°

0.10

Min.

0.004

0.049

0.011

0.007

0.189

0.228

0.150

0.010

0.016

0°

Inches

Typ.

0.193

0.236

0.154

0.050

0.040

Max

0.069

0.010

0.019

0.010

0.197

0.244

0.157

0.020

0.050

8°

0.004

DocID2163 Rev 15

17/25

Package information

LM158, LM258, LM358, LM158A, LM258A,
LM358A

7.2

MiniSO8 package information

Figure 29: MiniSO8 package outline

Table 5: MiniSO8 mechanical data

Dimensions

Ref.

Millimeters

Min.

Typ.

Max.

Min.

A

A1

A2

b

c

D

E

E1

e

L

L1

L2

k

ccc

0

0.75

0.22

0.08

2.80

4.65

2.80

0.40

0°

0.85

3.00

4.90

3.00

0.65

0.60

0.95

0.25

1.1

0.15

0.95

0.40

0.23

3.20

5.15

3.10

0

0.030

0.009

0.003

0.11

0.183

0.11

0.80

0.016

8°

0.10

0°

Inches

Typ.

0.033

0.118

0.193

0.118

0.026

0.024

0.037

0.010

Max.

0.043

0.006

0.037

0.016

0.009

0.126

0.203

0.122

0.031

8°

0.004

18/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A
7.3

DFN8 2x2 package information

Package information

Figure 30: DFN8 2x2 package outline

Table 6: DFN8 2x2 mechanical data

Dimensions

Ref.

Millimeters

Min.

0.51

0.18

1.85

1.45

1.85

0.75

Typ.

0.55

0.15

0.25

2.00

1.60

2.00

0.90

0.50

0.3

A

A1

A3

b

D

D2

E

E2

e

L

ddd

Max.

0.60

0.05

0.30

2.15

1.70

2.15

1.00

0.425

0.08

Min.

0.020

0.007

0.073

0.057

0.073

0.030

Inches

Typ.

0.022

0.006

0.010

0.079

0.063

0.079

0.035

0.020

0.012

Max.

0.024

0.002

0.012

0.085

0.067

0.085

0.039

0.017

0.003

DocID2163 Rev 15

19/25

Package information

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Figure 31: DFN8 2x2 recommended footprint

20/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A
7.4

TSSOP8 package information

Figure 32: TSSOP8 package outline

Package information

Table 7: TSSOP8 mechanical data

Dimensions

Ref.

Millimeters

Min.

Typ.

Max.

Min.

A

A1

A2

b

c

D

E

E1

e

k

L

L1

aaa

0.05

0.80

0.19

0.09

2.90

6.20

4.30

0°

0.45

1.00

3.00

6.40

4.40

0.65

0.60

1

0.1

1.2

0.15

1.05

0.30

0.20

3.10

6.60

4.50

8°

0.75

0.002

0.031

0.007

0.004

0.114

0.244

0.169

0°

0.018

Inches

Typ.

0.039

0.118

0.252

0.173

0.0256

0.024

0.039

0.004

Max.

0.047

0.006

0.041

0.012

0.008

0.122

0.260

0.177

8°

0.030

DocID2163 Rev 15

21/25

Ordering information

LM158, LM258, LM358, LM158A, LM258A,
LM358A

8

Ordering information

Order code

Temperature range

-55 °C to 125 °C

-40 °C to 105 °C

0 °C to 70 °C

LM158QT

LM158DT

LM258ADT

LM258AYDT (1)

LM258DT

LM258APT

LM258AST

LM258QT

LM358DT

LM358YDT(1)

LM358ADT

LM358PT
LM358APT

LM358ST
LM358AST

LM358QT

Table 8: Order codes

Package

DFN8 2x2

SO8

SO8

SO8, automotive grade

SO8

TSSOP8

MiniSO8

DFN8 2x2

SO8

SO8, automotive grade

SO8

TSSOP8

MiniSO8

DFN8 2x2

Packaging

Marking

Tape and reel

K4A

158

258A

258AY

258

258A

K408

K4C

358

358Y

358A

358
358A

K405
K404

K4E

Notes:
(1)Qualified and characterized according to AEC Q100 and Q003 or equivalent, advanced screening according to AEC Q001 & Q
002 or equivalent.

22/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

9

Revision history

Revision history

Date

Revision

Changes

Table 9: Document revision history

01-Jul- 2003

02-Jan-2005

01-Jul-2005

05-Oct-2006

30-Nov-2006

25-Apr-2007

1

2

3

4

5

6

12-Feb-2008

7

26-Aug-2008

8

02-Sep-2011

9

First release.

Rthja and Tj parameters added in AMR Table 1: "Absolute
maximum ratings".

ESD protection inserted in Table 1: "Absolute maximum ratings".

Added Figure 17: Phase margin vs. capacitive load.

Added missing ordering information.

Removed LM158A, LM258A and LM358A from document title.
Corrected error in MiniSO-8 package data. L1 is 0.004 inch.
Added automotive grade order codes in Section 7: "Ordering
information".

Corrected VCC max (30 V instead of 32 V) in operating conditions.
Changed presentation of electrical characteristics table.
Deleted Vopp parameter in electrical characteristics table.
Corrected miniSO-8 package information.
Corrected temperature range for automotive grade order codes.
Updated automotive grade footnotes in order codes table.

Added limitations on input current in Table 1: "Absolute maximum
ratings".
Corrected title for Figure 11.
Added E and L1 parameters in Table 4: "SO8 package mechanical
data".
Changed Figure 31: "TSSOP8 package mechanical drawing".

In Section 6: "Package information", added:
  DFN8 2 x 2 mm package mechanical drawing
  DFN8 2 x 2 mm recommended footprint
  DFN8 2 x 2 mm order codes.

06-Apr-2012

10

Removed order codes LM158YD, LM258AYD, LM258YD and
LM358YD from Table 8: "Order codes".

11-Jun-2013

11

Table 8: "Order codes": removed order codes LM158D,
LM158YDT, LM258YDT, and LM258AD; added automotive grade
qualification to order codes LM258ATDT and LM358YDT; updated
marking for order codes LM158DT and LM258D/LM258DT;
updated temperature range, packages, and packaging for several
order codes.

DocID2163 Rev 15

23/25

Revision history

LM158, LM258, LM358, LM158A, LM258A,
LM358A

Date

Revision

Changes

20-Jun-2014

12

13-Nov-2015

13

Removed DIP8 package
Corrected typos (W replaced with Ω, £ replaced with ≤)
Updated Features
Added Related products
Table 3: replaced DVio with ΔVio/ΔT and DIio with ΔIio/ΔT.
Updated Table 7 for exposed pad dimensions

Table 8: "Order codes": removed order codes LM258YPT and
LM258AYPT; removed all order codes for devices with tube
packing; added package code (NB) to DFN8 2x2 package.

Updated document layout
Updated name of the "DFN8 2x2 (NB) mm" package to "DFN8
2x2" everywhere in datasheet.
Section 2: "Package pin connections": placed the package's pinout
in this section and added note about exposed pad.

Table 8: "Order codes": removed order codes LM258ST,
LM358YPT, and LM358AYPT.

24-Aug-2016

14

Table 6: "DFN8 2x2 mechanical data": added typ. value for "L"
dimension.

22-Nov-2017

15

Updated: related products on the cover page.
Updated: Section 3: "Absolute maximum ratings", Table 2:
"Operating conditions", Section 4: "Electrical characteristics",
Figure 6: "Voltage follower pulse response with VCC = 30 V" and
Figure 7: "Input current".

24/25

DocID2163 Rev 15

LM158, LM258, LM358, LM158A, LM258A,
LM358A

IMPORTANT NOTICE – PLEASE READ CAREFULLY

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST
products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order
acknowledgement.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the
design of Purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2017 STMicroelectronics – All rights reserved

DocID2163 Rev 15

25/25


