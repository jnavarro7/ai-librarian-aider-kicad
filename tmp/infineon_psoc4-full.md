# Full PDF Extract

Source file: infineon_psoc4.pdf

## Page 1

### Raw Page Text

```text
CY8C41x5
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
General description
Infineon’ PSoC™ 4 is a scalable and reconfigurable platform architecture for a family of programmable embedded
system controllers with an Arm® Cortex®-M0+ CPU. It combines programmable and reconfigurable analog and
digital blocks with flexible automatic routing. PSoC™ 4100PS is a member of the PSoC™ 4 platform architecture.
It is a combination of a microcontroller with standard communication and timing peripherals, a capacitive
touch-sensing system (CAPSENSE™) with best-in-class performance, programmable general-purpose
continuous-time and switched-capacitor analog blocks, and programmable connectivity.
Features
• Programmable analog blocks
- Two dedicated analog-to-digital converters (ADC) including a 12-bit SAR ADC and a 10-bit single-slope ADC
- Four opamps, two low-power comparators, and a flexible 38-channel analog mux to create custom Analog
Front Ends (AFE)
- Two 13-bit voltage DACs
- Two 7-bit current DACs (IDACs) for general-purpose or capacitive sensing applications on any pin
• CAPSENSE™ capacitive sensing
- Infineon’s fourth-generation CAPSENSE™ Sigma-Delta (CSD) providing best-in-class signal-to-noise ratio
(SNR) and water tolerance
- Infineon-supplied software component makes capacitive sensing design easy
- Automatic hardware tuning (SmartSense™)
• Segment LCD drive
- LCD drive supported on all pins (common or segment)
- Operates in Deep-Sleep mode with four bits per pin memory
• Programmable digital peripherals
- Three independent serial communication blocks (SCBs) that are run-time configurable as I2C, SPI or UART
- Eight 16-bit timer/counter/pulse-width modulator (TCPWM) blocks with center-aligned, edge, and
pseudo-random modes
• 32-bit signal processing engine
- Arm® Cortex®-M0+ CPU up to 48 MHz
- Up to 32 KB of flash with read accelerator
- Up to 4 KB of SRAM
- Eight-channel descriptor-based DMA controller
• Low-power operation
- 1.71-V to 5.5-V operation
- Deep-Sleep mode with operational analog and 2.5-µA digital system current
- Watch crystal oscillator (WCO)
• Programmable GPIO pins
- Up to 38 GPIOs that can be used for analog, digital, CAPSENSE™, or LCD functions with programmable drive
modes, strength and slew rates
- Includes eight Smart I/Os to implement pin-level Boolean operations on input and output signals
- 48-pin QFN, 48-pin TQFP, 28-pin SSOP, and 45-ball WLCSP packages
Datasheet Please read the Important Notice and Warnings at the end of this document 002-22097 Rev. *F
www.infineon.com page 1 2023-11-16
```

## Page 2

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Features
• PSoC™ Creator Design Environment
- Integrated Design Environment (IDE) provides schematic-capture design entry and build (with automatic
routing of analog and digital signals) and concurrent firmware development with an Arm®-SWD debugger
- GUI-based configurable PSoC™ Components with fully engineered embedded initialization, calibration and
correction algorithms
- Application programming interfaces (API) for all fixed-function and programmable peripherals
• Industry-standard tool compatibility
- After schematic-capture, firmware development can be done with Arm-based industry-standard development
tools
Datasheet 2 002-22097 Rev. *F
2023-11-16
```

## Page 3

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
More information
More information
Infineon provides a wealth of data at www.infineon.com to help you to select the right PSoC™ device for your
design, and to help you to quickly and effectively integrate the device into your design. For a comprehensive list
of resources, see the knowledge base article KBA86521, How to Design with PSoC™ 3, PSoC™ 4, and
PSoC™ 5LP. Following is an abbreviated list for PSoC™ 4:
• Overview: MCU Portfolio
• Product selectors: PSoC™ 1, PSoC™ 3, PSoC™ 4, PSoC™5LP, PSoC™ 6
In addition, PSoC™ Creator includes a device selection tool.
• Application notes: Infineon offers a large number of PSoC™ application notes covering a broad range of topics,
from basic to advanced level. Recommended application notes for getting started with PSoC™ 4 are:
- AN79953: Getting Started With PSoC™ 4
- AN88619: PSoC™ 4 Hardware Design Considerations
- AN86439: Using PSoC™ 4 GPIO Pins
- AN57821: Mixed Signal Circuit Board Layout
- AN81623: Digital Design Best Practices
- AN73854: Introduction To Bootloaders
- AN89610: Arm® Cortex® Code Optimization
- AN85951: PSoC™ 4 and PSoC™ Analog Coprocessor CAPSENSE™ Design Guide
• Technical reference manual (TRM) is in two documents:
- Architecture TRM details each PSoC™ 4 functional block.
- Registers TRM describes each of the PSoC™ 4 registers.
• Development kits:
- CY8CKIT-147, PSoC™4100PS Prototyping Kit enables you to evaluate and develop with PSoC™ 4100PS devices
at a low cost.
The MiniProg3 device provides an interface for flash programming and debug.
• Software user guide:
- A step-by-step guide for using PSoC™ Creator. The software user guide shows you how the PSoC™ Creator
build process works in detail, how to use source control with PSoC™ Creator, and much more.
• Component datasheets:
- The flexibility of PSoC™ allows the creation of new peripherals (components) long after the device has gone
into production. Component datasheets provide all the information needed to select and use a particular
component, including a functional description, API documentation, example code, and AC/DC specifications.
• Online:
- In addition to print documentation, the Infineon Developer Community connect you with fellow PSoC™ users
and experts in PSoC™ from around the world, 24 hours a day, 7 days a week.
Datasheet 3 002-22097 Rev. *F
2023-11-16
```

## Page 4

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
PSoC™ Creator
PSoC™ Creator
PSoC™ Creator is a free Windows-based Integrated Design Environment (IDE). It enables concurrent hardware
and firmware design of PSoC™ 3, PSoC™ 4, and PSoC™ 5LP based systems. Create designs using classic, familiar
schematic capture supported by over 100 pre-verified, production-ready PSoC™ Components; see the list of
component datasheets. With PSoC™ Creator, you can:
1.Drag and drop component icons to build your hardware system design in the main design workspace
2.Codesign your application firmware with the PSoC™ hardware, using the PSoC™ Creator IDE C compiler
3.Configure components using the configuration tools
4.Explore the library of 100+ components
5.Review component datasheets
1
2
3
4
5
Figure 1 Multiple-sensor example project in PSoC™ Creator
Datasheet 4 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| 1 2 3 4 5 |
|---|

#### Table 2

|  | 5 |
|---|---|
| 3 |  |

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

## Page 6

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Table of contents
6.3 Analog peripherals................................................................................................................................................30
6.3.1 CTB Opamp........................................................................................................................................................30
6.3.2 PGA.....................................................................................................................................................................35
6.3.3 Voltage DAC........................................................................................................................................................36
6.3.4 Comparator........................................................................................................................................................37
6.3.5 Temperature Sensor..........................................................................................................................................38
6.3.6 SAR......................................................................................................................................................................39
6.3.7 CAPSENSE™ and IDAC........................................................................................................................................41
6.4 Digital Peripherals................................................................................................................................................45
6.4.1 Timer Counter Pulse-Width Modulator (TCPWM).............................................................................................45
6.4.2 I2C.......................................................................................................................................................................46
6.4.3 SPI.......................................................................................................................................................................47
6.4.4 UART...................................................................................................................................................................48
6.4.5 LCD......................................................................................................................................................................48
6.5 Memory..................................................................................................................................................................49
6.5.1 Flash...................................................................................................................................................................49
6.6 System resources..................................................................................................................................................50
6.6.1 Power-on Reset (POR).......................................................................................................................................50
6.6.2 SWD Interface.....................................................................................................................................................50
6.6.3 Internal Main Oscillator (IMO)...........................................................................................................................51
6.6.4 Internal low-speed oscillator (ILO)...................................................................................................................51
6.6.5 Watch Crystal Oscillator (WCO).........................................................................................................................52
6.6.6 External Clock....................................................................................................................................................52
6.6.7 Block...................................................................................................................................................................52
6.6.8 PRGIO Pass-through Time.................................................................................................................................52
7 Ordering information....................................................................................................................53
8 Packaging....................................................................................................................................55
8.1 Package diagrams.................................................................................................................................................56
9 Acronyms.....................................................................................................................................60
10 Document conventions................................................................................................................64
10.1 Units of measure.................................................................................................................................................64
Revision history..............................................................................................................................65
Datasheet 6 002-22097 Rev. *F
2023-11-16
```

## Page 7

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional overview
1 Functional overview
CPU Subsystem
PSoCTM 4100 PS
Architecture
32-bit
AHB-Lite
Peripherals
Active/Sleep
Deep Sleep
38x GPIO, LCD
Figure 2 Block diagram
PSoC™ 4100PS devices include extensive support for programming, testing, debugging, and tracing both
hardware and firmware.
The Arm® Serial-Wire Debug (SWD) interface supports all programming and debug features of the device.
Complete debug-on-chip functionality enables full-device debugging in the final system using the standard
production device. It does not require special interfaces, debugging pods, simulators, or emulators. Only the
standard programming connections are required to fully support debug.
The PSoC™ Creator IDE provides fully integrated programming and debug support for the PSoC™ 4100PS devices.
The SWD interface is fully compatible with industry-standard third-party tools. The PSoC™ 4100PS family
provides a level of security not possible with multi-chip application solutions or with microcontrollers. It has the
following advantages:
• Allows disabling of debug features
• Robust flash protection
• Allows customer-proprietary functionality to be implemented in on-chip programmable blocks
Datasheet 7 002-22097 Rev. *F
2023-11-16
)strop
x6(
OIPG
SSOI
PCLK Peripheral Interconnect (MMIO)
MWPCT
x8
™ESNESPAC
TRAU/IPS/C2I-BCS
x3
rotarapmoC
PL
x2
System Resources
Lite
Power
Sleep Control
WIC
POR REF
PWRSYS
Clock
Clock Control Programmable
WDT
Analog
IMO ILO
Reset SAR ADC VDAC
Reset Control
XRES (12-bit) (13-bit)
Test x1 x2
DFT Logic
DFT Analog
SARMUX CTB
x2
2x Opamp
Power Modes
I/O Subsystem
OCW
CPU Subsystem
SWD/TC SPCIF
Cortex®
FLASH SRAM ROM DataWire/
M0+
32 KB 4 KB 8 KB DMA
48 MHz
FAST MUL
Read Accelerator SRAM Controller ROM Controller Initiator/MMIO
NVIC, IRQMX
System Interconnect ( Multi Layer AHB)
High Speed I/O Matrix, Smart I/O
```

### Extracted Tables

#### Table 1

| PSoCTM 4100 PS Architecture |
|---|
| 32-bit AHB-Lite |

#### Table 2

| SWD/TC |
|---|
| Cortex® M0+ 48 MHz |
| FAST MUL |
| NVIC, IRQMX |

#### Table 3

| SPCIF |
|---|
| FLASH 32 KB |
| Read Accelerator |

#### Table 4

| SRAM 4 KB |
|---|
| SRAM Controller |

#### Table 5

| ROM 8 KB |
|---|
| ROM Controller |

#### Table 6

| DataWire/ DMA |
|---|
| Initiator/MMIO |

#### Table 7

| Sleep Control |  |
|---|---|
| WIC |  |
| POR | REF |
| PWRSYS |  |

#### Table 8

| Clock Control |  |
|---|---|
| WDT |  |
| IMO | ILO |

#### Table 9

| Programmable Analog |  |  |  |
|---|---|---|---|
| SAR ADC (12-bit) x1 |  |  | VDAC (13-bit) x2 |
| SARMUX | CTB x2 2x Opamp |  |  |

#### Table 10

| Reset Control |
|---|
| XRES |

#### Table 11

| DFT Logic |
|---|
| DFT Analog |

#### Table 12

|  |  | High Speed I/O Matrix, |  | Smart I/O |  |  |
|---|---|---|---|---|---|---|

#### Table 13

| Active/Sleep |
|---|
| Deep Sleep |

## Page 8

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional overview
The debug circuits are enabled by default and can be disabled in firmware. If they are not enabled, the only way
to re-enable them is to erase the entire device, clear flash protection, and reprogram the device with new
firmware that enables debugging. Thus firmware control of debugging cannot be over-ridden without erasing the
firmware thus providing security.
Additionally, all device interfaces can be permanently disabled (device security) for applications concerned
about phishing attacks due to a maliciously reprogrammed device or attempts to defeat security by starting and
interrupting flash programming sequences. All programming, debug, and test interfaces are disabled when
maximum device security is enabled. Therefore, PSoC™4100PS, with device security enabled, may not be
returned for failure analysis. This is a trade-off the PSoC™4100PS allows the customer to make.
Datasheet 8 002-22097 Rev. *F
2023-11-16
```

## Page 9

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2 Functional definition
2.1 CPU and memory subsystem
2.1.1 CPU
The Cortex®-M0+ CPU in the PSoC™ 4100PS is part of the 32-bit MCU subsystem, which is optimized for low-power
operation with extensive clock gating. Most instructions are 16 bits in length and the CPU executes a subset of
the Thumb-2 instruction set. It includes a nested vectored interrupt controller (NVIC) block with eight interrupt
inputs and also includes a Wakeup Interrupt Controller (WIC). The WIC can wake the processor from Deep Sleep
mode, allowing power to be switched off to the main processor when the chip is in Deep Sleep mode.
The CPU also includes a debug interface, the serial wire debug (SWD) interface, which is a two-wire form of JTAG.
The debug configuration used for PSoC™ 4100PS has four breakpoint (address) comparators and two watchpoint
(data) comparators.
2.1.2 DMA/DataWire
The DMA engine will be capable of doing independent data transfers anywhere within the memory map via a
user-programmable descriptor chain. The DataWire capability is used to effect single-element transfers from one
location in memory to another. There are eight DMA channels with a range of selectable trigger sources.
2.1.3 Flash
The PSoC™ 4100PS device has a flash module with a flash accelerator, tightly coupled to the CPU to improve
average access times from the flash block. The low-power flash block is designed to deliver two wait-state (WS)
access time at 48MHz. The flash accelerator delivers 85% of single-cycle SRAM access performance on average.
2.1.4 SRAM
Four KB of SRAM are provided with zero wait-state access at 48MHz.
2.1.5 SROM
Eight KB of SROM are provided that contain boot and configuration routines.
Datasheet 9 002-22097 Rev. *F
2023-11-16
```

