#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the circle plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Circle(OpenCVPlugin):
    """
    Circle plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.x0 = 100
        self.y0 = 100
        self.color = "#0000ffff0000"

        self.help = "Desenha Circulos."

        self.description = {
            "Label": "Circle",
            "Icon": "images/opening.png",
            "Color": "255:0:0:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_INT", 2: "HRP_INT"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Basic Shapes"
        }

        self.properties = {
            "x0": {
                "name": "x0",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 800,
                "step": 1
            },
            "y0": {
                "name": "y0",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 1000,
                "step": 1
            },
            "color": {
                "name": "Color",
                "type": HARPIA_COLOR
            }
        }

        # -----------------C/OpenCv code ---------------------------
        self.vars = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'int block$id$_int_i1 = $x0$;\n' + \
            'int block$id$_int_i2 = $y0$;\n'

    # ----------------------------------------------------------------------
    def generate_vars(self):
        self.x0 = int(self.x0)
        self.y0 = int(self.y0)

        return self.vars

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        # -------------define RGB---------------
        red = self.color[1:5]
        green = self.color[5:9]
        blue = self.color[9:13]

        red = int(red, 16) / 257
        green = int(green, 16) / 257
        blue = int(blue, 16) / 257

        return \
            '\nif(block$id$_img_i0){\n' + \
            'CvPoint center = cvPoint' + \
            '(block$id$_int_i1, block$id$_int_i2);\n' + \
            'CvScalar color = cvScalar(' + str(blue) + ',' + str(green) + \
            ',' + str(red) + ',0);\n' + \
            'cvCircle(block$id$_img_i0, center, 10, color, 1, 8, 0);\n' +\
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            '}\n'

# ------------------------------------------------------------------------------
