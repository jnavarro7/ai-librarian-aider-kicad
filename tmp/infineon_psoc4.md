# Extracted Datasheet

Part: UNKNOWN
Package: ANY

## Page 5

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Table of contents
Table of contents
General description...........................................................................................................................1
Features...........................................................................................................................................1
More information..............................................................................................................................3
PSoC™ Creator..................................................................................................................................4
Table of contents...............................................................................................................................5
1 Functional overview .......................................................................................................................7
2 Functional definition.......................................................................................................................9
2.1 CPU and memory subsystem.................................................................................................................................9
2.1.1 CPU.......................................................................................................................................................................9
2.1.2 DMA/DataWire......................................................................................................................................................9
2.1.3 Flash.....................................................................................................................................................................9
2.1.4 SRAM.....................................................................................................................................................................9
2.1.5 SROM....................................................................................................................................................................9
2.2 System resources..................................................................................................................................................10
2.2.1 Power system.....................................................................................................................................................10
2.2.2 Clock system......................................................................................................................................................10
2.2.3 IMO clock source................................................................................................................................................10
2.2.4 ILO clock source.................................................................................................................................................11
2.2.5 Watch crystal oscillator (WCO)..........................................................................................................................11
2.2.6 Watchdog timer..................................................................................................................................................11
2.2.7 Reset...................................................................................................................................................................11
2.2.8 Voltage reference...............................................................................................................................................11
2.3 Analog blocks........................................................................................................................................................12
2.3.1 12-bit SAR ADC...................................................................................................................................................12
2.3.2 Four opamps (Continuous-time block; CTB)....................................................................................................12
2.3.3 VDAC (13 bits).....................................................................................................................................................13
2.3.4 Low-power comparators (LPC).........................................................................................................................13
2.3.5 Current DACs......................................................................................................................................................13
2.3.6 Analog multiplexed buses.................................................................................................................................13
2.3.7 Temperature sensor..........................................................................................................................................13
2.4 Fixed Function Digital...........................................................................................................................................13
2.4.1 Timer/Counter/PWM (TCPWM) block................................................................................................................13
2.4.2 Serial Communication block (SCB)...................................................................................................................14
2.5 GPIO.......................................................................................................................................................................14
2.6 Special Function Peripherals...............................................................................................................................15
2.6.1 CAPSENSE™........................................................................................................................................................15
2.7 WLCSP Package Bootloader.................................................................................................................................15
3 Pinouts........................................................................................................................................16
3.1 Alternate pin functions.........................................................................................................................................18
4 Power..........................................................................................................................................21
4.1 Mode 1: 1.8V to 5.5V External Supply.................................................................................................................21
4.2 Mode 2: 1.8V ± 5% External Supply.....................................................................................................................22
5 Development support...................................................................................................................23
5.1 Documentation.....................................................................................................................................................23
5.2 Online....................................................................................................................................................................23
5.3 Tools......................................................................................................................................................................23
6 Electrical specifications.................................................................................................................24
6.1 Absolute maximum ratings..................................................................................................................................24
6.2 Device Level Specifications..................................................................................................................................25
6.2.1 GPIO....................................................................................................................................................................27
6.2.2 XRES....................................................................................................................................................................29
Datasheet 5 002-22097 Rev. *F
2023-11-16
```

### Port Functions

| pin | name | description |
|---|---|---|
| P0.0 | Alternate function pin | Alternate function pin |
| P1.0 | Alternate function pin | Alternate function pin |
| VDDA | Alternate function pin | Alternate function pin |
| XRES | Alternate function pin | Alternate function pin |

## Page 12

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.3 Analog blocks
2.3.1 12-bit SAR ADC
The 12-bit, 1-Msps SAR ADC can operate at a maximum clock rate of 18 MHz and requires a minimum of 18 clocks
at that frequency to do a 12-bit conversion.
The Sample-and-Hold (S/H) aperture is programmable allowing the gain bandwidth requirements of the
amplifier driving the SAR inputs, which determine its settling time, to be relaxed if required. It is possible to
provide an external bypass (through a fixed pin location) for the internal reference amplifier.
The SAR is connected to a fixed set of pins through an 8-input sequencer. The sequencer cycles through selected
channels autonomously (sequencer scan) with zero switching overhead (that is, aggregate sampling bandwidth
is equal to 1Msps whether it is for a single channel or distributed over several channels). The sequencer switching
is effected through a state machine or through firmware driven switching. A feature provided by the sequencer
is buffering of each channel to reduce CPU interrupt service requirements. To accommodate signals with varying
source impedance and frequency, it is possible to have different sample times programmable for each channel.
Also, signal range specification through a pair of range registers (low and high range values) is implemented with
a corresponding out-of-range interrupt if the digitized value exceeds the programmed range; this allows fast
detection of out-of-range values without the necessity of having to wait for a sequencer scan to be completed
and the CPU to read the values and check for out-of-range values in software.
The SAR is not available in Deep Sleep mode as it requires a high-speed clock (up to 18 MHz). The SAR operating
range is 1.71V to 5.5 V.
Figure 4 SAR ADC
2.3.2 Four opamps (Continuous-time block; CTB)
PSoC™ 4100PS has four opamps with Comparator modes which allow most common analog functions to be
performed on-chip eliminating external components; PGAs, Voltage Buffers, Filters, Trans-Impedance Amplifiers,
and other functions can be realized, in some cases with external passives, saving power, cost, and space. The
on-chip opamps are designed with enough bandwidth to drive the Sample-and-Hold circuit of the ADC without
requiring external buffering.
Datasheet 12 002-22097 Rev. *F
2023-11-16
troP
XUMRAS
)stupni
8(
0P
7P
XUMRAS
sulpvsunimv
AHB System Bus and Programmable Logic
Interconnect
SAR Sequencer
Sequencing
and Control Data and
POS Status Flags
SARADC
NEG
Reference R E e x fe te re rn n a c l e
Selection and
Bypass
(optional)
VDDA/2 VDDA VREF
Inputs from other Ports
```