## Page 10

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.2 System resources
2.2.1 Power system
The power system is described in detail in the section “Power” on page21. It provides an assurance that voltage
levels are as required for each respective mode and either delays mode entry (for example, on power-on reset
(POR) until voltage levels are as required for proper functionality, or generates resets (for example, on brown-out
detection). PSoC™ 4100PS operates with a single external supply over the range of either 1.8V ± 5% (externally
regulated) or 1.8V to 5.5V (internally regulated) and has three different power modes, transitions between which
are managed by the power system. PSoC™ 4100PS provides Active, Sleep, and Deep Sleep low-power modes.
All subsystems are operational in Active mode. The CPU subsystem (CPU, flash, and SRAM) is clock-gated off in
Sleep mode, while all peripherals and interrupts are active with instantaneous wake-up on a wake-up event. In
Deep Sleep mode, the high-speed clock and associated circuitry is switched off; wake-up from this mode takes
35 µs. The opamps can remain operational in Deep Sleep mode.
2.2.2 Clock system
The PSoC™ 4100PS clock system is responsible for providing clocks to all subsystems that require clocks and for
switching between different clock sources without glitching. In addition, the clock system ensures that there are
no metastable conditions.
The clock system for the PSoC™ 4100PS consists of the internal main oscillator (IMO), internal low-frequency
oscillator (ILO), a 32 kHz Watch Crystal Oscillator (WCO) and provision for an external clock. Clock dividers are
provided to generate clocks for peripherals on a fine-grained basis. Fractional dividers are also provided to
enable clocking of higher data rates for UARTs.
IMO
HFCLK
Divide By
2,4,8
External Clock
WDC0
WCO LFCLK 16-bits
WDC1
16-bits
ILO WDC2
32-bits
Watchdog Counters (WDC)
WDT
Watchdog Timer (WDT)
Prescaler
SYSCLK
HFCLK
Integer
Dividers 7X 16-bit
Fractional
Dividers 3X 16.5-bit, 1X 24.5 bit
Figure 3 PSoC™ 4100PS MCU Clocking Architecture
The HFCLK signal can be divided down to generate synchronous clocks for the analog and digital peripherals.
There are 11 clock dividers for PSoC™ 4100PS as shown in the diagram above. The 16-bit capability allows flexible
generation of fine-grained frequency values (there is one 24-bit divider for large divide ratios), and is fully
supported in PSoC™ Creator.
2.2.3 IMO clock source
The IMO is the primary source of internal clocking in PSoC™4100PS. It is trimmed during testing to achieve the
specified accuracy.The IMO default frequency is 24 MHz and it can be adjusted from 24 to 48 MHz in steps of
4 MHz. The IMO tolerance with Infineon-provided calibration settings is ±2%.
Datasheet 10 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Integer Dividers |
|---|
| Fractional Dividers |

## Page 11

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.2.4 ILO clock source
The ILO is a very low power, nominally 40-kHz oscillator, which is primarily used to generate clocks for the
watchdog timer (WDT) and peripheral operation in Deep Sleep mode. ILO-driven counters can be calibrated to
the IMO to improve accuracy. Infineon provides a software component, which does the calibration.
2.2.5 Watch crystal oscillator (WCO)
The PSoC™ 4100PS clock subsystem also implements a low-frequency (32-kHz watch crystal) oscillator that can
be used for Watchdog timing applications.
2.2.6 Watchdog timer
A watchdog timer is implemented in the clock block running from the ILO; this allows watchdog operation during
Deep Sleep and generates a watchdog reset if not serviced before the set timeout occurs. The watchdog reset is
recorded in a Reset Cause register, which is firmware readable.
2.2.7 Reset
PSoC™ 4100PS can be reset from a variety of sources including a software reset. Reset events are asynchronous
and guarantee reversion to a known state. The reset cause is recorded in a register, which is sticky through reset
and allows software to determine the cause of the reset. An XRES pin is reserved for external reset by asserting it
active low. The XRES pin has an internal pull-up resistor that is always enabled.
2.2.8 Voltage reference
The PSoC™ 4100PS reference system generates all internally required references. A 1.2-V voltage reference is
provided for the comparator. The IDACs are based on a ±5% reference.
Datasheet 11 002-22097 Rev. *F
2023-11-16
```

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

## Page 13

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.3.3 VDAC (13 bits)
The PSoC™ 4100PS has two 13-bit resolution Voltage DACs.
2.3.4 Low-power comparators (LPC)
PSoC™ 4100PS has a pair of low-power comparators, which can also operate in Deep Sleep modes. This allows
the analog system blocks to be disabled while retaining the ability to monitor external voltage levels during
low-power modes. The comparator outputs are normally synchronized to avoid metastability unless operating
in an asynchronous power mode where the system wake-up circuit is activated by a comparator switch event.
The LPC outputs can be routed to pins.
2.3.5 Current DACs
PSoC™ 4100PS has two IDACs, which can drive any of the pins on the chip. These IDACs have programmable
current ranges.
2.3.6 Analog multiplexed buses
PSoC™ 4100PS has two concentric independent buses that go around the periphery of the chip. These buses
(called amux buses) are connected to firmware-programmable analog switches that allow the chip’s internal
resources (IDACs, comparator) to connect to any pin on the I/O ports.
2.3.7 Temperature sensor
There is an on-chip temperature sensor which is calibrated during production to achieve ±1% typical (±5%
maximum) deviation from accuracy. The SAR ADC is used to measure the temperature.
2.4 Fixed Function Digital
2.4.1 Timer/Counter/PWM (TCPWM) block
The TCPWM block consists of a 16-bit counter with user-programmable period length. There is a capture register
to record the count value at the time of an event (which may be an I/O event), a period register that is used to
either stop or auto-reload the counter when its count is equal to the period register, and compare registers to
generate compare value signals that are used as PWM duty cycle outputs. The block also provides true and
complementary outputs with programmable offset between them to allow use as dead-band programmable
complementary PWM outputs. It also has a Kill input to force outputs to a predetermined state; for example, this
is used in motor drive systems when an over-current state is indicated and the PWM driving the FETs needs to be
shut off immediately with no time for software intervention. There are eight TCPWM blocks in PSoC™ 4100PS.
Datasheet 13 002-22097 Rev. *F
2023-11-16
```

## Page 14

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.4.2 Serial Communication block (SCB)
PSoC™ 4100PS has three serial communication blocks, which can be programmed to have SPI, I2C, or UART
functionality.
I2C Mode: The hardware I2C block implements a full multi-master and slave interface (it is capable of
multi-master arbitration). This block is capable of operating at speeds of up to 1Mbps (Fast Mode Plus) and has
flexible buffering options to reduce interrupt overhead and latency for the CPU. It also supports EZI2C that
creates a mailbox address range in the memory of PSoC™ 4100PS and effectively reduces I2C communication to
reading from and writing to an array in memory. In addition, the block supports an 8-deep FIFO for receive and
transmit which, by increasing the time given for the CPU to read data, greatly reduces the need for clock
stretching caused by the CPU not having read data on time.
The I2C peripheral is compatible with the I2C Standard-mode and Fast-mode devices as defined in the NXP
I2C-bus specification and user manual (UM10204). The I2C bus I/O is implemented with GPIO in open-drain
modes.
PSoC™ 4100PS is not completely compliant with the I2C spec in the following respect:
• GPIO cells are not overvoltage tolerant and, therefore, cannot be hot-swapped or powered up independently
of the rest of the I2C system.
UART Mode: This is a full-feature UART operating at up to 1Mbps. It supports automotive single-wire interface
(LIN), infrared interface (IrDA), and SmartCard (ISO7816) protocols, all of which are minor variants of the basic
UART protocol. In addition, it supports the 9-bit multiprocessor mode that allows addressing of peripherals
connected over common RX and TX lines. Common UART functions such as parity error, break detect, and frame
error are supported. An 8-deep FIFO allows much greater CPU service latencies to be tolerated.
SPI Mode: The SPI mode supports full Motorola SPI, TI SSP (adds a start pulse used to synchronize SPI Codecs),
and National Microwire (half-duplex form of SPI). The SPI block can use the FIFO.
2.5 GPIO
PSoC™ 4100PS has up to 38 GPIOs. The GPIO block implements the following:
• Eight drive modes:
- Analog input mode (input and output buffers disabled)
- Input only
- Weak pull-up with strong pull-down
- Strong pull-up with weak pull-down
- Open drain with strong pull-down
- Open drain with strong pull-up
- Strong pull-up with strong pull-down
- Weak pull-up with weak pull-down
• Input threshold select (CMOS or LVTTL)
• Individual control of input and output buffer enabling/disabling in addition to the drive strength modes
• Selectable slew rates for dV/dt related noise control to improve EMI.
The pins are organized in logical entities called ports, which are 8-bit in width (less for Ports 2 and 3). During
power-on and reset, the blocks are forced to the disable state so as not to crowbar any inputs and/or cause excess
turn-on current. A multiplexing network known as a high-speed I/O matrix is used to multiplex between various
signals that may connect to an I/O pin.
Data output and pin state registers store, respectively, the values to be driven on the pins and the states of the
pins themselves.
Every I/O pin can generate an interrupt if so enabled; each I/O port has an interrupt request (IRQ) and interrupt
service routine (ISR) vector associated with it (4 for PSoC™ 4100PS). The Smart I/O block is a fabric of switches
and LUTs that allows Boolean functions to be performed on signals being routed to the pins of a GPIO port. The
Smart I/O block can perform logical operations on input pins to the chip and on signals going out as outputs.
Datasheet 14 002-22097 Rev. *F
2023-11-16
```

## Page 15

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Functional definition
2.6 Special Function Peripherals
2.6.1 CAPSENSE™
CAPSENSE™ is supported in PSoC™ 4100PS through a CSD block that can be connected to any pins through an
analog mux bus via an analog switch. CAPSENSE™ function can thus be provided on any available pin or group
of pins in a system under software control. A PSoC™ Creator component is provided for the CAPSENSE™ block to
make it easy for the user.
Shield voltage can be driven on another mux bus to provide water-tolerance capability. Water tolerance is
provided by driving the shield electrode in phase with the sense electrode to keep the shield capacitance from
attenuating the sensed input. Proximity sensing can also be implemented.
The CAPSENSE™ block has two IDACs, which can be used for general purposes if CAPSENSE™ is not being used
(both IDACs are available in that case) or if CAPSENSE™ is used without water tolerance (one IDAC is available).
The CAPSENSE™ block also provides a 10-bit Slope ADC function, which can be used in conjunction with the
CAPSENSE™ function.
The CAPSENSE™ block is an advanced, low-noise, programmable block with programmable voltage references
and current source ranges for improved sensitivity and flexibility. It can also use an external reference voltage. It
has a full-wave CSD mode that alternates sensing to VDDA and ground to null out power-supply related noise
2.7 WLCSP Package Bootloader
The WLCSP package is supplied with an I2C bootloader installed in flash. The bootloader is compatible with
PSoC™ Creator bootloader project files.
Datasheet 15 002-22097 Rev. *F
2023-11-16
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

## Page 21

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Power
4 Power
The following power system diagram shows the set of power supply pins as implemented for the PSoC™4100PS.
The system has one regulator in Active mode for the digital circuitry. There is no analog regulator; the analog
circuits run directly from the V input.
DDA
Note that VDDD and VDDA must be shorted together on the PCB.
VDDA
VDDA
Digital Analog
Domain
Domain
VSSA
VDDD
VDDD VCCD
1.8 Volt
Reg
VSSD
Figure 5 Power supply connections
There are two distinct modes of operation. In Mode 1, the supply voltage range is 1.8 V to 5.5 V (unregulated
externally; internal regulator operational). In Mode 2, the supply range is 1.8 V ± 5% (externally regulated; 1.71 V
to 1.89 V, internal regulator bypassed).
4.1 Mode 1: 1.8V to 5.5V External Supply
In this mode, the PSoC™ 4100PS is powered by an external power supply that can be anywhere in the range of
1.8 V to 5.5 V. This range is also designed for battery-powered operation. For example, the chip can be powered
from a battery system that starts at 3.5 V and works down to 1.8 V. In this mode, the internal regulator of the
PSoC™ 4100PS supplies the internal logic and its output is connected to the V pin. The V pin must be
CCD CCD
bypassed to ground via an external capacitor (0.1 µF; X5R ceramic or better) and must not be connected to
anything else.
Datasheet 21 002-22097 Rev. *F
2023-11-16
```

## Page 22

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Power
4.2 Mode 2: 1.8V ± 5% External Supply
In this mode, the PSoC™ 4100PS is powered by an external power supply that must be within the range of 1.71 V
to 1.89 V; note that this range needs to include the power supply ripple too. In this mode, the V and V pins
DDD CCD
are shorted together and bypassed.
Bypass capacitors must be used from V and V to ground. The typical practice for systems in this frequency
DDD DDA
range is to use a capacitor in the 1-µF range, in parallel with a smaller capacitor (0.1 µF, for example). Note that
these are simply rules of thumb and that, for critical applications, the PCB layout, lead inductance, and the
bypass capacitor parasitic should be simulated to design and obtain optimal bypassing.
Figure6 shows an example of a bypass scheme.
Power supply bypass connections example
1.8 V to 5.5 V 1.8 V to 5.5 V
V DDD V DDA
1 µF 0.1 µF 1 µF 0.1 µF
V
CCD
0.1 µF PSoC CY8C4Axx
V
SS
Figure 6 External supply range from 1.8V to 5.5V with Internal Regulator Active
Datasheet 22 002-22097 Rev. *F
2023-11-16
```

## Page 23

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Development support
5 Development support
The PSoC™ 4100PS family has a rich set of documentation, development tools, and online resources to assist you
during your development process. Visit www.infineon.com/psoc4 to find out more.
5.1 Documentation
A suite of documentation supports the PSoC™ 4100PS family to ensure that you can find answers to your
questions quickly. This section contains a list of some of the key documents.
Software user guide: A step-by-step guide for using PSoC™ Creator. The software user guide shows you how the
PSoC™ Creator build process works in detail, how to use source control with PSoC™ Creator, and much more.
Component datasheets: The flexibility of PSoC™ allows the creation of new peripherals (components) long after
the device has gone into production. Component data sheets provide all of the information needed to select and
use a particular component, including a functional description, API documentation, example code, and AC/DC
specifications.
Application notes: PSoC™ application notes discuss a particular application of PSoC™ in depth; examples
include brushless DC motor control and on-chip filtering. Application notes often include example projects in
addition to the application note document.
Technical reference manual: The Technical Reference Manual (TRM) contains all the technical detail you need
to use a PSoC™ device, including a complete description of all PSoC™ registers. The TRM is available in the
Documentation section at www.infineon.com/psoc4.
5.2 Online
In addition to print documentation, the Infineon PSoC™ forums connect you with fellow PSoC™ users and experts
in PSoC™ from around the world, 24 hours a day, 7 days a week.
5.3 Tools
With industry standard cores, programming, and debugging interfaces, the PSoC™ 4100PS family is part of a
development tool ecosystem. Visit us at www.infineon.com/psoccreator for the latest information on the
revolutionary, easy to use PSoC™ Creator IDE, supported third party compilers, programmers, debuggers, and
development kits.
Datasheet 23 002-22097 Rev. *F
2023-11-16
```

## Page 24

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6 Electrical specifications
6.1 Absolute maximum ratings
Table 3 Absolute maximum ratings[1]
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
V , V ,
Digital or Analog supply DDD DDA
SID1 V -0.5 - 6 Absolute
DD_ABS relative to V
SS Max
V
Direct digital core voltage
SID2 V -0.5 - 1.95 -
CCD_ABS input relative to V
SS
SID3 V GPIO voltage -0.5 - V + 0.5 -
GPIO_ABS DD
SID4 I Maximum current per GPIO -25 - 25 -
GPIO_ABS
GPIO injection current, Current
mA
SID5 I Max for V > V , and -0.5 - 0.5 injected per
GPIO_injection IH DDD
Min for V < V pin
IL SS
Electrostatic discharge
BID44 ESD_HBM 2200 - - -
human body model
V
Electrostatic discharge
BID45 ESD_CDM 500 - - -
charged device model
BID46 LU Pin current for latch-up -140 - 140 mA -
Note
1.Usage above the absolute maximum conditions listed in Table3 may cause permanent damage to the device.
Exposure to Absolute Maximum conditions for extended periods of time may affect device reliability. The
Maximum Storage Temperature is 150°C in compliance with JEDEC Standard JESD22-A103, High
Temperature Storage Life. When used below Absolute Maximum conditions but above normal operating
conditions, the device may not operate to specification.
Datasheet 24 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V DD_ABS | Digital or Analog supply relative to V SS | -0.5 | - | 6 | V |
| V CCD_ABS | Direct digital core voltage input relative to V SS | -0.5 | - | 1.95 |  |
| V GPIO_ABS | GPIO voltage | -0.5 | - | V + 0.5 DD |  |
| I GPIO_ABS | Maximum current per GPIO | -25 | - | 25 | mA |
| I GPIO_injection | GPIO injection current, Max for V > V , and IH DDD Min for V < V IL SS | -0.5 | - | 0.5 |  |
| ESD_HBM | Electrostatic discharge human body model | 2200 | - | - | V |
| ESD_CDM | Electrostatic discharge charged device model | 500 | - | - |  |
| LU | Pin current for latch-up | -140 | - | 140 | mA |

## Page 25

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.2 Device Level Specifications
All specifications are valid for -40°C  T  105°C and T  125°C, except where noted. Specifications are valid for
A J
1.71V to 5.5V, except where noted.
Table 4 DC specifications
Typical values measured at V = 3.3V and 25°C.
DD
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
With
SID53 V Power supply input voltage 1.8 - 5.5 regulator
DD
enabled
V Internally
Power supply input voltage
SID255 V 1.71 - 1.89 unregulated
DD (V = V )
CCD DD supply
SID54 V V domain supply 1.71 - V -
DDIO DDIO DD
External regulator voltage X5R ceramic
SID55 C - 0.1 -
EFC bypass or better
µF
Power supply bypass X5R ceramic
SID56 C - 1 -
EXC capacitor or better
Active Mode, V = 1.8V to 5.5V. Typical values measured at VDD = 3.3 V and 25°C.
DD
Execute from flash;
SID10 I - 2 - -
DD5 CPU at 6 MHz
Execute from flash;
SID16 I - 5.6 - mA -
DD8 CPU at 24 MHz
Execute from flash;
SID19 I - 10.4 - -
DD11 CPU at 48 MHz
Sleep Mode, VDDD = 1.8V to 5.5 V (Regulator on)
I2C wakeup WDT, and
SID22 I - 1.1 - 6 MHz
DD17 Comparators on.
mA
I2C wakeup, WDT, and
SID25 I - 3.1 - 12 MHz
DD20 Comparators on.
Sleep Mode, V = 1.71V to 1.89 V (Regulator bypassed)
DDD
I2C wakeup, WDT, and
SID28 I - 1.1 - mA 6 MHz
DD23 Comparators on.
I2C wakeup, WDT, and
SID28A I - 3.1 - mA 12 MHz
DD23A Comparators on.
Deep Sleep Mode, V = 1.8V to 3.6V (Regulator on)
DD
SID31 I I2C wakeup and WDT on - 2.5 - µA -
DD26
Deep Sleep Mode, V = 3.6V to 5.5V (Regulator on)
DD
SID34 I I2C wakeup and WDT on - 2.5 - µA -
DD29
Deep Sleep Mode, V = 1.71V to 1.89V (Regulator bypassed)
DD
SID37 I I2C wakeup and WDT on - 2.5 - µA -
DD32
XRES Current
Supply current while XRES
SID307 I - 115 300 µA -
DD_XR asserted
Datasheet 25 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V DD | Power supply input voltage | 1.8 | - | 5.5 | V |
| V DD | Power supply input voltage (V = V ) CCD DD | 1.71 | - | 1.89 |  |
| V DDIO | V domain supply DDIO | 1.71 | - | V DD |  |
| C EFC | External regulator voltage bypass | - | 0.1 | - | µF |
| C EXC | Power supply bypass capacitor | - | 1 | - |  |

#### Table 2

| I DD5 | Execute from flash; CPU at 6 MHz | - | 2 | - | mA |
|---|---|---|---|---|---|
| I DD8 | Execute from flash; CPU at 24 MHz | - | 5.6 | - |  |
| I DD11 | Execute from flash; CPU at 48 MHz | - | 10.4 | - |  |

#### Table 3

| I DD17 | I2C wakeup WDT, and Comparators on. | - | 1.1 | - | mA |
|---|---|---|---|---|---|
| I DD20 | I2C wakeup, WDT, and Comparators on. | - | 3.1 | - |  |

#### Table 4

| I DD23 | I2C wakeup, WDT, and Comparators on. | - | 1.1 | - | mA |
|---|---|---|---|---|---|
| I DD23A | I2C wakeup, WDT, and Comparators on. | - | 3.1 | - | mA |

## Page 26

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 5 AC specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SID48 F CPU frequency DC - 48 MHz 1.71 V 5.5
CPU DD
Wakeup from Sleep
SID49[2] T - 0 - -
SLEEP mode
µs
Wakeup from Deep
SID50[2] T - 35 - -
DEEPSLEEP Sleep mode
Note
2.Guaranteed by characterization.
Datasheet 26 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F CPU | CPU frequency | DC | - | 48 | MHz |
| T SLEEP | Wakeup from Sleep mode | - | 0 | - | µs |
| T DEEPSLEEP | Wakeup from Deep Sleep mode | - | 35 | - |  |

## Page 27

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.2.1 GPIO
Table 6 GPIO DC specifications
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
SID57 V [3] Input voltage high threshold 0.7 ×V - - CMOS Input
IH DDD
SID58 V Input voltage low threshold - - 0.3 ×V CMOS Input
IL DDD
SID241 V [3] LVTTL input, V < 2.7V 0.7 ×V - - -
IH DDD DDD
SID242 V LVTTL input, V < 2.7V - - 0.3 ×V -
IL DDD DDD
SID243 V [3] LVTTL input, V  2.7V 2.0 - - -
IH DDD
SID244 V LVTTL input, V  2.7V - - 0.8 -
IL DDD
I = 4mA at
SID59 V Output voltage high level V - 0.6 - - OH
OH DDD V 3V V DDD
I = 1mA at
SID60 V Output voltage high level V - 0.5 - - OH
OH DDD 1.8V V
DDD
I = 4mA at
SID61 V Output voltage low level - - 0.6 OL
OL 1.8V V
DDD
I = 10mA
SID62 V Output voltage low level - - 0.6 OL
OL at 3V V
DDD
I = 3mA at
SID62A V Output voltage low level - - 0.4 OL
OL 3V V
DDD
SID63 R Pull-up resistor 3.5 5.6 8.5 -
PULLUP
kΩ
SID64 R Pull-down resistor 3.5 5.6 8.5 -
PULLDOWN
Input leakage current
SID65 I - 2 - nA -
IL (absolute value)
SID66 C Input capacitance - 3 7 pF -
IN
SID67[4] V Input hysteresis LVTTL 15 40 - V  2.7V
HYSTTL DDD
0.05 ×
SID68[4] V Input hysteresis CMOS - - mV V < 4.5V
HYSCMOS V DD
DDD
SID68A[4] V Input hysteresis CMOS 200 - - V > 4.5V
HYSCMOS5V5 DD
Current through protection
SID69[4] I - - 100 µA -
DIODE diode to V /V
DD SS
Maximum total source or
SID69A[4] I - - 85 mA -
TOT_GPIO sink chip current
Notes
3.V must not exceed V + 0.2V.
IH DDD
4.Guaranteed by characterization.
Datasheet 27 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Spec ID# | Parameter | Description | Min | Typ | Max | Unit | Details/ conditions |
|---|---|---|---|---|---|---|---|
| SID57 | V [3] IH | Input voltage high threshold | 0.7 ×V DDD | - | - | V | CMOS Input |
| SID58 | V IL | Input voltage low threshold | - | - | 0.3 ×V DDD |  | CMOS Input |
| SID241 | V [3] IH | LVTTL input, V < 2.7V DDD | 0.7 ×V DDD | - | - |  | - |
| SID242 | V IL | LVTTL input, V < 2.7V DDD | - | - | 0.3 ×V DDD |  | - |
| SID243 | V [3] IH | LVTTL input, V  2.7V DDD | 2.0 | - | - |  | - |
| SID244 | V IL | LVTTL input, V  2.7V DDD | - | - | 0.8 |  | - |
| SID59 | V OH | Output voltage high level | V - 0.6 DDD | - | - |  | I = 4mA at OH 3V V DDD |
| SID60 | V OH | Output voltage high level | V - 0.5 DDD | - | - |  | I = 1mA at OH 1.8V V DDD |
| SID61 | V OL | Output voltage low level | - | - | 0.6 |  | I = 4mA at OL 1.8V V DDD |
| SID62 | V OL | Output voltage low level | - | - | 0.6 |  | I = 10mA OL at 3V V DDD |
| SID62A | V OL | Output voltage low level | - | - | 0.4 |  | I = 3mA at OL 3V V DDD |
| SID63 | R PULLUP | Pull-up resistor | 3.5 | 5.6 | 8.5 | kΩ | - |
| SID64 | R PULLDOWN | Pull-down resistor | 3.5 | 5.6 | 8.5 |  | - |
| SID65 | I IL | Input leakage current (absolute value) | - | 2 | - | nA | - |
| SID66 | C IN | Input capacitance | - | 3 | 7 | pF | - |
| SID67[4] | V HYSTTL | Input hysteresis LVTTL | 15 | 40 | - | mV | V  2.7V DDD |
| SID68[4] | V HYSCMOS | Input hysteresis CMOS | 0.05 × V DDD | - | - |  | V < 4.5V DD |
| SID68A[4] | V HYSCMOS5V5 | Input hysteresis CMOS | 200 | - | - |  | V > 4.5V DD |
| SID69[4] | I DIODE | Current through protection diode to V /V DD SS | - | - | 100 | µA | - |
| SID69A[4] | I TOT_GPIO | Maximum total source or sink chip current | - | - | 85 | mA | - |

## Page 28

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 7 GPIO AC specifications
(Guaranteed by characterization)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Rise time in fast strong 3.3V V ,
SID70 T 2 - 12 DDD
RISEF mode Cload = 25pF
ns
Fall time in fast strong 3.3V V ,
SID71 T 2 - 12 DDD
FALLF mode Cload = 25pF
Rise time in slow 3.3V V ,
SID72 T 10 - 60 ns DDD
RISES strong mode Cload = 25pF
Fall time in slow strong 3.3V V ,
SID73 T 10 - 60 ns DDD
FALLS mode Cload = 25pF
GPIO F ; 90/10%,
OUT
SID74 F 3.3V  V 5.5V - - 16 25-pF load,
GPIOUT1 DDD
Fast strong mode 60/40 duty cycle
GPIO F ; 90/10%,
OUT
SID75 F 1.71V V 3.3V - - 16 25-pF load,
GPIOUT2 DDD
Fast strong mode 60/40 duty cycle
GPIO F ; 90/10%,
OUT
SID76 F 3.3V V 5.5V - - 7 MHz 25-pF load,
GPIOUT3 DDD
Slow strong mode 60/40 duty cycle
GPIO F ; 90/10%,
OUT
SID245 F 1.71V V 3.3V - - 3.5 25-pF load,
GPIOUT4 DDD
Slow strong mode. 60/40 duty cycle
GPIO input operating
SID246 F frequency; - - 48 90/10% V
GPIOIN IO
1.71V V 5.5V
DDD
Datasheet 28 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| T RISEF | Rise time in fast strong mode | 2 | - | 12 | ns |
| T FALLF | Fall time in fast strong mode | 2 | - | 12 |  |
| T RISES | Rise time in slow strong mode | 10 | - | 60 | ns |
| T FALLS | Fall time in slow strong mode | 10 | - | 60 | ns |
| F GPIOUT1 | GPIO F ; OUT 3.3V  V 5.5V DDD Fast strong mode | - | - | 16 | MHz |
| F GPIOUT2 | GPIO F ; OUT 1.71V V 3.3V DDD Fast strong mode | - | - | 16 |  |
| F GPIOUT3 | GPIO F ; OUT 3.3V V 5.5V DDD Slow strong mode | - | - | 7 |  |
| F GPIOUT4 | GPIO F ; OUT 1.71V V 3.3V DDD Slow strong mode. | - | - | 3.5 |  |
| F GPIOIN | GPIO input operating frequency; 1.71V V 5.5V DDD | - | - | 48 |  |

## Page 29

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.2.2 XRES
Table 8 XRES DC specifications
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
Input voltage high
SID77 V 0.7 × V - -
IH threshold DDD
V CMOS Input
Input voltage low
SID78 V - - 0.3  V
IL threshold DDD
SID79 R Pull-up resistor - 60 - kΩ -
PULLUP
SID80 C Input capacitance - 3 7 pF -
IN
Typical
hysteresis is
SID81[5] V Input voltage hysteresis - 0.05  V - mV
HYSXRES DD 200mV for
V > 4.5V
DD
Table 9 XRES AC specifications
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
SID83[5] T Reset pulse width 1 - - µs -
RESETWIDTH
Wake-up time from reset
BID194[5] T - - 2.5 ms -
RESETWAKE release
Note
5.Guaranteed by characterization.
Datasheet 29 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V IH | Input voltage high threshold | 0.7 × V DDD | - | - | V |
| V IL | Input voltage low threshold | - | - | 0.3  V DDD |  |
| R PULLUP | Pull-up resistor | - | 60 | - | kΩ |
| C IN | Input capacitance | - | 3 | 7 | pF |
| V HYSXRES | Input voltage hysteresis | - | 0.05  V DD | - | mV |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| T RESETWIDTH | Reset pulse width | 1 | - | - | µs |
| T RESETWAKE | Wake-up time from reset release | - | - | 2.5 | ms |

## Page 30

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3 Analog peripherals
6.3.1 CTB Opamp
Table 10 CTB Opamp specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
I Opamp block current, No load
DD
SID269 I power = hi - 1100 2070 -
DD_HI
SID270 I power = med - 550 950 µA -
DD_MED
SID271 I power = lo - 150 350 -
DD_LOW
Load = 20pF,
G 0.1mA,
BW
V = 2.7V
DDA
Input and output are
SID272 G power = hi 6 - -
BW_HI 0.2V to V - 0.2V
DDA
Input and output are
SID273 G power = med 3 - - MHz
BW_MED 0.2V to V - 0.2V
DDA
Input and output are
SID274 G power = lo - 1 -
BW_LO 0.2V to V - 0.2V
DDA
V = 2.7V,
I DDA
OUT_MAX 500mV from rail
Output is 0.5V to
SID275 I power = hi 10 - -
OUT_MAX_HI V - 0.5V
DDA
Output is 0.5V to
SID276 I power = mid 10 - - mA
OUT_MAX_MID V - 0.5V
DDA
Output is 0.5V to
SID277 I power = lo - 5 -
OUT_MAX_LO V - 0.5V
DDA
V = 1.71V,
I DDA
OUT 500 mV from rail
Output is 0.5V to
SID278 I power = hi 4 - -
OUT_MAX_HI V - 0.5V
DDA
Output is 0.5V to
SID279 I OUT_MAX_MID power = mid 4 - - mA V - 0.5V
DDA
Output is 0.5V to
SID280 I power = lo - 2 -
OUT_MAX_LO V - 0.5V
DDA
I Opamp block current Internal Load
DD_Int
SID269_I I power = hi - 1500 2300 -
DD_HI_Int
µA
SID270_I I power = med - 700 1200 -
DD_MED_Int
G V = 2.7V
BW DDA
Output is 0.25V to
SID272_I G power = hi 8 - - MHz
BW_HI_Int V - 0.25V
DDA
Datasheet 30 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I DD |  |  |  |  |  |
| I DD_HI | power = hi | - | 1100 | 2070 | µA |
| I DD_MED | power = med | - | 550 | 950 |  |
| I DD_LOW | power = lo | - | 150 | 350 |  |
| G BW |  |  |  |  |  |
| G BW_HI | power = hi | 6 | - | - | MHz |
| G BW_MED | power = med | 3 | - | - |  |
| G BW_LO | power = lo | - | 1 | - |  |
| I OUT_MAX |  |  |  |  |  |
| I OUT_MAX_HI | power = hi | 10 | - | - | mA |
| I OUT_MAX_MID | power = mid | 10 | - | - |  |
| I OUT_MAX_LO | power = lo | - | 5 | - |  |
| I OUT |  |  |  |  |  |
| I OUT_MAX_HI | power = hi | 4 | - | - | mA |
| I OUT_MAX_MID | power = mid | 4 | - | - |  |
| I OUT_MAX_LO | power = lo | - | 2 | - |  |
| I DD_Int |  |  |  |  |  |
| I DD_HI_Int | power = hi | - | 1500 | 2300 | µA |
| I DD_MED_Int | power = med | - | 700 | 1200 |  |
| G BW |  |  |  |  |  |
| G BW_HI_Int | power = hi | 8 | - | - | MHz |

## Page 31

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 10 CTB Opamp specifications (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
General opamp specs for both internal and external modes
Charge-pump on,
SID281 V -0.05 - V - 0.2 -
IN DDA
V = 2.7V
DDA
V
Charge-pump on,
SID282 V -0.05 - V - 0.2 -
CM DDA
V = 2.7V
DDA
power = hi,
SID283 V 0.5 - V - 0.5 V = 2.7V
OUT_1 DDA DD
Iload = 10mA
power = hi,
SID284 V 0.2 - V - 0.2 V = 2.7V
OUT_2 DDA DDA
Iload = 1mA
V
power = med,
SID285 V 0.2 - V - 0.2 V = 2.7V
OUT_3 DDA DDA
Iload = 1mA
power = lo,
SID286 V 0.2 - V - 0.2 V = 2.7V
OUT_4 DDA DDA
Iload = 0.1mA
Offset voltage, High mode, input 0V
SID288 V -1.0 0.5 1.0
OS_TR
trimmed to V - 0.2V
DDA
Offset voltage, Medium mode, input
SID288A V - 1 - mV
OS_TR
trimmed 0V to V - 0.2V
DDA
Offset voltage, Low mode, input 0V to
SID288B V - 2 -
OS_TR
trimmed V - 0.2V
DDA
Offset voltage drift,
SID290 V -10 3 10 µV/C High mode
OS_DR_TR
trimmed
Offset voltage drift,
SID290A V - 10 - Medium mode
OS_DR_TR
trimmed
µV/C
Offset voltage drift,
SID290B V - 10 - Low mode
OS_DR_TR
trimmed
Input is 0V to
V - 0.2V, Output is
DDA
SID291 CMRR DC 70 80 -
0.2V to V - 0.2V,
DDA
V ≥ 2.7V
DDA
Input is 0V to
V - 0.2V, Output is
DDA
SID291A CMRR2 DC 60 70 - dB
0.2V to V - 0.2V.
DDA
1.71V  V < 2.7V
DDA
V = 3.6V,
DDD
At 1kHz, high-power mode,
SID292 PSRR 70 85 -
10-mV ripple input is 0.2V to
V - 0.2V
DDA
Datasheet 31 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V IN | Charge-pump on, V = 2.7V DDA | -0.05 | - | V - 0.2 DDA | V |
| V CM | Charge-pump on, V = 2.7V DDA | -0.05 | - | V - 0.2 DDA |  |
| V OUT_1 | power = hi, Iload = 10mA | 0.5 | - | V - 0.5 DDA | V |
| V OUT_2 | power = hi, Iload = 1mA | 0.2 | - | V - 0.2 DDA |  |
| V OUT_3 | power = med, Iload = 1mA | 0.2 | - | V - 0.2 DDA |  |
| V OUT_4 | power = lo, Iload = 0.1mA | 0.2 | - | V - 0.2 DDA |  |
| V OS_TR | Offset voltage, trimmed | -1.0 | 0.5 | 1.0 | mV |
| V OS_TR | Offset voltage, trimmed | - | 1 | - |  |
| V OS_TR | Offset voltage, trimmed | - | 2 | - |  |
| V OS_DR_TR | Offset voltage drift, trimmed | -10 | 3 | 10 | µV/C |
| V OS_DR_TR | Offset voltage drift, trimmed | - | 10 | - | µV/C |
| V OS_DR_TR | Offset voltage drift, trimmed | - | 10 | - |  |
| CMRR | DC | 70 | 80 | - | dB |
| CMRR2 | DC | 60 | 70 | - |  |
| PSRR | At 1kHz, 10-mV ripple | 70 | 85 | - |  |

## Page 32

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 10 CTB Opamp specifications (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Noise
Input-referred,
Input and output are
SID294 VN2 1kHz, - 72 -
at 0.2V to V - 0.2V
DDA
power = Hi
Input-referred,
nV/ Input and output are
SID295 VN3 10kHz, - 28 -
rtHz at 0.2V to V - 0.2V
DDA
power = Hi
Input-referred,
Input and output are
SID296 VN4 100kHz, - 15 -
at 0.2V to V - 0.2V
DDA
power = Hi
Stable up to max.
SID297 C load. Performance - - 125 pF -
LOAD
specs at 50pF.
C = 50pF,
LOAD
SID298 SLEW_RATE Power = High, 6 - - V/µs -
V = 2.7V
DDA
From disable to
SID299 T_OP_WAKE enable, no external - - 25 µs -
RC dominating
SID299A OL_GAIN Open Loop Gain - 90 - dB -
COMP_
Comparator mode; 50-mV drive, T = T (approx)
rise fall
MODE
Response time; Input is 0.2V to
SID300 T - 150 175
PD1 power = hi V - 0.2V
DDA
Response time; Input is 0.2V to
SID301 T - 500 - ns
PD2 power = med V - 0.2V
DDA
Response time; Input is 0.2V to
SID302 T - 2500 -
PD3 power = lo V - 0.2V
DDA
SID303 V Hysteresis - 10 - mV -
HYST_OP
Wake-up time from
SID304 WUP_CTB - - 25 µs -
Enabled to Usable
Datasheet 32 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| VN2 | Input-referred, 1kHz, power = Hi | - | 72 | - | nV/ rtHz |
|---|---|---|---|---|---|
| VN3 | Input-referred, 10kHz, power = Hi | - | 28 | - |  |
| VN4 | Input-referred, 100kHz, power = Hi | - | 15 | - |  |
| C LOAD | Stable up to max. load. Performance specs at 50pF. | - | - | 125 | pF |
| SLEW_RATE | C = 50pF, LOAD Power = High, V = 2.7V DDA | 6 | - | - | V/µs |
| T_OP_WAKE | From disable to enable, no external RC dominating | - | - | 25 | µs |
| OL_GAIN | Open Loop Gain | - | 90 | - | dB |
| COMP_ MODE |  |  |  |  |  |
| T PD1 | Response time; power = hi | - | 150 | 175 | ns |
| T PD2 | Response time; power = med | - | 500 | - |  |
| T PD3 | Response time; power = lo | - | 2500 | - |  |
| V HYST_OP | Hysteresis | - | 10 | - | mV |
| WUP_CTB | Wake-up time from Enabled to Usable | - | - | 25 | µs |

## Page 33

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 10 CTB Opamp specifications (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Opamp
Deep Sleep Mode 2 is lowest current range. Mode 1 has higher GBW.
Mode
Mode 1,
SID_DS_1 I - 1400 - -
DD_HI_M1
High current
Mode 1,
SID_DS_2 I - 700 - µA -
DD_MED_M1
Medium current
Mode 1,
SID_DS_3 I - 200 - -
DD_LOW_M1
Low current
Mode 2,
SID_DS_4 I - 120 - -
DD_HI_M2
High current
Mode 2,
SID_DS_5 I - 60 - µA -
DD_MED_M2
Medium current
Mode 2,
SID_DS_6 I - 15 - -
DD_LOW_M2
Low current
Mode 1, 20-pF load, no DC load
SID_DS_7 G - 4 -
BW_HI_M1 High current 0.2V to V - 0.2 V
DDA
Mode 1, 20-pF load, no DC load
SID_DS_8 G - 2 -
BW_MED_M1 Medium current 0.2V to V - 0.2V
DDA
Mode 1, 20-pF load, no DC load
SID_DS_9 G - 0.5 -
BW_LOW_M1 Low current 0.2V to V - 0.2V
DDA
MHz
Mode 2, 20-pF load, no DC load
SID_DS_10 G - 0.5 -
BW_HI_M2 High current 0.2V to V - 0.2V
DDA
Mode 2, 20-pF load, no DC load
SID_DS_11 G - 0.2 -
BW_MED_M2 Medium current 0.2V to V - 0.2V
DDA
Mode 2, 20-pF load, no DC load
SID_DS_12 G - 0.1 -
BW_Low_M2 Low current 0.2V to V - 0.2V
DDA
Mode 1, With trim 25°C,
SID_DS_13 V - 5 -
OS_HI_M1 High current 0.2V to V - 1.5V
DDA
Mode 1, With trim 25°C,
SID_DS_14 V - 5 -
OS_MED_M1 Medium current 0.2V to V - 1.5V
DDA
Mode 1, With trim 25°C,
SID_DS_15 V - 5 -
OS_LOW_M1 Low current 0.2V to V - 1.5V
DDA
mV
Mode 2, With trim 25°C,
SID_DS_16 V - 5 -
OS_HI_M2 High current 0.2 V to V - 1.5V
DDA
Mode 2, With trim 25°C,
SID_DS_17 V - 5 -
OS_MED_M2 Medium current 0.2V to V - 1.5V
DDA
Mode 2, With trim 25°C,
SID_DS_18 V - 5 -
OS_LOW_M2 Low current 0.2V to V - 1.5V
DDA
Datasheet 33 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| Opamp Deep Sleep Mode |  |  |  |  |  |
| I DD_HI_M1 | Mode 1, High current | - | 1400 | - | µA |
| I DD_MED_M1 | Mode 1, Medium current | - | 700 | - |  |
| I DD_LOW_M1 | Mode 1, Low current | - | 200 | - |  |
| I DD_HI_M2 | Mode 2, High current | - | 120 | - | µA |
| I DD_MED_M2 | Mode 2, Medium current | - | 60 | - |  |
| I DD_LOW_M2 | Mode 2, Low current | - | 15 | - |  |
| G BW_HI_M1 | Mode 1, High current | - | 4 | - | MHz |
| G BW_MED_M1 | Mode 1, Medium current | - | 2 | - |  |
| G BW_LOW_M1 | Mode 1, Low current | - | 0.5 | - |  |
| G BW_HI_M2 | Mode 2, High current | - | 0.5 | - |  |
| G BW_MED_M2 | Mode 2, Medium current | - | 0.2 | - |  |
| G BW_Low_M2 | Mode 2, Low current | - | 0.1 | - |  |
| V OS_HI_M1 | Mode 1, High current | - | 5 | - | mV |
| V OS_MED_M1 | Mode 1, Medium current | - | 5 | - |  |
| V OS_LOW_M1 | Mode 1, Low current | - | 5 | - |  |
| V OS_HI_M2 | Mode 2, High current | - | 5 | - |  |
| V OS_MED_M2 | Mode 2, Medium current | - | 5 | - |  |
| V OS_LOW_M2 | Mode 2, Low current | - | 5 | - |  |

## Page 34

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 10 CTB Opamp specifications (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Mode 1, Output is
SID_DS_19 I - 10 -
OUT_HI_M1 High current 0.5V to V - 0.5V
DDA
Mode 1, Output is
SID_DS_20 I - 10 -
OUT_MED_M1 Medium current 0.5V to V - 0.5V
DDA
Mode 1, Output is
SID_DS_21 I - 4 -
OUT_LOW_M1 Low current 0.5V to V - 0.5V
mA DDA
Mode 2,
SID_DS_22 I - 1 - -
OUT_HI_M2
High current
Mode 2,
SID_DS_23 I - 1 - -
OU_MED_M2
Medium current
Mode 2,
SID_DS_24 I - 0.5 - -
OU_LOW_M2
Low current
Datasheet 34 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I OUT_HI_M1 | Mode 1, High current | - | 10 | - | mA |
| I OUT_MED_M1 | Mode 1, Medium current | - | 10 | - |  |
| I OUT_LOW_M1 | Mode 1, Low current | - | 4 | - |  |
| I OUT_HI_M2 | Mode 2, High current | - | 1 | - |  |
| I OU_MED_M2 | Mode 2, Medium current | - | 1 | - |  |
| I OU_LOW_M2 | Mode 2, Low current | - | 0.5 | - |  |

## Page 35

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.2 PGA
Table 11 PGA specifications
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
PGA Gain Gain Values are 2, 4, 16, and
- 2 - 32 - -
Values 32.
Gain Error for Low range;
- 1 - % -
Gain = 2
Gain Error for Medium
SID_PGA_1 PGA_ERR_1 range; - - 1.5 % -
Gain = 2
Gain Error for High range;
- - 1.5 % -
Gain = 2
Gain Error for Low range;
- 1 - % -
Gain = 4
Gain Error for Medium
SID_PGA_2 PGA_ERR_2 range; - - 1.5 % -
Gain = 4
Gain Error for High range;
- - 1.5 % -
Gain = 4
Gain Error for Low range;
- 3 - % -
Gain = 16
Gain Error for Medium
SID_PGA_3 PGA_ERR_3 range; - 3 - % -
Gain = 16
Gain Error for High range;
- 3 - % -
Gain = 16
Gain Error for Low range;
- 5 - % -
Gain = 32
Gain Error for Medium
SID_PGA_4 PGA_ERR_4 range; - 5 - % -
Gain = 32
Gain Error for High range;
- 5 - % -
Gain = 32
Datasheet 35 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| - | Gain Values are 2, 4, 16, and 32. | 2 | - | 32 | - |
| PGA_ERR_1 | Gain Error for Low range; Gain = 2 | - | 1 | - | % |
|  | Gain Error for Medium range; Gain = 2 | - | - | 1.5 | % |
|  | Gain Error for High range; Gain = 2 | - | - | 1.5 | % |
| PGA_ERR_2 | Gain Error for Low range; Gain = 4 | - | 1 | - | % |
|  | Gain Error for Medium range; Gain = 4 | - | - | 1.5 | % |
|  | Gain Error for High range; Gain = 4 | - | - | 1.5 | % |
| PGA_ERR_3 | Gain Error for Low range; Gain = 16 | - | 3 | - | % |
|  | Gain Error for Medium range; Gain = 16 | - | 3 | - | % |
|  | Gain Error for High range; Gain = 16 | - | 3 | - | % |
| PGA_ERR_4 | Gain Error for Low range; Gain = 32 | - | 5 | - | % |
|  | Gain Error for Medium range; Gain = 32 | - | 5 | - | % |
|  | Gain Error for High range; Gain = 32 | - | 5 | - | % |

## Page 36

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.3 Voltage DAC
Table 12 Voltage DAC specifications
(VDAC specs are valid from -20°C to 85°C)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
13-bit DAC
Integral non
SID_DAC_1 INL_VDAC1 -6 - 5 -
linearity (INL)
LSB
Differential non
SID_DAC_2 DNL_VDAC1 -1 - 4 -
linearity (DNL)
Valid output range
is 200 LSBs from
VOUT_ Output voltage rails. Full settling
SID_DAC_3 0.2 - V - 0.2 V
VDAC1 range DDA bandwidth to
within 200mV of
rail.
Zero scale error
Zero scale is at
SID_DAC_4 ZSE_VDAC1 (output with all - 20 - mV
analog ground.
zeroes input)
Full scale error less V DDA ≥ 2.7 V,
SID_DAC_5 GE_VDAC1 - 0.3 2 %
offset VREF = V /2
DDA
SID_DAC_6 IDD_VDAC1 Block current - 1.8 - mA -
PSRR_ Power supply
SID_DAC_7 - 50 - dB 2.7V < V  5.5V
VDAC1 rejection ratio DDA
Wake-up time from
SID_DAC_8 WUP_VDAC1 - - 32 µs 2.7 V < V 5.5 V
Enabled to Usable DDA
Wake-up time from
SID_DAC_8A WUP_VDAC2 - - 72 µs V  2.7 V
Enabled to Usable DDA
Settling time for 500 ksps operation,
SID_DAC_9 TS_VDAC1 - - 2 µs
DAC V ≥ 2.7 V
DDA
Settling time for 100 ksps operation,
SID_DAC_9A TS_VDAC2 - - 10 µs
DAC V  2.7 V
DDA
Note
6.Guaranteed by characterization.
Datasheet 36 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |  |
|---|---|---|---|---|---|---|
| INL_VDAC1 | Integral non linearity (INL) | -6 | - | 5 | LSB |  |
| DNL_VDAC1 | Differential non linearity (DNL) | -1 | - | 4 |  |  |
| VOUT_ VDAC1 | Output voltage range | 0.2 | - | V - 0.2 DDA | V |  |
| ZSE_VDAC1 | Zero scale error (output with all zeroes input) | - | 20 | - | mV |  |
| GE_VDAC1 | Full scale error less offset | - | 0.3 | 2 | % | V ≥ 2.7 V, DDA VREF = V /2 DDA |
| IDD_VDAC1 | Block current | - | 1.8 | - | mA |  |
| PSRR_ VDAC1 | Power supply rejection ratio | - | 50 | - | dB | 2.7V < V  5.5V DDA |
| WUP_VDAC1 | Wake-up time from Enabled to Usable | - | - | 32 | µs | 2.7 V < V 5.5 V DDA |
| WUP_VDAC2 | Wake-up time from Enabled to Usable | - | - | 72 | µs | V  2.7 V DDA |
| TS_VDAC1 | Settling time for DAC | - | - | 2 | µs | 500 ksps operation, V ≥ 2.7 V DDA |
| TS_VDAC2 | Settling time for DAC | - | - | 10 | µs | 100 ksps operation, V  2.7 V DDA |

## Page 37

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.4 Comparator
Table 13 Comparator DC specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Input offset voltage,
SID84 V - - ±10 -
OFFSET1 Factory trim
Input offset voltage,
SID85 V - - ±4 mV -
OFFSET2 Custom trim
Hysteresis when
SID86 V - 10 35 -
HYST enabled
Input common mode
SID87 V voltage in normal 0 - V - 0.1 Modes 1 and 2
ICM1 DDD
mode
Input common mode
SID247 V voltage in low power 0 - V -
ICM2 DDD V
mode
V ≥ 2.2V for
Input common mode DDD
Temp < 0°C,
SID247A V voltage in ultra low 0 - V - 1.15
ICM3 DDD V ≥ 1.8V for
power mode DDD
Temp > 0°C
Common mode
SID88 C 50 - - V ≥ 2.7 V
MRR rejection ratio DDD
dB
Common mode
SID88A C 42 - - V ≤ 2.7 V
MRR rejection ratio DDD
Block current, normal
SID89 I - - 400 -
CMP1 mode
Block current, low
SID248 I - - 100 -
CMP2 power mode
µA
V ≥ 2.2V for
DDD
Block current in ultra Temp < 0°C,
SID259 I - - 28
CMP3 low-power mode V ≥ 1.8V for
DDD
Temp > 0°C
DC Input impedance of
SID90 Z 35 - - MΩ -
CMP comparator
Table 14 Comparator AC specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Response time,
SID91 TRESP1 normal mode, - 38 110 All V
DD
50 mV overdrive
ns
Response time, low
SID258 TRESP2 power mode, - 70 200 -
50 mV overdrive
V ≥ 2.2V for
Response time, DDD
Temp < 0°C,
SID92 TRESP3 ultra-low power mode, - 2.3 15 µs
V ≥ 1.8V for
200 mV overdrive DDD
Temp > 0°C
Datasheet 37 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |  |
|---|---|---|---|---|---|---|
| V OFFSET1 | Input offset voltage, Factory trim | - | - | ±10 | mV | - |
| V OFFSET2 | Input offset voltage, Custom trim | - | - | ±4 |  | - |
| V HYST | Hysteresis when enabled | - | 10 | 35 |  | - |
| V ICM1 | Input common mode voltage in normal mode | 0 | - | V - 0.1 DDD | V |  |
| V ICM2 | Input common mode voltage in low power mode | 0 | - | V DDD |  | - |
| V ICM3 | Input common mode voltage in ultra low power mode | 0 | - | V - 1.15 DDD |  | V ≥ 2.2V for DDD Temp < 0°C, V ≥ 1.8V for DDD Temp > 0°C |
| C MRR | Common mode rejection ratio | 50 | - | - | dB |  |
| C MRR | Common mode rejection ratio | 42 | - | - |  |  |
| I CMP1 | Block current, normal mode | - | - | 400 | µA | - |
| I CMP2 | Block current, low power mode | - | - | 100 |  | - |
| I CMP3 | Block current in ultra low-power mode | - | - | 28 |  | V ≥ 2.2V for DDD Temp < 0°C, V ≥ 1.8V for DDD Temp > 0°C |
| Z CMP | DC Input impedance of comparator | 35 | - | - | MΩ | - |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |  |
|---|---|---|---|---|---|---|
| TRESP1 | Response time, normal mode, 50 mV overdrive | - | 38 | 110 | ns |  |
| TRESP2 | Response time, low power mode, 50 mV overdrive | - | 70 | 200 |  |  |
| TRESP3 | Response time, ultra-low power mode, 200 mV overdrive | - | 2.3 | 15 | µs | V ≥ 2.2V for DDD Temp < 0°C, V ≥ 1.8V for DDD Temp > 0°C |

## Page 38

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.5 Temperature Sensor
Table 15 Temperature Sensor specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Temperature sensor
SID93 TSENSACC -5 ±1 5 °C -40°C to +85°C
accuracy
Datasheet 38 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Spec ID# | Parameter | Description | Min | Typ | Max | Unit | Details/conditions |
|---|---|---|---|---|---|---|---|
|  | TSENSACC | Temperature sensor accuracy | -5 | ±1 | 5 | °C |  |

## Page 39

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.3.6 SAR
Table 16 SAR specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SAR ADC DC specifications
SID94 A_RES Resolution - - 12 bits -
Number of channels -
SID95 A_CHNLS_S - - 8 8 full speed.
single ended
Number of channels -
SID96 A-CHNKS_D - - 4 -
differential
SID97 A-MONO Monotonicity - - - Yes.
With external
SID98 A_GAINERR Gain error - - ±0.1 %
reference.
Measured with 1-V
SID99 A_OFFSET Input offset voltage - - 2 mV
reference.
SID100 A_ISAR Current consumption - - 1 mA -
Input voltage range -
SID101 A_VINS V - V V -
single ended SS DDA
Input voltage range -
SID102 A_VIND V - V V -
differential SS DDA
SID103 A_INRES Input resistance - - 2.2 KΩ -
SID104 A_INCAP Input capacitance - - 10 pF -
Trimmed internal
SID260 VREFSAR - - TBD V -
reference to SAR
SAR ADC AC specifications
Power supply rejection
SID106 A_PSRR 70 - - dB -
ratio
Common mode
SID107 A_CMRR 66 - - dB Measured at 1V.
rejection ratio
SID108 A_SAMP Sample rate - - 1 Msps -
Signal-to-noise and
SID109 A_SNR distortion ratio 65 - - dB F = 10 kHz
IN
(SINAD)
Input bandwidth
SID110 A_BW - - A_samp/2 kHz -
without aliasing
Integral non linearity.
SID111 A_INL V = 1.71 V to 5.5 V, -1.7 - 2 LSB V = 1 to V
DD REF DD
1Msps
Integral non linearity.
SID111A A_INL V = 1.71 V to 3.6 V, -1.5 - 1.7 LSB V = 1.71 to V
DDD REF DD
1Msps
Integral non linearity.
SID111B A_INL V = 1.71 V to 5.5 V, -1.5 - 1.7 LSB V = 1 to V
DD REF DD
500ksps
Datasheet 39 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| A_RES | Resolution | - | - | 12 | bits |
|---|---|---|---|---|---|
| A_CHNLS_S | Number of channels - single ended | - | - | 8 |  |
| A-CHNKS_D | Number of channels - differential | - | - | 4 |  |
| A-MONO | Monotonicity | - | - | - |  |
| A_GAINERR | Gain error | - | - | ±0.1 | % |
| A_OFFSET | Input offset voltage | - | - | 2 | mV |
| A_ISAR | Current consumption | - | - | 1 | mA |
| A_VINS | Input voltage range - single ended | V SS | - | V DDA | V |
| A_VIND | Input voltage range - differential | V SS | - | V DDA | V |
| A_INRES | Input resistance | - | - | 2.2 | KΩ |
| A_INCAP | Input capacitance | - | - | 10 | pF |
| VREFSAR | Trimmed internal reference to SAR | - | - | TBD | V |

#### Table 2

| A_PSRR | Power supply rejection ratio | 70 | - | - | dB |
|---|---|---|---|---|---|
| A_CMRR | Common mode rejection ratio | 66 | - | - | dB |
| A_SAMP | Sample rate | - | - | 1 | Msps |
| A_SNR | Signal-to-noise and distortion ratio (SINAD) | 65 | - | - | dB |
| A_BW | Input bandwidth without aliasing | - | - | A_samp/2 | kHz |
| A_INL | Integral non linearity. V = 1.71 V to 5.5 V, DD 1Msps | -1.7 | - | 2 | LSB |
| A_INL | Integral non linearity. V = 1.71 V to 3.6 V, DDD 1Msps | -1.5 | - | 1.7 | LSB |
| A_INL | Integral non linearity. V = 1.71 V to 5.5 V, DD 500ksps | -1.5 | - | 1.7 | LSB |

## Page 40

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 16 SAR specifications (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Differential non
linearity.
SID112 A_DNL -1 - 2.2 LSB V = 1 to V
V = 1.71 V to 5.5 V, REF DD
DD
1Msps
Differential non
linearity.
SID112A A_DNL -1 - 2 LSB V = 1.71 to V
V = 1.71 V to 3.6 V, REF DD
DD
1Msps
Differential non
linearity.
SID112B A_DNL -1 - 2.2 LSB V = 1 to V
V = 1.71 V to 5.5 V, REF DD
DD
500ksps
Total harmonic
SID113 A_THD - - -65 dB F = 10 kHz
distortion IN
SAR operating speed
SID261 FSARINTREF without external ref. - - 100 ksps 12-bit resolution
bypass
Datasheet 40 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| A_DNL | Differential non linearity. V = 1.71 V to 5.5 V, DD 1Msps | -1 | - | 2.2 | LSB |
| A_DNL | Differential non linearity. V = 1.71 V to 3.6 V, DD 1Msps | -1 | - | 2 | LSB |
| A_DNL | Differential non linearity. V = 1.71 V to 5.5 V, DD 500ksps | -1 | - | 2.2 | LSB |
| A_THD | Total harmonic distortion | - | - | -65 | dB |
| FSARINTREF | SAR operating speed without external ref. bypass | - | - | 100 | ksps |

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

## Page 42

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 17 CAPSENSE™ and IDAC specifications[7] (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Maximum Source
SID314B IDAC7_SRC3 current of 7-bit 275 - 330 µA LSB = 2.4µA typ.
IDAC in high range
Maximum Source
current of 7-bit LSB = 37.5nA typ.
SID314C IDAC7_SRC4 8 - 10.5 µA
IDAC in low range, 2X output stage
2X mode
Maximum Source
current of 7-bit LSB = 300nA typ.
SID314D IDAC7_SRC5 69 - 82 µA
IDAC in medium 2X output stage
range, 2X mode
Maximum Source
current of 7-bit LSB = 2.4µA typ.
SID314E IDAC7_SRC6 540 - 660 µA
IDAC in high range, 2X output stage
2X mode
Maximum Sink
SID315 IDAC7_SINK_1 current of 7-bit 4.2 - 5.7 µA LSB = 37.5nA typ.
IDAC in low range
Maximum Sink
current of 7-bit
SID315A IDAC7_SINK_2 34 - 44 µA LSB = 300nA typ.
IDAC in medium
range
Maximum Sink
SID315B IDAC7_SINK_3 current of 7-bit 260 - 340 µA LSB = 2.4µA typ.
IDAC in high range
Maximum Sink
current of 7-bit LSB = 37.5nA typ.
SID315C IDAC7_SINK_4 8 - 11.5 µA
IDAC in low range, 2X output stage
2X mode
Maximum Sink
current of 7-bit LSB = 300nA typ.
SID315D IDAC7_SINK_5 68 - 86 µA
IDAC in medium 2X output stage
range, 2X mode
Maximum Sink
current of 7-bit LSB = 2.4µA typ.
SID315E IDAC7_SINK_6 540 - 700 µA
IDAC in high range, 2X output stage
2X mode
Maximum Source
SID315F IDAC8_SRC_1 current of 8-bit 8.4 - 10.8 µA LSB = 37.5nA typ.
IDAC in low range
Maximum Source
current of 8-bit
SID315G IDAC8_SRC_2 68 - 82 µA LSB = 300nA typ.
IDAC in medium
range
Note
7.For optimal CAPSENSE™ performance, Ports 0, 4, and 5 must be used for large DC loads.
Datasheet 42 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| IDAC7_SRC3 | Maximum Source current of 7-bit IDAC in high range | 275 | - | 330 | µA |
| IDAC7_SRC4 | Maximum Source current of 7-bit IDAC in low range, 2X mode | 8 | - | 10.5 | µA |
| IDAC7_SRC5 | Maximum Source current of 7-bit IDAC in medium range, 2X mode | 69 | - | 82 | µA |
| IDAC7_SRC6 | Maximum Source current of 7-bit IDAC in high range, 2X mode | 540 | - | 660 | µA |
| IDAC7_SINK_1 | Maximum Sink current of 7-bit IDAC in low range | 4.2 | - | 5.7 | µA |
| IDAC7_SINK_2 | Maximum Sink current of 7-bit IDAC in medium range | 34 | - | 44 | µA |
| IDAC7_SINK_3 | Maximum Sink current of 7-bit IDAC in high range | 260 | - | 340 | µA |
| IDAC7_SINK_4 | Maximum Sink current of 7-bit IDAC in low range, 2X mode | 8 | - | 11.5 | µA |
| IDAC7_SINK_5 | Maximum Sink current of 7-bit IDAC in medium range, 2X mode | 68 | - | 86 | µA |
| IDAC7_SINK_6 | Maximum Sink current of 7-bit IDAC in high range, 2X mode | 540 | - | 700 | µA |
| IDAC8_SRC_1 | Maximum Source current of 8-bit IDAC in low range | 8.4 | - | 10.8 | µA |
| IDAC8_SRC_2 | Maximum Source current of 8-bit IDAC in medium range | 68 | - | 82 | µA |

## Page 43

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 17 CAPSENSE™ and IDAC specifications[7] (continued)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Maximum Source
SID315H IDAC8_SRC_3 current of 8-bit 550 - 680 µA LSB = 2.4µA typ.
IDAC in high range
Maximum Sink
SID315J IDAC8_SINK_1 current of 8-bit 8.4 - 11.4 µA LSB = 37.5nA typ.
IDAC in low range
Maximum Sink
current of 8-bit
SID315K IDAC8_SINK_2 68 - 88 µA LSB = 300nA typ.
IDAC in medium
range
Maximum Sink
SID315L IDAC8_SINK_3 current of 8-bit 540 - 670 µA LSB = 2.4µA typ.
IDAC in high range
All zeroes input;
Polarity set by
SID320 IDACOFFSET1 Medium and High - - 1 LSB
Source or Sink
range
All zeroes input; Polarity set by
SID320A IDACOFFSET2 - - 2 LSB
Low range Source or Sink
Full-scale error less
SID321 IDACGAIN - - ±20 %
offset
Mismatch between
SID322 IDACMISMATCH1 IDAC1 and IDAC2 in - - 9.2 LSB LSB = 37.5nA typ.
Low mode
Mismatch between
SID322A IDACMISMATCH2 IDAC1 and IDAC2 in - - 6 LSB LSB = 300nA typ.
Medium mode
Mismatch between
SID322B IDACMISMATCH3 IDAC1 and IDAC2 in - - 6.8 LSB LSB = 2.4µA typ.
High mode
Full-scale
Settling time to 0.5
SID323 IDACSET8 - - 10 µs transition. No
LSB for 8-bit IDAC
external load.
Full-scale
Settling time to 0.5
SID324 IDACSET7 - - 10 µs transition. No
LSB for 7-bit IDAC
external load.
External modulator 5-V rating, X7R or
SID325 CMOD - 2.2 - nF
capacitor. NP0 cap.
Note
7.For optimal CAPSENSE™ performance, Ports 0, 4, and 5 must be used for large DC loads.
Datasheet 43 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| IDAC8_SRC_3 | Maximum Source current of 8-bit IDAC in high range | 550 | - | 680 | µA |
| IDAC8_SINK_1 | Maximum Sink current of 8-bit IDAC in low range | 8.4 | - | 11.4 | µA |
| IDAC8_SINK_2 | Maximum Sink current of 8-bit IDAC in medium range | 68 | - | 88 | µA |
| IDAC8_SINK_3 | Maximum Sink current of 8-bit IDAC in high range | 540 | - | 670 | µA |
| IDACOFFSET1 | All zeroes input; Medium and High range | - | - | 1 | LSB |
| IDACOFFSET2 | All zeroes input; Low range | - | - | 2 | LSB |
| IDACGAIN | Full-scale error less offset | - | - | ±20 | % |
| IDACMISMATCH1 | Mismatch between IDAC1 and IDAC2 in Low mode | - | - | 9.2 | LSB |
| IDACMISMATCH2 | Mismatch between IDAC1 and IDAC2 in Medium mode | - | - | 6 | LSB |
| IDACMISMATCH3 | Mismatch between IDAC1 and IDAC2 in High mode | - | - | 6.8 | LSB |
| IDACSET8 | Settling time to 0.5 LSB for 8-bit IDAC | - | - | 10 | µs |
| IDACSET7 | Settling time to 0.5 LSB for 7-bit IDAC | - | - | 10 | µs |
| CMOD | External modulator capacitor. | - | 2.2 | - | nF |

## Page 44

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
Table 18 10-bit CAPSENSE™ ADC specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SIDA94 A_RES Resolution - - 10 bits 8 full speed.
Number of channels - Diff inputs use
SID95 A_CHNLS_S - - 16
single-ended neighboring I/O
SIDA97 A-MONO Monotonicity - - - Yes Yes
With external
SIDA98 A_GAINERR Gain error - - TBD %
reference.
Measured with 1-V
SIDA99 A_OFFSET Input offset voltage - - TBD mV
reference.
SIDA100 A_ISAR Current consumption - - TBD mA -
Input voltage range -
SIDA101 A_VINS V - V V -
SSA DDA
single-ended
SIDA103 A_INRES Input resistance - 2.2 - KΩ -
SIDA104 A_INCAP Input capacitance - 20 - pF -
Power supply rejection
SIDA106 A_PSRR TBD - - dB -
ratio
Sample acquisition
SIDA107 A_TACQ - 1 - µs -
time
Does not include
Conversion time for
8-bit resolution at acquisition time.
SIDA108 A_CONV8 conversion rate = - - 21.3 µs Equivalent to
Fhclk/(2^(N+2)). Clock
44.8ksps including
frequency = 48 MHz.
acquisition time.
Does not include
Conversion time for
10-bit resolution at acquisition time.
SIDA108A A_CONV10 conversion rate = - - 85.3 µs Equivalent to
Fhclk/(2^(N+2)). Clock
11.6ksps including
frequency = 48 MHz.
acquisition time.
Signal-to-noise and
SIDA109 A_SND distortion ratio TBD - - dB -
(SINAD)
Input bandwidth
SIDA110 A_BW - - 22.4 kHz 8-bit resolution
without aliasing
Integral non linearity.
V = 2.4V or
SIDA111 A_INL V = 1.71 V to 5.5 V, - - 2 LSB REF
DD
greater
1ksps
Differential non
linearity.
SIDA112 A_DNL - - 1 LSB -
V = 1.71 V to 5.5 V,
DD
1ksps
Datasheet 44 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Spec ID# | Parameter | Description | Min | Typ | Max | Unit | Details/conditions |
|---|---|---|---|---|---|---|---|
|  | A_RES | Resolution | - | - | 10 | bits |  |
|  | A_CHNLS_S | Number of channels - single-ended | - | - | 16 |  |  |
|  | A-MONO | Monotonicity | - | - | - | Yes |  |
|  | A_GAINERR | Gain error | - | - | TBD | % |  |
|  | A_OFFSET | Input offset voltage | - | - | TBD | mV |  |
|  | A_ISAR | Current consumption | - | - | TBD | mA |  |
|  | A_VINS | Input voltage range - single-ended | V SSA | - | V DDA | V |  |
|  | A_INRES | Input resistance | - | 2.2 | - | KΩ |  |
|  | A_INCAP | Input capacitance | - | 20 | - | pF |  |
|  | A_PSRR | Power supply rejection ratio | TBD | - | - | dB |  |
|  | A_TACQ | Sample acquisition time | - | 1 | - | µs |  |
|  | A_CONV8 | Conversion time for 8-bit resolution at conversion rate = Fhclk/(2^(N+2)). Clock frequency = 48 MHz. | - | - | 21.3 | µs |  |
|  | A_CONV10 | Conversion time for 10-bit resolution at conversion rate = Fhclk/(2^(N+2)). Clock frequency = 48 MHz. | - | - | 85.3 | µs |  |
|  | A_SND | Signal-to-noise and distortion ratio (SINAD) | TBD | - | - | dB |  |
|  | A_BW | Input bandwidth without aliasing | - | - | 22.4 | kHz |  |
|  | A_INL | Integral non linearity. V = 1.71 V to 5.5 V, DD 1ksps | - | - | 2 | LSB |  |
|  | A_DNL | Differential non linearity. V = 1.71 V to 5.5 V, DD 1ksps | - | - | 1 | LSB |  |

## Page 45

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.4 Digital Peripherals
6.4.1 Timer Counter Pulse-Width Modulator (TCPWM)
Table 19 TCPWM specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Block current
SID.TCPWM.1 ITCPWM1 - - 45 All modes (TCPWM)
consumption at 3 MHz
Block current
SID.TCPWM.2 ITCPWM2 - - 155 µA All modes (TCPWM)
consumption at 12 MHz
Block current
SID.TCPWM.2A ITCPWM3 - - 650 All modes (TCPWM)
consumption at 48 MHz
Fc max = CLK_SYS
SID.TCPWM.3 TCPWM FREQ Operating frequency - - Fc MHz
Maximum = 48 MHz
Input trigger pulse For all trigger
SID.TCPWM.4 TPWM ENEXT width 2/Fc - - events[8]
Minimum possible
width of Overflow,
Output trigger pulse Underflow, and CC
SID.TCPWM.5 TPWM EXT widths 2/Fc - - (Counter equals
Compare value)
outputs
Minimum time
ns
SID.TCPWM.5A TC RES Resolution of counter 1/Fc - - between
successive counts
Minimum pulse
SID.TCPWM.5B PWM RES PWM resolution 1/Fc - - width of PWM
Output
Minimum pulse
Quadrature inputs width between
SID.TCPWM.5C Q RES resolution 1/Fc - - Quadrature phase
inputs
Note
8.Trigger events can be Stop, Start, Reload, Count, Capture, or Kill depending on which mode of operation is
selected.
Datasheet 45 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| ITCPWM1 | Block current consumption at 3 MHz | - | - | 45 | µA |
| ITCPWM2 | Block current consumption at 12 MHz | - | - | 155 |  |
| ITCPWM3 | Block current consumption at 48 MHz | - | - | 650 |  |
| TCPWM FREQ | Operating frequency | - | - | Fc | MHz |
| TPWM ENEXT | Input trigger pulse width | 2/Fc | - | - | ns |
| TPWM EXT | Output trigger pulse widths | 2/Fc | - | - |  |
| TC RES | Resolution of counter | 1/Fc | - | - |  |
| PWM RES | PWM resolution | 1/Fc | - | - |  |
| Q RES | Quadrature inputs resolution | 1/Fc | - | - |  |

## Page 46

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
2
6.4.2 I C
Table 20 Fixed I2C DC specifications[9]
Spec ID Parameter Description Min Typ Max Unit Details/conditions
Block current
SID149 I consumption at - - 50 -
I2C1
100kHz
Block current
SID150 I consumption at - - 135 -
I2C2
400kHz µA
Block current
SID151 I consumption at - - 310 -
I2C3
1 Mbps
I2C enabled in Deep
SID152 I - - 1.4 -
I2C4 Sleep mode
Table 21 Fixed I2C AC specifications[9]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SID153 F Bit rate - - 1 Msps -
I2C1
Note
9.Guaranteed by characterization.
Datasheet 46 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I I2C1 | Block current consumption at 100kHz | - | - | 50 | µA |
| I I2C2 | Block current consumption at 400kHz | - | - | 135 |  |
| I I2C3 | Block current consumption at 1 Mbps | - | - | 310 |  |
| I I2C4 | I2C enabled in Deep Sleep mode | - | - | 1.4 |  |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F I2C1 | Bit rate | - | - | 1 | Msps |

## Page 47

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.4.3 SPI
Table 22 SPI DC specifications[10]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Block current
SID163 ISPI1 consumption at - - 360 -
1Mbits/sec
Block current
SID164 ISPI2 consumption at - - 560 µA -
4Mbits/sec
Block current
SID165 ISPI3 consumption at - - 600 -
8Mbits/sec
Table 23 SPI AC specifications[10]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SPI Operating
SID166 FSPI frequency (Master; 6X - - 8 MHz SID166
Oversampling)
Fixed SPI Master Mode AC specifications
MOSI Valid after
SID167 TDMO - - 15 -
SClock driving edge
MISO Valid before Full clock, late
SID168 TDSI 20 - - ns
SClock capturing edge MISO sampling
Previous MOSI data Referred to Slave
SID169 THMO 0 - -
hold time capturing edge
Fixed SPI Slave Mode AC specifications
MOSI Valid before
SID170 TDMI 40 - - -
Sclock Capturing edge
MISO Valid after Sclock
SID171 TDSO - - 42 + 3 × Tscb T = SCB clock
driving edge scb
MISO Valid after Sclock ns
SID171A TDSO_EXT driving edge in Ext. Clk - - 48 -
mode
Previous MISO data
SID172 THSO 0 - - -
hold time
Note
10.Guaranteed by characterization.
Datasheet 47 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| ISPI1 | Block current consumption at 1Mbits/sec | - | - | 360 | µA |
| ISPI2 | Block current consumption at 4Mbits/sec | - | - | 560 |  |
| ISPI3 | Block current consumption at 8Mbits/sec | - | - | 600 |  |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| FSPI | SPI Operating frequency (Master; 6X Oversampling) | - | - | 8 | MHz |

#### Table 3

| TDMO | MOSI Valid after SClock driving edge | - | - | 15 | ns |
|---|---|---|---|---|---|
| TDSI | MISO Valid before SClock capturing edge | 20 | - | - |  |
| THMO | Previous MOSI data hold time | 0 | - | - |  |

#### Table 4

| TDMI | MOSI Valid before Sclock Capturing edge | 40 | - | - | ns |
|---|---|---|---|---|---|
| TDSO | MISO Valid after Sclock driving edge | - | - | 42 + 3 × Tscb |  |
| TDSO_EXT | MISO Valid after Sclock driving edge in Ext. Clk mode | - | - | 48 |  |
| THSO | Previous MISO data hold time | 0 | - | - |  |

## Page 48

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.4.4 UART
Table 24 UART DC specifications[11]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Block current
SID160 I consumption at - - 55 µA -
UART1
100 Kbits/sec
Block current
SID161 I consumption at - - 312 µA -
UART2
1000 Kbits/sec
Table 25 UART AC specifications[11]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SID162 F Bit rate - - 1 Mbps -
UART
6.4.5 LCD
Table 26 LCD Direct Drive DC specifications[11]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Operating current in 16 × 4 small
SID154 I - 5 - µA
LCDLOW low power mode segment disp. at Hz
LCD capacitance per
SID155 C segment/common - 500 5000 pF -
LCDCAP
driver
Long-term segment
SID156 LCD - 20 - mV -
OFFSET offset
LCD system operating 32 × 4 segments.
SID157 I - 2 -
LCDOP1 current Vbias = 5V 50 Hz. 25°C
32 × 4 segments.
mA
LCD system operating 50 Hz. 25°C
SID158 I - 2 -
LCDOP2 current Vbias = 3.3V 4 segments.
50 Hz. 25°C.
Table 27 LCD Direct Drive AC specifications[11]
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SID159 F LCD frame rate 10 50 150 Hz -
LCD
Note
11.Guaranteed by characterization.
Datasheet 48 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I UART1 | Block current consumption at 100 Kbits/sec | - | - | 55 | µA |
| I UART2 | Block current consumption at 1000 Kbits/sec | - | - | 312 | µA |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F UART | Bit rate | - | - | 1 | Mbps |

#### Table 3

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I LCDLOW | Operating current in low power mode | - | 5 | - | µA |
| C LCDCAP | LCD capacitance per segment/common driver | - | 500 | 5000 | pF |
| LCD OFFSET | Long-term segment offset | - | 20 | - | mV |
| I LCDOP1 | LCD system operating current Vbias = 5V | - | 2 | - | mA |
| I LCDOP2 | LCD system operating current Vbias = 3.3V | - | 2 | - |  |

#### Table 4

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F LCD | LCD frame rate | 10 | 50 | 150 | Hz |

## Page 49

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.5 Memory
6.5.1 Flash
Table 28 Flash DC specifications
Details/
Spec ID# Parameter Description Min Typ Max Unit
conditions
SID173 V Erase and program voltage 1.71 - 5.5 V -
PE
Table 29 Flash AC specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Row (block) write
Row (block) =
SID174 T [12] time (erase and - - 20
ROWWRITE 64bytes
program)
SID175 T [12] Row erase time - - 13 -
ROWERASE
ms
Row program time
SID176 T [12] - - 7 -
ROWPROGRAM after erase
Bulk erase time
SID178 T [12] - - 15 -
BULKERASE (16 KB)
Total device
SID180[13] T [12] - - 7.5 Seconds -
DEVPROG program time
SID181[13] F Flash endurance 100K - - Cycles -
END
Flash retention.
SID182[13] F T  55°C, 20 - - -
RET A
100K P/E cycles
Flash retention.
SID182A[13] - T  85°C, 10 - - -
A
10K P/E cycles Years
Flash retention.
T  105°C,
A Guaranteed by
SID182B[13] F 10K P/E cycles; 10 - -
RETQ characterization
 three years at
T  85°C
A
Number of Wait CPU execution
SID256 TWS48 2 - -
states at 48 MHz from Flash
Number of Wait CPU execution
SID257 TWS24 1 - -
states at 24 MHz from Flash
Notes
12.It can take as much as 20 milliseconds to write to Flash. During this time the device should not be Reset, or
Flash operations will be interrupted and cannot be relied on to have completed. Reset sources include the
XRES pin, software resets, CPU lockup states and privilege violations, improper power supply levels, and
watchdogs. Make certain that these are not inadvertently activated.
13.Guaranteed by characterization.
Datasheet 49 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V PE | Erase and program voltage | 1.71 | - | 5.5 | V |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| T [12] ROWWRITE | Row (block) write time (erase and program) | - | - | 20 | ms |
| T [12] ROWERASE | Row erase time | - | - | 13 |  |
| T [12] ROWPROGRAM | Row program time after erase | - | - | 7 |  |
| T [12] BULKERASE | Bulk erase time (16 KB) | - | - | 15 |  |
| T [12] DEVPROG | Total device program time | - | - | 7.5 | Seconds |
| F END | Flash endurance | 100K | - | - | Cycles |
| F RET | Flash retention. T  55°C, A 100K P/E cycles | 20 | - | - | Years |
| - | Flash retention. T  85°C, A 10K P/E cycles | 10 | - | - |  |
| F RETQ | Flash retention. T  105°C, A 10K P/E cycles;  three years at T  85°C A | 10 | - | - |  |
| TWS48 | Number of Wait states at 48 MHz | 2 | - | - |  |
| TWS24 | Number of Wait states at 24 MHz | 1 | - | - |  |

## Page 50

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.6 System resources
6.6.1 Power-on Reset (POR)
Table 30 POR
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
Power supply slew At power-up and
SID.CLK#6 SR_POWER_UP 1 - 67 V/ms
rate power-down.
SID185[14] V Rising trip voltage 0.80 - 1.5 -
RISEIPOR
V
SID186[14] V Falling trip voltage 0.70 - 1.4 -
FALLIPOR
Table 31 Brown-out Detect (BOD) for V
CCD
Spec ID Parameter Description Min Typ Max Unit Details/conditions
BOD trip voltage in active and
SID190[14] V 1.48 - 1.62 -
FALLPPOR sleep modes V
SID192[14] V BOD trip voltage in Deep Sleep 1.1 - 1.5 -
FALLDPSLP
6.6.2 SWD Interface
Table 32 SWD Interface specifications
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
SWDCLK ≤ 1/3 CPU
SID213 F_SWDCLK1 3.3V  V  5.5V - - 14
DD clock frequency
MHz
SWDCLK ≤ 1/3 CPU
SID214 F_SWDCLK2 1.71V  V  3.3V - - 7
DD clock frequency
SID215[14] T_SWDI_SETUP T = 1/f SWDCLK 0.25 × T - - -
SID216[14] T_SWDI_HOLD T = 1/f SWDCLK 0.25 × T - - -
ns
SID217[14] T_SWDO_VALID T = 1/f SWDCLK - - 0.5 × T -
SID217A[14] T_SWDO_HOLD T = 1/f SWDCLK 1 - - -
Note
14.Guaranteed by characterization.
Datasheet 50 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| SR_POWER_UP | Power supply slew rate | 1 | - | 67 | V/ms |
| V RISEIPOR | Rising trip voltage | 0.80 | - | 1.5 | V |
| V FALLIPOR | Falling trip voltage | 0.70 | - | 1.4 |  |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| V FALLPPOR | BOD trip voltage in active and sleep modes | 1.48 | - | 1.62 | V |
| V FALLDPSLP | BOD trip voltage in Deep Sleep | 1.1 | - | 1.5 |  |

#### Table 3

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F_SWDCLK1 | 3.3V  V  5.5V DD | - | - | 14 | MHz |
| F_SWDCLK2 | 1.71V  V  3.3V DD | - | - | 7 |  |
| T_SWDI_SETUP | T = 1/f SWDCLK | 0.25 × T | - | - | ns |
| T_SWDI_HOLD | T = 1/f SWDCLK | 0.25 × T | - | - |  |
| T_SWDO_VALID | T = 1/f SWDCLK | - | - | 0.5 × T |  |
| T_SWDO_HOLD | T = 1/f SWDCLK | 1 | - | - |  |

## Page 51

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.6.3 Internal Main Oscillator (IMO)
Table 33 IMO DC specifications
(Guaranteed by design)
Spec ID# Parameter Description Min Typ Max Unit Details/conditions
IMO operating current
SID218 I - - 250 µA -
IMO1 at 48 MHz
IMO operating current
SID219 I - - 180 µA -
IMO2 at 24 MHz
Table 34 IMO AC specifications
Spec ID Parameter Description Min Typ Max Unit Details/conditions
Frequency range from 2 V  V  5.5 V,
DD
SID223 F 24MHz to 48MHz -2 - +2 % and
IMOTOL1
(4-MHz increments) -25°C  T  85°C
A
SID226 T IMO startup time - - 7 µs -
STARTIMO
SID228 T RMS jitter at 24 MHz - 145 - ps -
JITRMSIMO2
6.6.4 Internal low-speed oscillator (ILO)
Table 35 ILO DC specifications
(Guaranteed by design)
Details/
Spec ID Parameter Description Min Typ Max Unit
conditions
SID231[15] I ILO operating current - 0.3 1.05 µA -
ILO1
Table 36 ILO AC specifications
Details/
Spec ID Parameter Description Min Typ Max Unit
conditions
SID234[15] T ILO startup time - - 2 ms -
STARTILO1
SID236[15] T ILO duty cycle 40 50 60 % -
ILODUTY
SID237 F ILO frequency range 20 40 80 kHz -
ILOTRIM1
Note
15.Guaranteed by characterization.
Datasheet 51 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I IMO1 | IMO operating current at 48 MHz | - | - | 250 | µA |
| I IMO2 | IMO operating current at 24 MHz | - | - | 180 | µA |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| F IMOTOL1 | Frequency range from 24MHz to 48MHz (4-MHz increments) | -2 | - | +2 | % |
| T STARTIMO | IMO startup time | - | - | 7 | µs |
| T JITRMSIMO2 | RMS jitter at 24 MHz | - | 145 | - | ps |

#### Table 3

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| I ILO1 | ILO operating current | - | 0.3 | 1.05 | µA |

#### Table 4

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| T STARTILO1 | ILO startup time | - | - | 2 | ms |
| T ILODUTY | ILO duty cycle | 40 | 50 | 60 | % |
| F ILOTRIM1 | ILO frequency range | 20 | 40 | 80 | kHz |

## Page 52

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Electrical specifications
6.6.5 Watch Crystal Oscillator (WCO)
Table 37 Watch Crystal Oscillator (WCO) specifications
Details/
Spec ID Parameter Description Min Typ Max Unit
conditions
SID398 FWCO Crystal Frequency - 32.768 - kHz -
With 20-ppm
SID399 FTOL Frequency tolerance - 50 250 ppm
crystal
SID400 ESR Equivalent series resistance - 50 - kΩ -
SID401 PD Drive Level - - 1 µW -
SID402 TSTART Startup time - - 500 ms -
SID403 CL Crystal Load Capacitance 6 - 12.5 pF -
SID404 C0 Crystal Shunt Capacitance - 1.35 - pF -
Operating Current (high
SID405 IWCO1 - - 8 µA -
power mode)
6.6.6 External Clock
Table 38 External Clock specifications
Details/
Spec ID Parameter Description Min Typ Max Unit
conditions
External clock input
SID305[15] ExtClkFreq 0 - 48 MHz -
frequency
Duty cycle; measured at
SID306[15] ExtClkDuty 45 - 55 % -
V
DD/2
6.6.7 Block
Table 39 Block specifications
Spec ID Parameter Description Min Typ Max Unit Details/conditions
System clock
SID262[16] T source switching 3 - 4 Periods -
CLKSWITCH
time
6.6.8 PRGIO Pass-through Time
Table 40 PRGIO Pass-through Time (Delay in Bypass Mode)
Details/
Spec ID Parameter Description Min Typ Max Unit
conditions
Max. delay added
SID252 PRG_BYPASS by PRGIO in bypass - - 1.6 ns -
mode
Note
16.Guaranteed by characterization.
Datasheet 52 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| FWCO | Crystal Frequency | - | 32.768 | - | kHz |
| FTOL | Frequency tolerance | - | 50 | 250 | ppm |
| ESR | Equivalent series resistance | - | 50 | - | kΩ |
| PD | Drive Level | - | - | 1 | µW |
| TSTART | Startup time | - | - | 500 | ms |
| CL | Crystal Load Capacitance | 6 | - | 12.5 | pF |
| C0 | Crystal Shunt Capacitance | - | 1.35 | - | pF |
| IWCO1 | Operating Current (high power mode) | - | - | 8 | µA |

#### Table 2

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| ExtClkFreq | External clock input frequency | 0 | - | 48 | MHz |
| ExtClkDuty | Duty cycle; measured at V DD/2 | 45 | - | 55 | % |

#### Table 3

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| T CLKSWITCH | System clock source switching time | 3 | - | 4 | Periods |

#### Table 4

| Parameter | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| PRG_BYPASS | Max. delay added by PRGIO in bypass mode | - | - | 1.6 | ns |

## Page 53

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Ordering information
7 Ordering information
Table 41 Ordering information
Datasheet 53 002-22097 Rev. *F
2023-11-16
yrogetaC
NPM
Features Package
)zHM(
deepS
UPC
xaM AMD
)BK(
hsalF
)BK(
MARS
CADV
tib-31
)BTC(
pmapO
™ESNESPAC
CDA
DSC
tib-01
evird
DCL
tceriD CTR
CDA
RAS
tib-21
srotarapmoc
PL
skcolb
MWPCT
skcolb
BCS
sOI
tramS OIPG
POSS
nip-82
PSCLW
llab-54
PFQT
nip-84
NFQ
nip-84
)C°(
egnar
erutarepmeT
806
CY8C4125PVI-PS421 24 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 20 ✓ - - -
ksps
806
CY8C4125FNI-PS423 24 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 37 - ✓ - -
ksps
4125
806
CY8C4125AZI-PS423 24 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 38 - - ✓ -
ksps
-40 to 85
806
CY8C4125LQI-PS423 24 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 38 - - - ✓
ksps
1000
CY8C4145PVI-PS421 48 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 20 ✓ - - -
ksps
1000
CY8C4145FNI-PS423 48 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 37 - ✓ - -
ksps
1000
CY8C4145FNQ-PS423 48 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 37 - ✓ - - -40 to 105
ksps
1000
CY8C4145AZI-PS423 48 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 38 - - ✓ -
ksps
1000
CY8C4145LQI-PS423 48 ✓ 32 4 2 4 - ✓ ✓ ✓ 2 8 2 8 38 - - - ✓
ksps
4145 -40 to 85
1000
CY8C4145PVI-PS431 48 ✓ 32 4 2 4 ✓ ✓ ✓ ✓ 2 8 3 8 20 ✓ - - -
ksps
1000
CY8C4145FNI-PS433 48 ✓ 32 4 2 4 ✓ ✓ ✓ ✓ 2 8 3 8 37 - ✓ - -
ksps
1000
CY8C4145FNQ-PS433 48 ✓ 32 4 2 4 ✓ ✓ ✓ ✓ 2 8 3 8 37 - ✓ - - -40 to 105
ksps
1000
CY8C4145AZI-PS433 48 ✓ 32 4 2 4 ✓ ✓ ✓ ✓ 2 8 3 8 38 - - ✓ -
ksps
-40 to 85
1000
CY8C4145LQI-PS433 48 ✓ 32 4 2 4 ✓ ✓ ✓ ✓ 2 8 3 8 38 - - - ✓
ksps
```

### Extracted Tables

#### Table 1

| NPM | Features |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Package |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | )zHM( deepS UPC xaM | AMD | )BK( hsalF | )BK( MARS | CADV tib-31 | )BTC( pmapO | ™ESNESPAC | CDA DSC tib-01 | evird DCL tceriD | CTR | CDA RAS tib-21 | srotarapmoc PL | skcolb MWPCT | skcolb BCS | sOI tramS | OIPG | POSS nip-82 | PSCLW llab-54 | PFQT nip-84 | NFQ nip-84 |
| CY8C4125PVI-PS421 | 24 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 806 ksps | 2 | 8 | 2 | 8 | 20 | ✓ | - | - | - |
| CY8C4125FNI-PS423 | 24 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 806 ksps | 2 | 8 | 2 | 8 | 37 | - | ✓ | - | - |
| CY8C4125AZI-PS423 | 24 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 806 ksps | 2 | 8 | 2 | 8 | 38 | - | - | ✓ | - |
| CY8C4125LQI-PS423 | 24 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 806 ksps | 2 | 8 | 2 | 8 | 38 | - | - | - | ✓ |
| CY8C4145PVI-PS421 | 48 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 2 | 8 | 20 | ✓ | - | - | - |
| CY8C4145FNI-PS423 | 48 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 2 | 8 | 37 | - | ✓ | - | - |
| CY8C4145FNQ-PS423 | 48 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 2 | 8 | 37 | - | ✓ | - | - |
| CY8C4145AZI-PS423 | 48 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 2 | 8 | 38 | - | - | ✓ | - |
| CY8C4145LQI-PS423 | 48 | ✓ | 32 | 4 | 2 | 4 | - | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 2 | 8 | 38 | - | - | - | ✓ |
| CY8C4145PVI-PS431 | 48 | ✓ | 32 | 4 | 2 | 4 | ✓ | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 3 | 8 | 20 | ✓ | - | - | - |
| CY8C4145FNI-PS433 | 48 | ✓ | 32 | 4 | 2 | 4 | ✓ | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 3 | 8 | 37 | - | ✓ | - | - |
| CY8C4145FNQ-PS433 | 48 | ✓ | 32 | 4 | 2 | 4 | ✓ | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 3 | 8 | 37 | - | ✓ | - | - |
| CY8C4145AZI-PS433 | 48 | ✓ | 32 | 4 | 2 | 4 | ✓ | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 3 | 8 | 38 | - | - | ✓ | - |
| CY8C4145LQI-PS433 | 48 | ✓ | 32 | 4 | 2 | 4 | ✓ | ✓ | ✓ | ✓ | 1000 ksps | 2 | 8 | 3 | 8 | 38 | - | - | - | ✓ |

## Page 54

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Ordering information
The nomenclature used in the preceding table is based on the following part numbering convention:
Table 42 Nomenclature
Field Description Values Meaning
CY8C Cypress, an Infineon company prefix
4 Architecture 4 Arm® Cortex®-M0+ CPU
A Family 1 4100PS Family
2 24 MHz
B Maximum frequency
4 48 MHz
C Flash Memory Capacity 5 32 KB
AZ TQFP (0.5 mm pitch)
LQ QFN
DE Package Code
PV SSOP
FN CSP
S Series Designator PS S-Series
I Industrial
F Temperature Range
Q Extended Industrial
XYZ Attributes Code 000-999 Code of feature set in the specific family
The following is an example of a part number:
Example CY 8 C 4 A B C DE F - S XYZ
Cypress, an Infineon company prefix
4: PSoC™ 4 Architecture
1: 4100 Family Family within Architecture
4: 48 MHz CPU speed
5: 32 KB Flash capacity
AZ: TQFP Package code
I: Industrial Temperature range
Series designator
Attributes code
Datasheet 54 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Field | Description | Values | Meaning |
|---|---|---|---|
|  | Cypress, an Infineon company prefix |  |  |
|  | Architecture | 4 |  |
|  | Family | 1 |  |
|  | Maximum frequency | 2 |  |
|  |  | 4 |  |
|  | Flash Memory Capacity | 5 |  |
|  | Package Code | AZ |  |
|  |  | LQ |  |
|  |  | PV |  |
|  |  | FN |  |
|  | Series Designator | PS |  |
|  | Temperature Range | I |  |
|  |  | Q |  |
|  | Attributes Code | 000-999 |  |

## Page 55

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Packaging
8 Packaging
Table 43 Details
Spec ID# Package Description Package DWG #
BID20 48-pin TQFP 7 × 7 × 1.4 mm A48 51-85135
BID27 48-pin QFN 6 × 6 × 0.6 mm LR48A/LQ48A 4.6 × 4.6 E-Pad (Sawn) 001-57280
BID34 45-ball WLCSP 1.986 × 3.691 × 0.482 mm FN45B 002-24003
BID34A 28-pin SSOP 10.2 × 5.3 × 2.0 mm SP28 51-85079
Table 44 Package Thermal characteristics
Parameter Description Package Min Typ Max Unit
TA Operating Ambient temperature - -40 25 105 °C
TJ Operating junction temperature - -40 - 125 °C
TJA Package θ
JA
48-pin TQFP - 71 - °C/W
TJC Package θ
JC
48-pin TQFP - 34.3 - °C/W
TJA Package θ
JA
48-pin QFN - 18 - °C/W
TJC Package θ
JC
48-pin QFN - 4.5 - °C/W
TJA Package θ
JA
45-ball WLCSP - 37.2 - °C/W
TJC Package θ
JC
45-ball WLCSP - 0.31 - °C/W
TJA Package θ
JA
28-pin SSOP - 60 - °C/W
TJC Package θ
JC
28-pin SSOP - 25 - °C/W
Table 45 Solder Reflow Peak Temperature
Package Maximum Peak Temperature Maximum Time at Peak Temperature
All 260°C 30 seconds
Table 46 Package Moisture Sensitivity Level (MSL), IPC/JEDEC J-STD-020
Package MSL
All MSL 3
Datasheet 55 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Package | Description |
|---|---|
| 48-pin TQFP | 7 × 7 × 1.4 mm A48 |
| 48-pin QFN | 6 × 6 × 0.6 mm LR48A/LQ48A 4.6 × 4.6 E-Pad (Sawn) |
| 45-ball WLCSP | 1.986 × 3.691 × 0.482 mm FN45B |
| 28-pin SSOP | 10.2 × 5.3 × 2.0 mm SP28 |

#### Table 2

| Parameter | Description | Package | Min | Typ | Max | Unit |
|---|---|---|---|---|---|---|
|  | Operating Ambient temperature | - | -40 | 25 | 105 |  |
|  | Operating junction temperature | - | -40 | - | 125 |  |
|  | Package θ JA | 48-pin TQFP | - | 71 | - |  |
|  | Package θ JC | 48-pin TQFP | - | 34.3 | - |  |
|  | Package θ JA | 48-pin QFN | - | 18 | - |  |
|  | Package θ JC | 48-pin QFN | - | 4.5 | - |  |
|  | Package θ JA | 45-ball WLCSP | - | 37.2 | - |  |
|  | Package θ JC | 45-ball WLCSP | - | 0.31 | - |  |
|  | Package θ JA | 28-pin SSOP | - | 60 | - |  |
|  | Package θ JC | 28-pin SSOP | - | 25 | - |  |

#### Table 3

| Package | Maximum Peak Temperature | Maximum Time at Peak Temperature |
|---|---|---|
| All | 260°C | 30 seconds |

## Page 56

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Packaging
8.1 Package diagrams
51-85135 Rev. *C
Figure 7 48-pin TQFP (7 × 7 × 1.4 mm) A48 package outline (PG-TQFP-48), 51-85135
Datasheet 56 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| 8. | 1 Package diagrams |  |  |  |  |
|---|---|---|---|---|---|
| Fi | gure 7 48-pin TQFP (7 × 7 × 1.4 mm) A48 package outline (PG-TQFP-48), 51-85135 |  |  |  |  |

## Page 57

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Packaging
001-57280 Rev. *E
Figure 8 48-pin QFN ((6 × 6 × 0.6 mm) LR48A/LQ48A 4.6 × 4.6 E-Pad (Sawn)) package outline
(PG-VQFN-48), 001-57280
Note:
The center pad on the QFN package should be connected to ground (VSS) for best mechanical, thermal, and
electrical performance. If not connected to ground, it should be electrically floating and not connected to any
other signal.
Datasheet 57 002-22097 Rev. *F
2023-11-16
```

## Page 58

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Packaging
7 6
5 4 3 2 1
A
B
C
D
E
F
G
H
J
5
NOTES:
DIMENSIONS
SYMBOL 1.ALL DIMENSIONS ARE IN MILLIMETERS.
MIN NOM MAX
2.SOLDER BALL POSITION DESIGNATION PER JEP95, SECTION 3, SPP-020.
A - - 0.482 3. "e" REPRESENTS THE SOLDER BALL GRID PITCH.
A1 0.141 - - 4. SYMBOL "MD" IS THE BALL MATRIX SIZE IN THE "D" DIRECTION.
D 1.986 BSC SYMBOL "ME" IS THE BALL MATRIX SIZE IN THE "E" DIRECTION.
N IS THE NUMBER OF POPULATED SOLDER BALL POSITIONS FOR MATRIX
E 3.691 BSC
SIZE MD X ME.
D1 1.52 BSC
5.DIMENSION "b" IS MEASURED AT THE MAXIMUM BALL DIAMETER IN A
E1 3.04 BSC PLANE PARALLEL TO DATUM C.
E2 0.263 BSC 6."SD" AND "SE" ARE MEASURED WITH RESPECT TO DATUMS A AND B AND
E3 0.388 BSC DEFINE THE POSITION OF THE CENTER SOLDER BALL IN THE OUTER ROW.
WHEN THERE IS AN ODD NUMBER OF SOLDER BALLS IN THE OUTER ROW,
MD 5
"SD" OR "SE" = 0.
ME 9
WHEN THERE IS AN EVEN NUMBER OF SOLDER BALLS IN THE OUTER ROW,
N 45 "SD" = eD/2 AND "SE" = eE/2.
Øb 0.19 0.22 0.25 7.A1 CORNER TO BE IDENTIFIED BY CHAMFER, LASER OR INK MARK,
eD 0.38 BSC METALIZED MARK, INDENTATION OR OTHER MEANS.
eE 0.38 BSC 8."+" INDICATES THE THEORETICAL CENTER OF DEPOPULATED SOLDER
SD 0.00 BSC BALLS.
SE 0.063 BSC 9.JEDEC SPECIFICATION NO. REF. : N/A.
CYPRESS
CompanyConfidential
002-24003 Rev. **
Figure 9 45-ball WLCSP (1.986 × 3.691 × 0.482 mm) FN45B package outline (SG-XFWLB-45), 002-24003
Datasheet 58 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

|  | 7 6 5 4 3 2 1 A B C D E F G H J 5 NOTES: DIMENSIONS SYMBOL 1.ALL DIMENSIONS ARE IN MILLIMETERS. MIN NOM MAX 2.SOLDER BALL POSITION DESIGNATION PER JEP95, SECTION 3, SPP-020. A - - 0.482 3. "e" REPRESENTS THE SOLDER BALL GRID PITCH. A1 0.141 - - 4. SYMBOL "MD" IS THE BALL MATRIX SIZE IN THE "D" DIRECTION. D 1.986 BSC SYMBOL "ME" IS THE BALL MATRIX SIZE IN THE "E" DIRECTION. N IS THE NUMBER OF POPULATED SOLDER BALL POSITIONS FOR MATRIX E 3.691 BSC SIZE MD X ME. D1 1.52 BSC 5.DIMENSION "b" IS MEASURED AT THE MAXIMUM BALL DIAMETER IN A E1 3.04 BSC PLANE PARALLEL TO DATUM C. E2 0.263 BSC 6."SD" AND "SE" ARE MEASURED WITH RESPECT TO DATUMS A AND B AND E3 0.388 BSC DEFINE THE POSITION OF THE CENTER SOLDER BALL IN THE OUTER ROW. WHEN THERE IS AN ODD NUMBER OF SOLDER BALLS IN THE OUTER ROW, MD 5 "SD" OR "SE" = 0. ME 9 WHEN THERE IS AN EVEN NUMBER OF SOLDER BALLS IN THE OUTER ROW, N 45 "SD" = eD/2 AND "SE" = eE/2. Øb 0.19 0.22 0.25 7.A1 CORNER TO BE IDENTIFIED BY CHAMFER, LASER OR INK MARK, eD 0.38 BSC METALIZED MARK, INDENTATION OR OTHER MEANS. eE 0.38 BSC 8."+" INDICATES THE THEORETICAL CENTER OF DEPOPULATED SOLDER SD 0.00 BSC BALLS. SE 0.063 BSC 9.JEDEC SPECIFICATION NO. REF. : N/A. CYPRESS CompanyConfidential 002-24003 Rev. ** |  |  |
|---|---|---|---|

#### Table 2

| 7 6 5 4 3 2 1 A B C D E F G H J 5 NOTES: DIMENSIONS SYMBOL 1.ALL DIMENSIONS ARE IN MILLIMETERS. MIN NOM MAX 2.SOLDER BALL POSITION DESIGNATION PER JEP95, SECTION 3, SPP-020. A - - 0.482 3. "e" REPRESENTS THE SOLDER BALL GRID PITCH. A1 0.141 - - 4. SYMBOL "MD" IS THE BALL MATRIX SIZE IN THE "D" DIRECTION. D 1.986 BSC SYMBOL "ME" IS THE BALL MATRIX SIZE IN THE "E" DIRECTION. N IS THE NUMBER OF POPULATED SOLDER BALL POSITIONS FOR MATRIX E 3.691 BSC SIZE MD X ME. D1 1.52 BSC 5.DIMENSION "b" IS MEASURED AT THE MAXIMUM BALL DIAMETER IN A E1 3.04 BSC PLANE PARALLEL TO DATUM C. E2 0.263 BSC 6."SD" AND "SE" ARE MEASURED WITH RESPECT TO DATUMS A AND B AND E3 0.388 BSC DEFINE THE POSITION OF THE CENTER SOLDER BALL IN THE OUTER ROW. WHEN THERE IS AN ODD NUMBER OF SOLDER BALLS IN THE OUTER ROW, MD 5 "SD" OR "SE" = 0. ME 9 WHEN THERE IS AN EVEN NUMBER OF SOLDER BALLS IN THE OUTER ROW, N 45 "SD" = eD/2 AND "SE" = eE/2. Øb 0.19 0.22 0.25 7.A1 CORNER TO BE IDENTIFIED BY CHAMFER, LASER OR INK MARK, eD 0.38 BSC METALIZED MARK, INDENTATION OR OTHER MEANS. eE 0.38 BSC 8."+" INDICATES THE THEORETICAL CENTER OF DEPOPULATED SOLDER SD 0.00 BSC BALLS. SE 0.063 BSC 9.JEDEC SPECIFICATION NO. REF. : N/A. CYPRESS |  |  |
|---|---|---|
|  | CompanyConfidential |  |

#### Table 3

| SYMBOL | DIMENSIONS |  |  |
|---|---|---|---|
|  | MIN | NOM | MAX |
| A | - | - | 0.482 |
| A1 | 0.141 | - | - |
| D | 1.986 BSC |  |  |
| E | 3.691 BSC |  |  |
| D1 | 1.52 BSC |  |  |
| E1 | 3.04 BSC |  |  |
| E2 | 0.263 BSC |  |  |
| E3 | 0.388 BSC |  |  |
| MD | 5 |  |  |
| ME | 9 |  |  |
| N | 45 |  |  |
| Øb | 0.19 | 0.22 | 0.25 |
| eD | 0.38 BSC |  |  |
| eE | 0.38 BSC |  |  |
| SD | 0.00 BSC |  |  |

## Page 59

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Packaging
51-85079 Rev. *G
Figure 10 28-pin SSOP (10.2 × 5.3 × 2.0 mm) SP28 package outline (PG-SSOP-28), 51-85079
Datasheet 59 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

|  | ackaging 51-85079 Rev. *G gure 10 28-pin SSOP (10.2 × 5.3 × 2.0 mm) SP28 package outline (PG-SSOP-28), 51-85079 |  |
|---|---|---|
|  | 51-85079 Rev. *G |  |
|  | gure 10 28-pin SSOP (10.2 × 5.3 × 2.0 mm) SP28 package outline (PG-SSOP-28), |  |

## Page 60

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Acronyms
9 Acronyms
Table 47 Acronyms used in this document
Acronym Description
abus analog local bus
ADC analog-to-digital converter
AG analog global
AMBA (advanced microcontroller bus architecture) high-performance bus, an Arm® data
AHB
transfer bus
ALU arithmetic logic unit
AMUXBUS analog multiplexer bus
API application programming interface
APSR application program status register
Arm® advanced RISC machine, a CPU architecture
ATM automatic thump mode
BW bandwidth
CAN Controller Area Network, a communications protocol
CMRR common-mode rejection ratio
CPU central processing unit
CRC cyclic redundancy check, an error-checking protocol
DAC digital-to-analog converter, see also IDAC, VDAC
DFB digital filter block
DIO digital input/output, GPIO with only digital capabilities, no analog. See GPIO.
DMIPS Dhrystone million instructions per second
DMA direct memory access, see also TD
DNL differential nonlinearity, see also INL
DNU do not use
DR port write data registers
DSI digital system interconnect
DWT data watchpoint and trace
ECC error correcting code
ECO external crystal oscillator
EEPROM electrically erasable programmable read-only memory
EMI electromagnetic interference
EMIF external memory interface
EOC end of conversion
EOF end of frame
EPSR execution program status register
ESD electrostatic discharge
ETM embedded trace macrocell
FIR finite impulse response, see also IIR
Datasheet 60 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Acronym | Description |
|---|---|
| abus | analog local bus |
| ADC | analog-to-digital converter |
| AG | analog global |
| AHB | AMBA (advanced microcontroller bus architecture) high-performance bus, an Arm® data transfer bus |
| ALU | arithmetic logic unit |
| AMUXBUS | analog multiplexer bus |
| API | application programming interface |
| APSR | application program status register |
| Arm® | advanced RISC machine, a CPU architecture |
| ATM | automatic thump mode |
| BW | bandwidth |
| CAN | Controller Area Network, a communications protocol |
| CMRR | common-mode rejection ratio |
| CPU | central processing unit |
| CRC | cyclic redundancy check, an error-checking protocol |
| DAC | digital-to-analog converter, see also IDAC, VDAC |
| DFB | digital filter block |
| DIO | digital input/output, GPIO with only digital capabilities, no analog. See GPIO. |
| DMIPS | Dhrystone million instructions per second |
| DMA | direct memory access, see also TD |
| DNL | differential nonlinearity, see also INL |
| DNU | do not use |
| DR | port write data registers |
| DSI | digital system interconnect |
| DWT | data watchpoint and trace |
| ECC | error correcting code |
| ECO | external crystal oscillator |
| EEPROM | electrically erasable programmable read-only memory |
| EMI | electromagnetic interference |
| EMIF | external memory interface |
| EOC | end of conversion |
| EOF | end of frame |
| EPSR | execution program status register |
| ESD | electrostatic discharge |
| ETM | embedded trace macrocell |
| FIR | finite impulse response, see also IIR |

## Page 61

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Acronyms
Table 47 Acronyms used in this document (continued)
Acronym Description
FPB flash patch and breakpoint
FS full-speed
GPIO general-purpose input/output, applies to a PSoC pin
HVI high-voltage interrupt, see also LVI, LVD
IC integrated circuit
IDAC current DAC, see also DAC, VDAC
IDE integrated development environment
I2C, or IIC Inter-Integrated Circuit, a communications protocol
IIR infinite impulse response, see also FIR
ILO internal low-speed oscillator, see also IMO
IMO internal main oscillator, see also ILO
INL integral nonlinearity, see also DNL
I/O input/output, see also GPIO, DIO, SIO, USBIO
IPOR initial power-on reset
IPSR interrupt program status register
IRQ interrupt request
ITM instrumentation trace macrocell
LCD liquid crystal display
LIN Local Interconnect Network, a communications protocol.
LR link register
LUT lookup table
LVD low-voltage detect, see also LVI
LVI low-voltage interrupt, see also HVI
LVTTL low-voltage transistor-transistor logic
MAC multiply-accumulate
MCU microcontroller unit
MISO master-in slave-out
NC no connect
NMI nonmaskable interrupt
NRZ non-return-to-zero
NVIC nested vectored interrupt controller
NVL nonvolatile latch, see also WOL
opamp operational amplifier
PAL programmable array logic, see also PLD
PC program counter
PCB printed circuit board
PGA programmable gain amplifier
PHUB peripheral hub
PHY physical layer
PICU port interrupt control unit
Datasheet 61 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Acronym | Description |
|---|---|
| FPB | flash patch and breakpoint |
| FS | full-speed |
| GPIO | general-purpose input/output, applies to a PSoC pin |
| HVI | high-voltage interrupt, see also LVI, LVD |
| IC | integrated circuit |
| IDAC | current DAC, see also DAC, VDAC |
| IDE | integrated development environment |
| I2C, or IIC | Inter-Integrated Circuit, a communications protocol |
| IIR | infinite impulse response, see also FIR |
| ILO | internal low-speed oscillator, see also IMO |
| IMO | internal main oscillator, see also ILO |
| INL | integral nonlinearity, see also DNL |
| I/O | input/output, see also GPIO, DIO, SIO, USBIO |
| IPOR | initial power-on reset |
| IPSR | interrupt program status register |
| IRQ | interrupt request |
| ITM | instrumentation trace macrocell |
| LCD | liquid crystal display |
| LIN | Local Interconnect Network, a communications protocol. |
| LR | link register |
| LUT | lookup table |
| LVD | low-voltage detect, see also LVI |
| LVI | low-voltage interrupt, see also HVI |
| LVTTL | low-voltage transistor-transistor logic |
| MAC | multiply-accumulate |
| MCU | microcontroller unit |
| MISO | master-in slave-out |
| NC | no connect |
| NMI | nonmaskable interrupt |
| NRZ | non-return-to-zero |
| NVIC | nested vectored interrupt controller |
| NVL | nonvolatile latch, see also WOL |
| opamp | operational amplifier |
| PAL | programmable array logic, see also PLD |
| PC | program counter |
| PCB | printed circuit board |
| PGA | programmable gain amplifier |
| PHUB | peripheral hub |
| PHY | physical layer |
| PICU | port interrupt control unit |

## Page 62

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Acronyms
Table 47 Acronyms used in this document (continued)
Acronym Description
PLA programmable logic array
PLD programmable logic device, see also PAL
PLL phase-locked loop
PMDD package material declaration data sheet
POR power-on reset
PRES precise power-on reset
PRS pseudo random sequence
PS port read data register
PSoC™ Programmable System-on-Chip™
PSRR power supply rejection ratio
PWM pulse-width modulator
RAM random-access memory
RISC reduced-instruction-set computing
RMS root-mean-square
RTC real-time clock
RTL register transfer language
RTR remote transmission request
RX receive
SAR successive approximation register
SC/CT switched capacitor/continuous time
SCL I2C serial clock
SDA I2C serial data
S/H sample and hold
SINAD signal to noise and distortion ratio
SIO special input/output, GPIO with advanced features. See GPIO.
SOC start of conversion
SOF start of frame
SPI Serial Peripheral Interface, a communications protocol
SR slew rate
SRAM static random access memory
SRES software reset
SWD serial wire debug, a test protocol
SWV single-wire viewer
TD transaction descriptor, see also DMA
THD total harmonic distortion
TIA transimpedance amplifier
TRM technical reference manual
TTL transistor-transistor logic
TX transmit
UART Universal Asynchronous Transmitter Receiver, a communications protocol
Datasheet 62 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Acronym | Description |
|---|---|
| PLA | programmable logic array |
| PLD | programmable logic device, see also PAL |
| PLL | phase-locked loop |
| PMDD | package material declaration data sheet |
| POR | power-on reset |
| PRES | precise power-on reset |
| PRS | pseudo random sequence |
| PS | port read data register |
| PSoC™ | Programmable System-on-Chip™ |
| PSRR | power supply rejection ratio |
| PWM | pulse-width modulator |
| RAM | random-access memory |
| RISC | reduced-instruction-set computing |
| RMS | root-mean-square |
| RTC | real-time clock |
| RTL | register transfer language |
| RTR | remote transmission request |
| RX | receive |
| SAR | successive approximation register |
| SC/CT | switched capacitor/continuous time |
| SCL | I2C serial clock |
| SDA | I2C serial data |
| S/H | sample and hold |
| SINAD | signal to noise and distortion ratio |
| SIO | special input/output, GPIO with advanced features. See GPIO. |
| SOC | start of conversion |
| SOF | start of frame |
| SPI | Serial Peripheral Interface, a communications protocol |
| SR | slew rate |
| SRAM | static random access memory |
| SRES | software reset |
| SWD | serial wire debug, a test protocol |
| SWV | single-wire viewer |
| TD | transaction descriptor, see also DMA |
| THD | total harmonic distortion |
| TIA | transimpedance amplifier |
| TRM | technical reference manual |
| TTL | transistor-transistor logic |
| TX | transmit |
| UART | Universal Asynchronous Transmitter Receiver, a communications protocol |

## Page 63

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Acronyms
Table 47 Acronyms used in this document (continued)
Acronym Description
UDB universal digital block
USB Universal Serial Bus
USBIO USB input/output, PSoC pins used to connect to a USB port
VDAC voltage DAC, see also DAC, IDAC
WDT watchdog timer
WOL write once latch, see also NVL
WRES watchdog timer reset
XRES external reset I/O pin
XTAL crystal
Datasheet 63 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Acronym | Description |
|---|---|
| UDB | universal digital block |
| USB | Universal Serial Bus |
| USBIO | USB input/output, PSoC pins used to connect to a USB port |
| VDAC | voltage DAC, see also DAC, IDAC |
| WDT | watchdog timer |
| WOL | write once latch, see also NVL |
| WRES | watchdog timer reset |
| XRES | external reset I/O pin |
| XTAL | crystal |

## Page 64

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Document conventions
10 Document conventions
10.1 Units of measure
Table 48 Units of measure
Symbol Unit of measure
°C degrees Celsius
dB decibel
fF femto farad
Hz hertz
KB 1024 bytes
kbps kilobits per second
Khr kilohour
kHz kilohertz
k kilo ohm
ksps kilosamples per second
LSB least significant bit
Mbps megabits per second
MHz megahertz
M mega-ohm
Msps megasamples per second
µA microampere
µF microfarad
µH microhenry
µs microsecond
µV microvolt
µW microwatt
mA milliampere
ms millisecond
mV millivolt
nA nanoampere
ns nanosecond
nV nanovolt
 ohm
pF picofarad
ppm parts per million
ps picosecond
s second
sps samples per second
sqrtHz square root of hertz
V volt
Datasheet 64 002-22097 Rev. *F
2023-11-16
```

## Page 65

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Revision history
Revision history
Document
Date Description of changes
revision
** 2018-01-30 New spec.
Updated Functional definition:
Updated Analog blocks:
Updated VDAC (13 bits):
Updated description.
*A 2018-04-27
Updated Electrical specifications:
Updated Analog peripherals:
Updated Voltage DAC:
Updated Table12.
Updated Ordering information:
*B 2018-05-03 No change in part numbers.
Fixed typo.
Updated Electrical specifications:
Updated Device Level Specifications:
Updated Table4.
Updated XRES:
Updated Table8.
Updated Analog peripherals:
Updated CTB Opamp:
Updated Table10.
Updated Voltage DAC:
Updated Table12.
*C 2018-09-25
Updated Memory:
Updated Flash:
Updated Table29.
Updated System resources:
Updated External Clock:
Updated Table38.
Updated Packaging:
Updated Package diagrams:
Removed spec 002-10531 Rev. **.
Added spec 002-24003 Rev. **.
Updated Electrical specifications:
Updated Device Level Specifications:
Updated description.
Updated Memory:
Updated Flash:
*D 2019-12-06 Updated Table29.
Updated Ordering information:
Updated Table41 (Updated part numbers).
Updated Packaging:
Updated Table44.
Updated to new template.
Datasheet 65 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Date |
|---|
| 2018-01-30 |
| 2018-04-27 |
| 2018-05-03 |
| 2018-09-25 |
| 2019-12-06 |

## Page 66

### Raw Page Text

```text
PSoC™ 4100PS
Based on Arm® Cortex™-M0+
Revision history
Document
Date Description of changes
revision
Updated Electrical specifications:
Updated System resources:
Updated Power-on Reset (POR):
Updated Table30.
*E 2020-12-17
Updated Packaging:
Updated Package diagrams:
spec 51-85079 - Changed revision from *F to *G.
Updated to new template.
Updated Document Title to read as “CY8C41x5, PSoC™ 4100PS Based on
Arm® Cortex™-M0+”.
Updated More information:
Updated description.
Updated hyperlinks.
Updated PSoC™ Creator:
Updated hyperlinks.
*F 2023-11-16 Updated Development support:
Updated hyperlinks.
Updated Packaging:
Updated Package diagrams:
No change in revisions.
Added Note below spec 001-57280 *E.
Migrated to Infineon template.
Completing Sunset Review.
Datasheet 66 002-22097 Rev. *F
2023-11-16
```

### Extracted Tables

#### Table 1

| Date |
|---|
| 2020-12-17 |
| 2023-11-16 |

## Page 67

### Raw Page Text

```text
Please read the Important Notice and Warnings at the end of this document
Trademarks
All referenced product or service names and trademarks are the property of their respective owners.
IMPORTANT NOTICE WARNINGS
Edition 2023-11-16 The information given in this document shall in no Due to technical requirements products may contain
event be regarded as a guarantee of conditions or dangerous substances. For information on the types
Published by characteristics (“Beschaffenheitsgarantie”). in question please contact your nearest Infineon
Technologies office.
Infineon Technologies AG With respect to any examples, hints or any typical
values stated herein and/or any information Except as otherwise explicitly approved by Infineon
81726 Munich, Germany regarding the application of the product, Infineon Technologies in a written document signed by
Technologies hereby disclaims any and all authorized representatives of Infineon
warranties and liabilities of any kind, including Technologies, Infineon Technologies’ products may
without limitation warranties of non-infringement of not be used in any applications where a failure of the
intellectual property rights of any third party. product or any consequences of the use thereof can
© 2023 Infineon Technologies AG.
reasonably be expected to result in personal injury.
All Rights Reserved.
In addition, any information given in this document
is subject to customer’s compliance with its
Do you have a question about this obligations stated in this document and any
applicable legal requirements, norms and standards
document?
concerning customer’s products and any use of the
Email: product of Infineon Technologies in customer’s
applications.
erratum@infineon.com
The data contained in this document is exclusively
Document reference intended for technically trained staff. It is the
responsibility of customer’s technical departments
002-22097 Rev. *F to evaluate the suitability of the product for the
intended application and the completeness of the
product information given in this document with
respect to such application.
```
