# conn_pads_tek_7k.py
# Footprints for wire pads to connect Tektronix 7000 scope extender.
#
# Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)
# This code is free, you may do whatever you want with it.

import sys
sys.path.append("..")

from KicadModTree import *
from KicadFootprintCommon import *

PITCH           	= inch_to_mm(.1)
PAD_SIZE        	= 1.75
DRILL_SIZE_FRONT	= .7
DRILL_SIZE_BACK      	= 1
TEXT_OFFSET		= .12
HEIGHT 			= 38 * PITCH
WIDTH 			= PAD_SIZE + 4

def create_wire_pads (name, is_left, is_front):

	module = Footprint(name)
	module.setDescription(
		"Pads for one side (" 
		+ ("left, " if is_left else "right, ")
		+ ("front" if is_front else "back")
		+ ") of Tektronix 7000 scope extender.")

	center = -WIDTH / 2 + PAD_SIZE / 2 + .3
	if not is_left:
		center = -center
	add_rectangle(module, center, 0, WIDTH, HEIGHT, "F.CrtYd")

    	top = -(19 * PITCH - PITCH / 2)
	module.append(Text(
		type = "reference",
		text = "REF**",
		at = [center, top - PITCH],
		layer = "Cmts.User"))
	module.append(Text(
		type = "value",
		text = name,
		at = [center, -top + PITCH],
		layer = "Cmts.User"))
	
	letter = 'A' if is_left else 'B'
	x = inch_to_mm(-TEXT_OFFSET if is_left else TEXT_OFFSET)
	drill_size = DRILL_SIZE_FRONT if is_front else DRILL_SIZE_BACK
    	for i in range(0, 38):
		y = top + i * PITCH
		add_circular_tht_pad(
			module, str(38 - i), 
			0, y,
			PAD_SIZE, drill_size);
		module.append(Text(
			type = "user", 
			text = str(38 - i) + letter, 
			at = [x, y],
			mirror = not is_front,
			layer = "F.SilkS" if is_front else "B.SilkS")) 

	return module

if __name__ == "__main__":

	name = "Connector_Pads_Front_A_Tek_7k"
        file_handler = KicadFileHandler(create_wire_pads(name, True, True))
        file_handler.writeFile("footprints/" + name + ".kicad_mod")

	name = "Connector_Pads_Front_B_Tek_7k"
        file_handler = KicadFileHandler(create_wire_pads(name, False, True))
        file_handler.writeFile("footprints/" + name + ".kicad_mod")

	name = "Connector_Pads_Back_A_Tek_7k"
        file_handler = KicadFileHandler(create_wire_pads(name, True, False))
        file_handler.writeFile("footprints/" + name + ".kicad_mod")

	name = "Connector_Pads_Back_B_Tek_7k"
        file_handler = KicadFileHandler(create_wire_pads(name, False, False))
        file_handler.writeFile("footprints/" + name + ".kicad_mod")