## Page 16

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Pinouts
3 Pinouts
The following table provides the pin list for PSoC™ 4100PS for the 48-pin QFN, 48-pin TQFP, 45-ball WLCSP, and
28-pin SSOP packages. All port pins support GPIO.
Table 1 Pinouts
Packages
48-pin QFN 48-pin TQFP 28-pin SSOP 45-ball CSP
Pin Name Pin Name Pin Name Pin Name
28 P0.0 28 P0.0 21 P0.0 D3 P0.0
29 P0.1 29 P0.1 22 P0.1 E2 P0.1
30 P0.2 30 P0.2 23 P0.2 D2 P0.2
31 P0.3 31 P0.3 C3 P0.3
32 P0.4 32 P0.4 D1 P0.4
33 P0.5 33 P0.5 E1 P0.5
34 P0.6 34 P0.6 C2 P0.6
35 P0.7 35 P0.7 B2 P0.7
36 XRES 36 XRES 24 XRES B3 XRES
37 P4.0 37 P4.0 A1 P4.0
38 P4.1 38 P4.1 B1 P4.1
39 P5.0 39 P5.0 25 P5.0 B4 P5.0
40 P5.1 40 P5.1 C1 P5.1
41 P5.2 41 P5.2 26 P5.2 A2 P5.2
42 P5.3 42 P5.3 27 P5.3 A3 P5.3
43 VDDA 43 VDDA 28 VDDA J2 VDDA
44 VSSA 44 VSSA J3 VSSA
45 VCCD 45 VCCD 1 VCCD A4 VCCD
B5 VDDD
46 VSSD 46 VSSD 2 VSSD A5 VSSD
47 VDDD 47 VDDD 3 VDDD
48 P1.0 48 P1.0 4 P1.0 C5 P1.0
1 P1.1 1 P1.1 5 P1.1 C4 P1.1
2 P1.2 2 P1.2 6 P1.2 D5 P1.2
3 P1.3 3 P1.3 7 P1.3 D4 P1.3
4 P1.4 4 P1.4 E3 P1.4
5 P1.5 5 P1.5 E4 P1.5
6 P1.6 6 P1.6
7 P1.7 7 P1.7 G3 P1.7
8 VDDA 8 VDDA 8 VDDA E5 VDDA
9 VSSA 9 VSSA 9 VSSA F5 VSSA
10 P2.0 10 P2.0 10 P2.0 F4 P2.0
11 P2.1 11 P2.1 11 P2.1 F3 P2.1
Datasheet 16 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Packages |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 48-pin QFN |  | 48-pin TQFP |  | 28-pin SSOP |  | 45-ball CSP |  |
| Pin | Name | Pin | Name | Pin | Name | Pin | Name |
| 28 | P0.0 | 28 | P0.0 | 21 | P0.0 | D3 | P0.0 |
| 29 | P0.1 | 29 | P0.1 | 22 | P0.1 | E2 | P0.1 |
| 30 | P0.2 | 30 | P0.2 | 23 | P0.2 | D2 | P0.2 |
| 31 | P0.3 | 31 | P0.3 |  |  | C3 | P0.3 |
| 32 | P0.4 | 32 | P0.4 |  |  | D1 | P0.4 |
| 33 | P0.5 | 33 | P0.5 |  |  | E1 | P0.5 |
| 34 | P0.6 | 34 | P0.6 |  |  | C2 | P0.6 |
| 35 | P0.7 | 35 | P0.7 |  |  | B2 | P0.7 |
| 36 | XRES | 36 | XRES | 24 | XRES | B3 | XRES |
| 37 | P4.0 | 37 | P4.0 |  |  | A1 | P4.0 |
| 38 | P4.1 | 38 | P4.1 |  |  | B1 | P4.1 |
| 39 | P5.0 | 39 | P5.0 | 25 | P5.0 | B4 | P5.0 |
| 40 | P5.1 | 40 | P5.1 |  |  | C1 | P5.1 |
| 41 | P5.2 | 41 | P5.2 | 26 | P5.2 | A2 | P5.2 |
| 42 | P5.3 | 42 | P5.3 | 27 | P5.3 | A3 | P5.3 |
| 43 | VDDA | 43 | VDDA | 28 | VDDA | J2 | VDDA |
| 44 | VSSA | 44 | VSSA |  |  | J3 | VSSA |
| 45 | VCCD | 45 | VCCD | 1 | VCCD | A4 | VCCD |
|  |  |  |  |  |  | B5 | VDDD |
| 46 | VSSD | 46 | VSSD | 2 | VSSD | A5 | VSSD |
| 47 | VDDD | 47 | VDDD | 3 | VDDD |  |  |
| 48 | P1.0 | 48 | P1.0 | 4 | P1.0 | C5 | P1.0 |
| 1 | P1.1 | 1 | P1.1 | 5 | P1.1 | C4 | P1.1 |
| 2 | P1.2 | 2 | P1.2 | 6 | P1.2 | D5 | P1.2 |
| 3 | P1.3 | 3 | P1.3 | 7 | P1.3 | D4 | P1.3 |
| 4 | P1.4 | 4 | P1.4 |  |  | E3 | P1.4 |
| 5 | P1.5 | 5 | P1.5 |  |  | E4 | P1.5 |
| 6 | P1.6 | 6 | P1.6 |  |  |  |  |
| 7 | P1.7 | 7 | P1.7 |  |  | G3 | P1.7 |
| 8 | VDDA | 8 | VDDA | 8 | VDDA | E5 | VDDA |
| 9 | VSSA | 9 | VSSA | 9 | VSSA | F5 | VSSA |
| 10 | P2.0 | 10 | P2.0 | 10 | P2.0 | F4 | P2.0 |
| 11 | P2.1 | 11 | P2.1 | 11 | P2.1 | F3 | P2.1 |

