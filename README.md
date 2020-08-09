# tek_7k_ext
Tektronix 7000 oscilloscope plug-in extender.

Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)\
*This project is free, you may do whatever you want with it.*

## Purpose and Prerequisites

This extender is intended to facilitate calibration and repair of Tektronix 7000 oscilloscope plug-ins. 
It consists of 2 PCBs: 1) An edge connector PCB for connecting with the 7000 series oscilloscope. 
It has extra (optional) connectors for power supplies, this is to provide a controlled environment 
(use lab supplies) to debug/repair plug-ins with PSU issues (short-circuit for instance). These
can also be used to check the voltages provided by the scope mainframe. 2) A backplate PCB for connecting 
with the plug-ins. Each of the 76 pins has a probing pad, these are spaced with a 2.54mm (0.1") pitch,
hence standard pin headers can be fitted. The two PCBs are to be connected using 24 or 
26AWG ribbon cables. If RF performance is required, coaxial cables (RG174 for example) should be used for 
the signal pins.

A good overview of the 7000 oscilloscope's plug-in interface can be found at 
[TekWiki](http://w140.com/tekwiki/wiki/7000_Series_plug-in_interface). However, the information 
is somewhat dispersed otherwise, there isn't a single Tektronix document summarizing everything. 
In particular, various models of the 7000 series implement additional features or omit some. 
Notably, the 76xx scopes don't supply the +5V for button lights. It is hence recommended to have at hand 
copies of the service manuals of the oscilloscope and plug-ins pair to calibrate/repair. 
Finally, note that the plug-ins are supplied with both -50VDC and +50VDC! Please exercise caution.

## How to make the PCBs

Some "ready to use" gerbers are available: [gerbers/tek_7k_ext-gerber.zip](./gerbers/tek_7k_ext-gerber.zip) 
(edge connector PCB) and [gerbers/tek_7k_ext_back-gerber.zip](./gerbers/tek_7k_ext_back-gerber.zip) (backplate PCB). 
They should work with any PCB fab. With [JLCPCB](http://www.jlcpcb.com), they're quoted at around 20 euros + shipping 
for 5 pieces of each. Please be sure to select "gold fingers" and "45 degrees" chamfered fingers for the edge connector PCB. 
If the gerbers needed modification for a specific PCB fab, please share them on this repository so everybody can benefit.

The complete Kicad projects are available: [kicad/tek_7k_ext.zip](./kicad/tek_7k_ext.zip) (edge connector)
and [kicad/tek_7k_ext_back.zip](./kicad/tek_7k_ext_back.zip) (backplate).
You will need [pointhi/kicad-footprint-generator](http://github.com/pointhi/kicad-footprint-generator) 
for running the Python footprint generation [scripts](./scripts).

You can actually do without the backplate PCB by soldering directly to a 2.54mm (0.1") pitch 76 pins edge card connector.
EDAC makes such connector with soldering eyelets, part number is **EDAC 345-076-500-201**. However, using the proposed 
backplate should be more convenient in the long run.

## Assembly

It is recommended that you build at least 2 extenders as some plug-ins (spectrum analyzers notably) make use of 2 slots.

Please first have a quick look at the schematics: [tek_7k_ext.pdf](./tek_7k_ext.pdf) and [tek_7k_ext_back.pdf](./tek_7k_ext_back.pdf),
along with the *BOM/Parts needed* section at the end of this document. Pins/pads are numbered from bottom to top. Looking from the front 
of the oscilloscope to the back of it, left is 'A' and right is 'B'. High-frequency signal pins are **11A**, **11B**, **13A**, **13B**,
**20A**, and **20B**. On each PCB, there are 6 dedicated *GND* pads for coaxial cables shield grounding.

First solder the 76 pins card edge connector on the backplate. Then solder the wires between the edge connector and the backplate PCBs.
*Match* each pin between the 2 PCBs. On the backplate, solder to the pads closest to the center, the outer ones being the probing pads 
(they have larger drill holes). You may use 24 or 26AWG ribbon cable. If RF performance is required (for calibrating or repairing 
high-frequency plug-ins), then use coxial cables (RG174 for example) to connect the signal pins. Be sure to ground the shield of the 
coaxial cables with the provided grounding pads (6 of them per PCB).

You may fit the extra power supply connectors on the edge connector PCB. This can come handy for debugging a plug-in with a short or 
PSU issues. Depending on your debugging/repair needs, you may solder extra wire(s) on the probing pad(s) or fit them with 2.54mm pin
headers.

## Usage

* As a "simple" extender (calibration of plug-ins for instance), just plug-and-play! If the connected plug-in is high-frequency, then 
coxial cables must have been used for the signal pins.

* For further debugging/repair:
   - Populate the power supply connectors on the edge connector PCB, or use the equivalent probing pads on the backplate PCB. Then 
   use lab supplies to "run" the faulty plug-in in a controlled environment;
   - Solder wire(s) or fit pin headers on the backplate PCB's probing pads as needed. Using headers can be handy if you regularly 
   probe some specific pins.
      
## BOM/Parts needed

For wiring, use 24 or 26AWG 2.54mm (0.1") ribbon cable, this will make soldering/assembly easier and faster. Ribbon cable
may be a little difficult to source but they're still manufactured. For coaxial cable, use good quality RG174 for instance, 
they're much thinner than RG58 and hence probably better suited for our purpose. 50cm or 20" should be an appropriate length 
for the cables.

### Edge connector PCB

| Symbol(s) | Name & Description | Part number | Quantity |
| --- | --- | --- | --- |
| | **_Parts below optional_** | | | |
| J4, J5 | PCB header, 2.54mm pitch, 3 circuits | Molex 22-23-2031 | 2 | 
| | Crimp housing, 2.54mm pitch, 3 circuits | Molex 22-01-3037 | 2 | 
| J6, J7 | Vertical PCB header, 2.54mm pitch, 2 circuits | Molex 22-23-2021 | 2 |
| | Crimp housing, 2.54mm pitch, 2 circuits | Molex 22-01-3027 | 2 |

### Backplate PCB

| Symbol(s) | Name & Description | Part number | Quantity |
| --- | --- | --- | --- |
| J1 | 76 pins 2.54mm (0.1") pitch card edge connector | EDAC 345-076-520-201 | 1 |
| | **_Parts below optional, use as needed_** | | | |
|  | pin header, 2.54mm pitch | Harwin M20-9992046 (cut to size) |  |
|  | 2.54mm pitch SIL housing | Harwin M20-1060200 (various number of position(s) available) |  |

## Revision history and status

* **_Version 1.2_** README.md added, probing pads enlarged.
  - Probing pads modified to have larger drill size (1mm) so standard 2.54mm pin headers can be fitted;
  - Still no prototypes made, no validation yet.

* **_Version 1.1_** Public release on github, no README.md. 
  - Modified the soldering pads dimensions so that the card edge connector will hopefully fit and the soldering of ribbon cable is easier;
  - Cleaned-up the Python scripts;
  - Prototypes need to be made to validate.

* **_Version 1.0_** First completed gerbers for both the edge connector and backplate PCBs, prototypes made by JLCPB.
  - The backplate is a complete failure, nothing salvageable. Pads for the EDAC card edge connector pads have no tolerance, can't even fit on PCB.
  - The soldering pads are also too tight, it's extremely difficult (but not impossible) to fit ribbon cables and then solder.
