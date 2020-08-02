# conn_card_edge_tek_7k.py
# Footprint for EDAC 345-076-520-201 76 pins .1" pitch edge connector.
#
# Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)
# This code is free, you may do whatever you want with it.

import sys
sys.path.append("..")

from KicadModTree import *
from KicadFootprintCommon import *

NAME 		= "Connector_Card_Edge_Tek_7k"
PITCH 		= inch_to_mm(.1)
PAD_SIZE 	= [1.75, 1.75]
DRILL_SIZE 	= [inch_to_mm(.018 + .006), inch_to_mm(.03 + .006)]
HEIGHT 		= inch_to_mm(4.06)
WIDTH 		= inch_to_mm(.37)

def create_card_edge_connector ():

	module = Footprint(NAME) 
	module.setDescription(
		"Card edge connector for Tektronix 7000 scope plug-in.")

	add_rectangle(module, 0, 0, WIDTH, HEIGHT, "F.CrtYd")

	module.append(Text(
		type = "reference",
		text = "REF**",
		at = [0, -9 * PITCH], 
		rotation = 90,
		layer = "Cmts.User"))
    	module.append(Text(
		type = "value",
		text = NAME,
		at = [0, 9 * PITCH],
		rotation = 90,
		layer = "Cmts.User"))
    	module.append(Text(
		type = "user",
		text = "EDAC 345-076-520-201",
		at = [0, 0],
		rotation = 90))

    	top = -(19 * PITCH - PITCH / 2)
    	for i in range(0, 38):
		y = top + i * PITCH
		pad_name = str(38 - i) + 'A'
		add_circular_tht_pad(
			module, pad_name, 
			-PITCH, y, 
			PAD_SIZE, DRILL_SIZE)
		pad_name = str(38 - i) + 'B'
		add_circular_tht_pad(
			module, pad_name, 
			PITCH, y, 
			PAD_SIZE, DRILL_SIZE)

	add_rectangle(module, 0, 0, WIDTH, HEIGHT, "F.SilkS", -0.24)

	return module
    
if __name__ == "__main__":

	file_handler = KicadFileHandler(create_card_edge_connector())
	file_handler.writeFile("footprints/" + NAME + ".kicad_mod")