### Port Functions

| pin | name | description |
|---|---|---|
| P0.0 | P0.0 |  |
| P1.0 | P1.0 |  |
| XRES | XRES |  |
| P4.0 | P4.0 |  |
| VDDA | VDDA |  |
| P5.0 | P5.0 |  |
| VCCD | VCCD |  |
| P1.4 | P1.4 |  |
| VSSA | VSSA |  |

## Page 17

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Pinouts
Table 1 Pinouts (continued)
Packages
48-pin QFN 48-pin TQFP 28-pin SSOP 45-ball CSP
Pin Name Pin Name Pin Name Pin Name
12 P2.2 12 P2.2 12 P2.2 G4 P2.2
13 P2.3 13 P2.3 13 P2.3 G5 P2.3
14 P2.4 14 P2.4 H5 P2.4
15 P2.5 15 P2.5 J4 P2.5
16 P2.6 16 P2.6 H4 P2.6
17 P2.7/VREF 17 P2.7/VREF 14 P2.7/VREF J5 P2.7/VREF
18 VSSA 18 VSSA J3 VSSA
19 VDDA 19 VDDA 15 VDDA J2 VDDA
20 P3.0 20 P3.0 H2 P3.0
21 P3.1 21 P3.1 16 P3.1 F2 P3.1
22 P3.2 22 P3.2 17 P3.2 J1 P3.2
23 P3.3 23 P3.3 18 P3.3 H3 P3.3
24 P3.4 24 P3.4 F1 P3.4
25 P3.5 25 P3.5 G2 P3.5
26 P3.6 26 P3.6 19 P3.6 G1 P3.6
27 P3.7 27 P3.7 20 P3.7 H1 P3.7
Descriptions of the Power pins are as follows:
VDDD: Power supply for the digital section.
VDDA: Power supply for the analog section.
VSS: Ground pin.
VCCD: Regulated digital supply (1.8 V ± 5%)
The 48-pin packages have 38 I/O pins. The 45-ball CSP and the 28-pin SSOP have 37 and 20 I/O pins respectively.
Datasheet 17 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Packages |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 48-pin QFN |  | 48-pin TQFP |  | 28-pin SSOP |  | 45-ball CSP |  |
| Pin | Name | Pin | Name | Pin | Name | Pin | Name |
| 12 | P2.2 | 12 | P2.2 | 12 | P2.2 | G4 | P2.2 |
| 13 | P2.3 | 13 | P2.3 | 13 | P2.3 | G5 | P2.3 |
| 14 | P2.4 | 14 | P2.4 |  |  | H5 | P2.4 |
| 15 | P2.5 | 15 | P2.5 |  |  | J4 | P2.5 |
| 16 | P2.6 | 16 | P2.6 |  |  | H4 | P2.6 |
| 17 | P2.7/VREF | 17 | P2.7/VREF | 14 | P2.7/VREF | J5 | P2.7/VREF |
| 18 | VSSA | 18 | VSSA |  |  | J3 | VSSA |
| 19 | VDDA | 19 | VDDA | 15 | VDDA | J2 | VDDA |
| 20 | P3.0 | 20 | P3.0 |  |  | H2 | P3.0 |
| 21 | P3.1 | 21 | P3.1 | 16 | P3.1 | F2 | P3.1 |
| 22 | P3.2 | 22 | P3.2 | 17 | P3.2 | J1 | P3.2 |
| 23 | P3.3 | 23 | P3.3 | 18 | P3.3 | H3 | P3.3 |
| 24 | P3.4 | 24 | P3.4 |  |  | F1 | P3.4 |
| 25 | P3.5 | 25 | P3.5 |  |  | G2 | P3.5 |
| 26 | P3.6 | 26 | P3.6 | 19 | P3.6 | G1 | P3.6 |
| 27 | P3.7 | 27 | P3.7 | 20 | P3.7 | H1 | P3.7 |

