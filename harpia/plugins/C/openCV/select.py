#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the select plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Select(OpenCVPlugin):
    """
    Select plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.key = "a"

        self.help = "Select between two images."

        self.properties = {
            "key": {
                "name": "Key",
                "type": HARPIA_STRING,
                "maxlength": 1
            }
        }

        self.description = {
            "Label": "Select",
            "Icon": "images/select.png",
            "Color": "50:100:200:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "General"
        }

        # -------------------C/OpenCv code------------------------------------
        self.vars = 'char block$id$_key = \'$key$\';\n'

        self.function_call = 'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'if (key != -1)\n' + \
            '\tblock$id$_key = key;\n' + \
            'if (block$id$_key == \'$key$\' )\n' + \
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'else\n' + \
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i1);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
