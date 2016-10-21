#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the not plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Not(OpenCVPlugin):
    """
    Not plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

        self.help = "Realiza a negação lógica de uma imagem. " + \
            "Corresponde à negativa da imagem."

        self.description = {
            "Label": "Not",
            "Icon": "images/not.png",
            "Color": "10:180:10:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Arithmetic and logical operations"
        }

        # -------------------C/OpenCv code------------------------------------
        self.function_call = \
            'if(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'cvNot(block$id$_img_i0, block$id$_img_o0);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
