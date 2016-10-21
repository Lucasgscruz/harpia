#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the pow plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Pow(OpenCVPlugin):
    """
    Pow plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.exponent = 1

        self.help = "Eleva cada ponto de uma " + \
            "imagem a um valor fixo de potência."

        self.description = {
            "Label": "Pow",
            "Icon": "images/pow.png",
            "Color": "230:230:60:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Math Functions"
        }

        self.properties = {
            "exponent": {
                "name": "Exponent",
                "type": HARPIA_INT,
                "lower": 1,
                "upper": 10,
                "step": 1
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.vars = ""

        self.function_call = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'cvPow(block$id$_img_i0, block$id$_img_o0, $exponent$);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