### Port Functions

| pin | name | description |
|---|---|---|
| P0.0 | P0.0 |  |
| P1.0 | P1.0 |  |
| VDDA | VDDA | Power supply for the analog section. |
| XRES | XRES |  |

## Page 18

### Raw Page Text

```text
2023-11-16
Datasheet
18
002-22097
Rev.
*F
Pinouts Based
on
Arm®
Cortex™-M0+
PSoC™
4100PS
3.1 Alternate pin functions
Each Port pin has can be assigned to one of multiple functions; it can, for example, be an Analog I/O, a Digital Peripheral function, or a CapSense or LCD
pin. The pin assignments are shown in the following table.
Table 2 Alternate pin functions
Active DeepSleep
Port/Pin Analog SmartIO
ACT #0 ACT #1 ACT #2 ACT #3 DS #0 DS #1
scb[0].spi_
P0.0 SmartIO[0].io[0] tcpwm.line[4]:1 tcpwm.tr_in[0] cpuss.swd_data:0
select1:0
tcpwm.line_ scb[0].spi_
P0.1 SmartIO[0].io[1] tcpwm.tr_in[1] cpuss.swd_clk:0
compl[4]:1 select2:0
scb[0].spi_
P0.2 SmartIO[0].io[2] tcpwm.line[5]:1 srss.ext_clk
select3:0
tcpwm.line_
P0.3 SmartIO[0].io[3]
compl[5]:1
scb[1].spi_
P0.4 SmartIO[0].io[4] tcpwm.line[6]:1 scb[1].uart_rx:0 scb[1].i2c_scl:0
mosi:0
tcpwm.line_ scb[1].spi_
P0.5 SmartIO[0].io[5] scb[1].uart_tx:0 scb[1].i2c_sda:0
compl[6]:1 miso:0
scb[1].spi_
P0.6 SmartIO[0].io[6] scb[1].uart_cts:0 lpcomp.comp[0]:0
clk:0
scb[1].spi_
P0.7 SmartIO[0].io[7] scb[1].uart_rts:0 lpcomp.comp[1]:0
select0:0
scb[2].spi_
P4.0 wco_in tcpwm.line[0]:2 scb[2].uart_rx:1 tcpwm.tr_in[5] scb[2].i2c_scl:1
mosi:1
tcpwm.line_ scb[2].spi_
P4.1 wco_out scb[2].uart_tx:1 tcpwm.tr_in[6] scb[2].i2c_sda:1
compl[0]:2 miso:1
scb[0].spi_
P5.0 csd.cshieldpads tcpwm.line[7]:1 scb[0].uart_rx:1 scb[0].i2c_scl:1
mosi:1
tcpwm.line_ scb[0].spi_
P5.1 csd.vref_ext scb[0].uart_tx:1 scb[0].i2c_sda:1
compl[7]:1 miso:1
scb[0].spi_
P5.2 csd.dsi_cmod tcpwm.line[6]:2 scb[0].uart_cts:1 tr_sar_out
clk:1
```

### Extracted Tables

#### Table 1

| Port/Pin | Analog | SmartIO | Active |  |  |  | DeepSleep |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | ACT #0 | ACT #1 | ACT #2 | ACT #3 | DS #0 | DS #1 |
| P0.0 |  | SmartIO[0].io[0] | tcpwm.line[4]:1 |  |  | tcpwm.tr_in[0] | cpuss.swd_data:0 |  |
| P0.1 |  | SmartIO[0].io[1] | tcpwm.line_ compl[4]:1 |  |  | tcpwm.tr_in[1] | cpuss.swd_clk:0 |  |
| P0.2 |  | SmartIO[0].io[2] | tcpwm.line[5]:1 |  | srss.ext_clk |  |  |  |
| P0.3 |  | SmartIO[0].io[3] | tcpwm.line_ compl[5]:1 |  |  |  |  |  |
| P0.4 |  | SmartIO[0].io[4] | tcpwm.line[6]:1 | scb[1].uart_rx:0 |  |  | scb[1].i2c_scl:0 |  |
| P0.5 |  | SmartIO[0].io[5] | tcpwm.line_ compl[6]:1 | scb[1].uart_tx:0 |  |  | scb[1].i2c_sda:0 |  |
| P0.6 |  | SmartIO[0].io[6] |  | scb[1].uart_cts:0 |  |  | lpcomp.comp[0]:0 |  |
| P0.7 |  | SmartIO[0].io[7] |  | scb[1].uart_rts:0 |  |  | lpcomp.comp[1]:0 |  |
| P4.0 | wco_in |  | tcpwm.line[0]:2 | scb[2].uart_rx:1 |  | tcpwm.tr_in[5] | scb[2].i2c_scl:1 |  |
| P4.1 | wco_out |  | tcpwm.line_ compl[0]:2 | scb[2].uart_tx:1 |  | tcpwm.tr_in[6] | scb[2].i2c_sda:1 |  |
| P5.0 | csd.cshieldpads |  | tcpwm.line[7]:1 | scb[0].uart_rx:1 |  |  | scb[0].i2c_scl:1 |  |
| P5.1 | csd.vref_ext |  | tcpwm.line_ compl[7]:1 | scb[0].uart_tx:1 |  |  | scb[0].i2c_sda:1 |  |
| P5.2 | csd.dsi_cmod |  | tcpwm.line[6]:2 | scb[0].uart_cts:1 | tr_sar_out |  |  |  |

