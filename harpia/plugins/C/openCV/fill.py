#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the fill plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Fill(OpenCVPlugin):
    """
    Module containing the Fill plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.color = "#0000ffff0000"

        self.help = "Preenche toda a imagem de uma cor."

        self.description = {
            "Label": "Fill image",
            "Icon": "images/fill.png",
            "Color": "50:100:200:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "General"
        }

        self.properties = {
            "color": {
                "name": "Color",
                "type": HARPIA_COLOR
            }
        }

        # ------------------------------C/OpenCv code--------------------------

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        # --------define RGB-------------
        red = self.color[1:5]
        green = self.color[5:9]
        blue = self.color[9:13]

        red = int(red, 16) / 257
        green = int(green, 16) / 257
        blue = int(blue, 16) / 257

        return \
            'if(block$id$_img_i0){\n' + \
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            '\tCvScalar color = cvScalar' + \
            '(' + str(blue) + ',' + str(green) + ',' + str(red) + ',0);\n' + \
            '\tcvSet(block$id$_img_o0, color, NULL);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
