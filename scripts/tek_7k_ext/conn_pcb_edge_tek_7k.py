# conn_pcb_edge_tek_7k.py
# 76 pins .1" (2.54mm) pitch PCB edge connector for Tektronix 7000 extender.
#
# Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)
# This code is free, you may do whatever you want with it.

import sys
sys.path.append("..")

from KicadModTree import *
from KicadFootprintCommon import *

NAME		= "Connector_PCB_Edge_Tek_7k"
PITCH 		= inch_to_mm(.1)
WIDTH 		= inch_to_mm(.35)
HEIGHT		= 38 * PITCH
PAD_SIZE 	= [WIDTH, inch_to_mm(.055)]

# JLCPCB requires a 1.2mm margin for the 45 degrees bevel. The actual Tektronix
# plug-ins don't have chamfer on the PCB edge connector, so you can set this 
# constant to zero.
BEVEL_SIZE	= 1.2

def create_pcb_edge_connector ():

	module = Footprint(NAME)
	module.setDescription(
		"PCB edge connector for Tektronix 7000 extender.")

	width = WIDTH + BEVEL_SIZE
	add_rectangle(module, BEVEL_SIZE / 2, 0, width, HEIGHT, "F.CrtYd")

    	top = -(19 * PITCH - PITCH / 2)
	module.append(Text(
		type = "reference",
		text = "REF**",
		at = [BEVEL_SIZE / 2, top - PITCH],
		layer = "Cmts.User"))
    	module.append(Text(
		type = "value",
		text = NAME,
		at = [BEVEL_SIZE / 2, -top + PITCH],
		layer = "Cmts.User"))

    	for i in range(0, 38):
		y = top + i * PITCH
		module.append(Pad(
			number = str(38 - i) + 'A',
			type = Pad.TYPE_SMT,
			shape = Pad.SHAPE_RECT, 
			at = [0, y],
			size = PAD_SIZE,
			layers = ['B.Cu', 'B.Mask']))
		module.append(Pad(
			number = str(38 - i) + 'B',
			type = Pad.TYPE_SMT,
			shape = Pad.SHAPE_RECT,
			at = [0, y],
			size = PAD_SIZE,
			layers = ['F.Cu', 'F.Mask']))

	module.append(Polygon(
		nodes = [ [-WIDTH / 2, -HEIGHT / 2],
			[-WIDTH / 2, HEIGHT / 2],
			[WIDTH / 2 + BEVEL_SIZE, HEIGHT / 2],
			[WIDTH / 2 + BEVEL_SIZE, -HEIGHT / 2] ],
		layer = "F.Mask"))
	module.append(Polygon(
		nodes = [ [-WIDTH / 2, -HEIGHT / 2],
			[-WIDTH / 2, HEIGHT / 2],
			[WIDTH / 2 + BEVEL_SIZE, HEIGHT / 2],
			[WIDTH / 2 + BEVEL_SIZE, -HEIGHT / 2] ],
		layer = "B.Mask"))

	return module
    
if __name__ == "__main__":

        file_handler = KicadFileHandler(create_pcb_edge_connector())
        file_handler.writeFile("footprints/" + NAME + ".kicad_mod")