### Port Functions

| pin | name | description |
|---|---|---|
| P0.0 |  | SmartIO[0].io[0] \| tcpwm.line[4]:1 \| \| \| tcpwm.tr_in[0] \| cpuss.swd_data:0 \| |
| P0.1 |  | SmartIO[0].io[1] \| tcpwm.line_ compl[4]:1 \| \| \| tcpwm.tr_in[1] \| cpuss.swd_clk:0 \| |
| P0.2 |  | SmartIO[0].io[2] \| tcpwm.line[5]:1 \| \| srss.ext_clk \| \| \| |
| P0.3 |  | SmartIO[0].io[3] \| tcpwm.line_ compl[5]:1 \| \| \| \| \| |
| P0.4 |  | SmartIO[0].io[4] \| tcpwm.line[6]:1 \| scb[1].uart_rx:0 \| \| \| scb[1].i2c_scl:0 \| |
| P0.5 |  | SmartIO[0].io[5] \| tcpwm.line_ compl[6]:1 \| scb[1].uart_tx:0 \| \| \| scb[1].i2c_sda:0 \| |
| P0.6 |  | SmartIO[0].io[6] \| \| scb[1].uart_cts:0 \| \| \| lpcomp.comp[0]:0 \| |
| P0.7 |  | SmartIO[0].io[7] \| \| scb[1].uart_rts:0 \| \| \| lpcomp.comp[1]:0 \| |
| P4.0 | wco_in | \| tcpwm.line[0]:2 \| scb[2].uart_rx:1 \| \| tcpwm.tr_in[5] \| scb[2].i2c_scl:1 \| |
| P4.1 | wco_out | \| tcpwm.line_ compl[0]:2 \| scb[2].uart_tx:1 \| \| tcpwm.tr_in[6] \| scb[2].i2c_sda:1 \| |
| P5.0 | csd.cshieldpads | \| tcpwm.line[7]:1 \| scb[0].uart_rx:1 \| \| \| scb[0].i2c_scl:1 \| |
| P5.1 | csd.vref_ext | \| tcpwm.line_ compl[7]:1 \| scb[0].uart_tx:1 \| \| \| scb[0].i2c_sda:1 \| |
| P5.2 | csd.dsi_cmod | \| tcpwm.line[6]:2 \| scb[0].uart_cts:1 \| tr_sar_out \| \| \| |

## Page 19

### Raw Page Text

```text
2023-11-16
Datasheet
19
002-22097
Rev.
*F
Pinouts Based
on
Arm®
Cortex™-M0+
PSoC™
4100PS
Table 2 Alternate pin functions (continued)
Active DeepSleep
Port/Pin Analog SmartIO
ACT #0 ACT #1 ACT #2 ACT #3 DS #0 DS #1
csd.dsi_csh_ tcpwm.line_ scb[0].spi_
P5.3 scb[0].uart_rts:1
tank compl[6]:2 select0:1
ctb_pads[8] scb[1].spi_
P1.0 tcpwm.line[0]:1 scb[1].uart_rx:1 scb[1].i2c_scl:1
lpcomp.in_p[1] mosi:1
ctb_pads[9] tcpwm.line_ scb[1].spi_
P1.1 scb[1].uart_tx:1 scb[1].i2c_sda:1
lpcomp.in_n[1] compl[0]:1 miso:1
ctb_pads[10]
scb[1].spi_
P1.2 ctb_oa0_ tcpwm.line[1]:1 scb[1].uart_cts:1
clk:1
out_10x[1]
ctb_pads[11]
tcpwm.line_ scb[1].spi_
P1.3 ctb_oa1_ scb[1].uart_rts:1
compl[1]:1 select0:1
out_10x[1]
scb[1].spi_
P1.4 ctb_pads[12] tcpwm.line[2]:1
select1:0
tcpwm.line_ scb[1].spi_
P1.5 ctb_pads[13]
compl[2]:1 select2:0
scb[1].spi_
P1.6 ctb_pads[14] tcpwm.line[3]:1
select3:0
tcpwm.line_
P1.7 ctb_pads[15]
compl[3]:1
scb[2].spi_
P2.0 ctb_pads[0] tcpwm.line[4]:0 scb[2].uart_rx:0 scb[2].i2c_scl:0
mosi:0
tcpwm.line_ scb[2].spi_
P2.1 ctb_pads[1] scb[2].uart_tx:0 scb[2].i2c_sda:0
compl[4]:0 miso:0
ctb_pads[2]
scb[2].spi_
P2.2 ctb_oa0_ tcpwm.line[5]:0 scb[2].uart_cts:0
clk:0
out_10x[0]
ctb_pads[3]
tcpwm.line_ scb[2].spi_
P2.3 ctb_oa1_ scb[2].uart_rts:0
compl[5]:0 select0:0
out_10x[0]
scb[2].spi_
P2.4 ctb_pads[4] tcpwm.line[0]:0
select1:0
```

