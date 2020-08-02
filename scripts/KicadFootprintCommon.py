# KicadFootprintCommon.py
# Common functions for Kicad footprint generation.
#
# Copyright (C) 2020 Lin Ke-Fong (anotherlin@gmail.com)
# This code is free, you may do whatever you want with it.

from KicadModTree import *

def inch_to_mm (x):
        return x * 25.4

def add_circular_tht_pad (module, name, x, y, pad_size, drill_size):
	module.append(Pad(
		number = name,
                type = Pad.TYPE_THT,
                shape = Pad.SHAPE_CIRCLE,
		layers = Pad.LAYERS_THT,
                at = [x, y],
                size = pad_size,
		drill = drill_size))

def add_rectangle (module, x, y, width, height, layer, offset = 0):
	module.append(RectLine(
		start = [-width / 2 + x, -height / 2 + y],
                end = [width / 2 + x, height / 2 + y],
                layer = layer,
		offset = offset))
