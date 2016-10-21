#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the subtraction plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Subtraction(OpenCVPlugin):
    """
    Subtraction plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

        self.help = "Realiza a subtração de duas imagens."

        self.description = {
            "Label": "Subtraction",
            "Icon": "images/subtraction.png",
            "Color": "180:10:10:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Arithmetic and logical operations"
        }

        # -------------------C/OpenCv code------------------------------------
        self.function_call = \
            'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'adjust_images_size(block$id$_img_i0, ' + \
            'block$id$_img_i1, block$id$_img_o0);\n' + \
            'cvSub(block$id$_img_i0, ' + \
            'block$id$_img_i1, block$id$_img_o0,0);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