### Extracted Tables

#### Table 1

| Port/Pin | Analog | SmartIO | Active |  |  |  | DeepSleep |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | ACT #0 | ACT #1 | ACT #2 | ACT #3 | DS #0 | DS #1 |
| P5.3 | csd.dsi_csh_ tank |  | tcpwm.line_ compl[6]:2 | scb[0].uart_rts:1 |  |  |  |  |
| P1.0 | ctb_pads[8] lpcomp.in_p[1] |  | tcpwm.line[0]:1 | scb[1].uart_rx:1 |  |  | scb[1].i2c_scl:1 |  |
| P1.1 | ctb_pads[9] lpcomp.in_n[1] |  | tcpwm.line_ compl[0]:1 | scb[1].uart_tx:1 |  |  | scb[1].i2c_sda:1 |  |
| P1.2 | ctb_pads[10] ctb_oa0_ out_10x[1] |  | tcpwm.line[1]:1 | scb[1].uart_cts:1 |  |  |  |  |
| P1.3 | ctb_pads[11] ctb_oa1_ out_10x[1] |  | tcpwm.line_ compl[1]:1 | scb[1].uart_rts:1 |  |  |  |  |
| P1.4 | ctb_pads[12] |  | tcpwm.line[2]:1 |  |  |  |  |  |
| P1.5 | ctb_pads[13] |  | tcpwm.line_ compl[2]:1 |  |  |  |  |  |
| P1.6 | ctb_pads[14] |  | tcpwm.line[3]:1 |  |  |  |  |  |
| P1.7 | ctb_pads[15] |  | tcpwm.line_ compl[3]:1 |  |  |  |  |  |
| P2.0 | ctb_pads[0] |  | tcpwm.line[4]:0 | scb[2].uart_rx:0 |  |  | scb[2].i2c_scl:0 |  |
| P2.1 | ctb_pads[1] |  | tcpwm.line_ compl[4]:0 | scb[2].uart_tx:0 |  |  | scb[2].i2c_sda:0 |  |
| P2.2 | ctb_pads[2] ctb_oa0_ out_10x[0] |  | tcpwm.line[5]:0 | scb[2].uart_cts:0 |  |  |  |  |
| P2.3 | ctb_pads[3] ctb_oa1_ out_10x[0] |  | tcpwm.line_ compl[5]:0 | scb[2].uart_rts:0 |  |  |  |  |
| P2.4 | ctb_pads[4] |  | tcpwm.line[0]:0 |  |  |  |  |  |

### Port Functions

| pin | name | description |
|---|---|---|
| P5.3 | csd.dsi_csh_ tank | \| tcpwm.line_ compl[6]:2 \| scb[0].uart_rts:1 \| \| \| \| |
| P1.0 | ctb_pads[8] lpcomp.in_p[1] | \| tcpwm.line[0]:1 \| scb[1].uart_rx:1 \| \| \| scb[1].i2c_scl:1 \| |
| P1.1 | ctb_pads[9] lpcomp.in_n[1] | \| tcpwm.line_ compl[0]:1 \| scb[1].uart_tx:1 \| \| \| scb[1].i2c_sda:1 \| |
| P1.2 | ctb_pads[10] ctb_oa0_ out_10x[1] | \| tcpwm.line[1]:1 \| scb[1].uart_cts:1 \| \| \| \| |
| P1.3 | ctb_pads[11] ctb_oa1_ out_10x[1] | \| tcpwm.line_ compl[1]:1 \| scb[1].uart_rts:1 \| \| \| \| |
| P1.4 | ctb_pads[12] | \| tcpwm.line[2]:1 \| \| \| \| \| |
| P1.5 | ctb_pads[13] | \| tcpwm.line_ compl[2]:1 \| \| \| \| \| |
| P1.6 | ctb_pads[14] | \| tcpwm.line[3]:1 \| \| \| \| \| |
| P1.7 | ctb_pads[15] | \| tcpwm.line_ compl[3]:1 \| \| \| \| \| |
| P2.0 | ctb_pads[0] | \| tcpwm.line[4]:0 \| scb[2].uart_rx:0 \| \| \| scb[2].i2c_scl:0 \| |
| P2.1 | ctb_pads[1] | \| tcpwm.line_ compl[4]:0 \| scb[2].uart_tx:0 \| \| \| scb[2].i2c_sda:0 \| |
| P2.2 | ctb_pads[2] ctb_oa0_ out_10x[0] | \| tcpwm.line[5]:0 \| scb[2].uart_cts:0 \| \| \| \| |
| P2.3 | ctb_pads[3] ctb_oa1_ out_10x[0] | \| tcpwm.line_ compl[5]:0 \| scb[2].uart_rts:0 \| \| \| \| |
| P2.4 | ctb_pads[4] | \| tcpwm.line[0]:0 \| \| \| \| \| |

## Page 20

### Raw Page Text

```text
2023-11-16
Datasheet
20
002-22097
Rev.
*F
Pinouts Based
on
Arm®
Cortex™-M0+
PSoC™
4100PS
Table 2 Alternate pin functions (continued)
Active DeepSleep
Port/Pin Analog SmartIO
ACT #0 ACT #1 ACT #2 ACT #3 DS #0 DS #1
tcpwm.line_ scb[2].spi_
P2.5 ctb_pads[5]
compl[0]:0 select2:0
scb[2].spi_
P2.6 ctb_pads[6] tcpwm.line[1]:0
select3:0
tcpwm.line_
ctb_pads[7]
compl[1]:0
sar_ext_
P2.7
vref0
sar_ext_
vref1
scb[0].spi_
P3.0 sarmux[0] tcpwm.line[2]:0 scb[0].uart_rx:0 scb[0].i2c_scl:0
mosi:0
tcpwm.line_ scb[0].spi_
P3.1 sarmux[1] scb[0].uart_tx:0 scb[0].i2c_sda:0
compl[2]:0 miso:0
sarmux[2]
scb[0].spi_
P3.2 lpcomp.in_ tcpwm.line[3]:0 scb[0].uart_cts:0
clk:0
p[0]
sarmux[3]
tcpwm.line_ scb[0].spi_
P3.3 lpcomp.in_ scb[0].uart_rts:0
compl[3]:0 select0:0
n[0]
scb[0].spi_
P3.4 sarmux[4] tcpwm.line[6]:0 tcpwm.tr_in[2]
select1:1
tcpwm.line_ scb[0].spi_
P3.5 sarmux[5] tcpwm.tr_in[3] csd.comp
compl[6]:0 select2:1
scb[2].spi_
P3.6 sarmux[6] tcpwm.line[7]:0 scb[2].uart_rx:2 tcpwm.tr_in[4] scb[2].i2c_scl:2
mosi:2
tcpwm.line_ scb[2].spi_
P3.7 sarmux[7] scb[2].uart_tx:2 scb[2].i2c_sda:2
compl[7]:0 miso:2
Refer to the Technical Reference Manual (TRM) for CTB connection details. The VDAC outputs are buffered through the CTB outputs; any VDAC output
may be routed to any CTB output.
```

### Extracted Tables

#### Table 1

| Port/Pin | Analog | SmartIO | Active |  |  |  | DeepSleep |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | ACT #0 | ACT #1 | ACT #2 | ACT #3 | DS #0 | DS #1 |
| P2.5 | ctb_pads[5] |  | tcpwm.line_ compl[0]:0 |  |  |  |  |  |
| P2.6 | ctb_pads[6] |  | tcpwm.line[1]:0 |  |  |  |  |  |
| P2.7 | ctb_pads[7] |  | tcpwm.line_ compl[1]:0 |  |  |  |  |  |
|  | sar_ext_ vref0 sar_ext_ vref1 |  |  |  |  |  |  |  |
| P3.0 | sarmux[0] |  | tcpwm.line[2]:0 | scb[0].uart_rx:0 |  |  | scb[0].i2c_scl:0 |  |
| P3.1 | sarmux[1] |  | tcpwm.line_ compl[2]:0 | scb[0].uart_tx:0 |  |  | scb[0].i2c_sda:0 |  |
| P3.2 | sarmux[2] lpcomp.in_ p[0] |  | tcpwm.line[3]:0 | scb[0].uart_cts:0 |  |  |  |  |
| P3.3 | sarmux[3] lpcomp.in_ n[0] |  | tcpwm.line_ compl[3]:0 | scb[0].uart_rts:0 |  |  |  |  |
| P3.4 | sarmux[4] |  | tcpwm.line[6]:0 |  |  | tcpwm.tr_in[2] |  |  |
| P3.5 | sarmux[5] |  | tcpwm.line_ compl[6]:0 |  |  | tcpwm.tr_in[3] | csd.comp |  |
| P3.6 | sarmux[6] |  | tcpwm.line[7]:0 | scb[2].uart_rx:2 |  | tcpwm.tr_in[4] | scb[2].i2c_scl:2 |  |
| P3.7 | sarmux[7] |  | tcpwm.line_ compl[7]:0 | scb[2].uart_tx:2 |  |  | scb[2].i2c_sda:2 |  |

### Port Functions

| pin | name | description |
|---|---|---|
| P2.5 | ctb_pads[5] | \| tcpwm.line_ compl[0]:0 \| \| \| \| \| |
| P2.6 | ctb_pads[6] | \| tcpwm.line[1]:0 \| \| \| \| \| |
| P2.7 | ctb_pads[7] | \| tcpwm.line_ compl[1]:0 \| \| \| \| \| |
| P3.0 | sarmux[0] | \| tcpwm.line[2]:0 \| scb[0].uart_rx:0 \| \| \| scb[0].i2c_scl:0 \| |
| P3.1 | sarmux[1] | \| tcpwm.line_ compl[2]:0 \| scb[0].uart_tx:0 \| \| \| scb[0].i2c_sda:0 \| |
| P3.2 | sarmux[2] lpcomp.in_ p[0] | \| tcpwm.line[3]:0 \| scb[0].uart_cts:0 \| \| \| \| |
| P3.3 | sarmux[3] lpcomp.in_ n[0] | \| tcpwm.line_ compl[3]:0 \| scb[0].uart_rts:0 \| \| \| \| |
| P3.4 | sarmux[4] | \| tcpwm.line[6]:0 \| \| \| tcpwm.tr_in[2] \| \| |
| P3.5 | sarmux[5] | \| tcpwm.line_ compl[6]:0 \| \| \| tcpwm.tr_in[3] \| csd.comp \| |
| P3.6 | sarmux[6] | \| tcpwm.line[7]:0 \| scb[2].uart_rx:2 \| \| tcpwm.tr_in[4] \| scb[2].i2c_scl:2 \| |
| P3.7 | sarmux[7] | \| tcpwm.line_ compl[7]:0 \| scb[2].uart_tx:2 \| \| \| scb[2].i2c_sda:2 \| |

## Page 41

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.7 CAPSENSE™ and IDAC
Table 17 CAPSENSE™ and IDAC specifications[7]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Max allowed ripple V > 2V (with
DD
SYS.PER#3 VDD_RIPPLE on power supply, - - ±50 mV ripple), 25°C T ,
A
DC to 10MHz Sensitivity = 0.1pF
V > 1.75V (with
DD
ripple), 25°C T ,
Max allowed ripple A
Parasitic
SYS.PER#16 VDD_RIPPLE_1.8 on power supply, - - ±25 mV
Capacitance
DC to 10MHz
(CP) < 20pF,
Sensitivity ≥ 0.4 pF
Maximum block
SID.CSD.BLK ICSD - - 4000 µA -
current
Voltage reference
V - 0.6 V or 4.4 V,
SID.CSD#15 VREF for CSD and 0.6 1.2 V - 0.6 V DDA
DDA whichever is lower
Comparator
External Voltage
V - 0.6 V or 4.4 V,
SID.CSD#15A VREF_EXT reference for CSD 0.6 - V - 0.6 V DDA
DDA whichever is lower
and Comparator
IDAC1 (7 bits) block
SID.CSD#16 IDAC1IDD - - 1750 µA -
current
IDAC2 (7 bits) block
SID.CSD#17 IDAC2IDD - - 1750 µA -
current
Voltage range of 1.8 V ± 5% or 1.8 V
SID308 VCSD 1.71 - 5.5 V
operation to 5.5 V
Voltage
V - 0.6 V or 4.4 V,
SID308A VCOMPIDAC compliance range 0.6 - V - 0.6 V DDA
DDA whichever is lower
of IDAC
SID309 IDAC1DNL DNL -1 - 1 LSB -
SID310 IDAC1INL INL -3 - 3 LSB -
SID311 IDAC2DNL DNL -1 - 1.0 LSB -
SID312 IDAC2INL INL -3 - 3 LSB -
Capacitance range
Ratio of counts of
of 5pF to 200pF,
finger to noise.
SID313 SNR 5.0 - - Ratio 0.1 pF sensitivity.
Guaranteed by
All use cases.
characterization
V > 2V.
DDA
Maximum Source
SID314 IDAC7_SRC1 current of 7-bit 4.2 - 5.4 µA LSB = 37.5nA typ.
IDAC in low range
Maximum Source
current of 7-bit
SID314A IDAC7_SRC2 34 - 41 µA LSB = 300nA typ.
IDAC in medium
range
Note
7.For optimal CAPSENSE™ performance, Ports 0, 4, and 5 must be used for large DC loads.
Datasheet 41 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| VDD_RIPPLE | Max allowed ripple on power supply, DC to 10MHz | - | - | ±50 | mV |
| VDD_RIPPLE_1.8 | Max allowed ripple on power supply, DC to 10MHz | - | - | ±25 | mV |
| ICSD | Maximum block current | - | - | 4000 | µA |
| VREF | Voltage reference for CSD and Comparator | 0.6 | 1.2 | V - 0.6 DDA | V |
| VREF_EXT | External Voltage reference for CSD and Comparator | 0.6 | - | V - 0.6 DDA | V |
| IDAC1IDD | IDAC1 (7 bits) block current | - | - | 1750 | µA |
| IDAC2IDD | IDAC2 (7 bits) block current | - | - | 1750 | µA |
| VCSD | Voltage range of operation | 1.71 | - | 5.5 | V |
| VCOMPIDAC | Voltage compliance range of IDAC | 0.6 | - | V - 0.6 DDA | V |
| IDAC1DNL | DNL | -1 | - | 1 | LSB |
| IDAC1INL | INL | -3 | - | 3 | LSB |
| IDAC2DNL | DNL | -1 | - | 1.0 | LSB |
| IDAC2INL | INL | -3 | - | 3 | LSB |
| SNR | Ratio of counts of finger to noise. Guaranteed by characterization | 5.0 | - | - | Ratio |
| IDAC7_SRC1 | Maximum Source current of 7-bit IDAC in low range | 4.2 | - | 5.4 | µA |
| IDAC7_SRC2 | Maximum Source current of 7-bit IDAC in medium range | 34 | - | 41 | µA |
