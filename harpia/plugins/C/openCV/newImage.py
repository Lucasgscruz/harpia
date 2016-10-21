#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the newImage plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class NewImage(OpenCVPlugin):
    """
    NewImage plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.width = "640"
        self.height = "480"

        self.help = "Cria uma nova imagem."

        self.description = {
            "Label": "New Image",
            "Icon": "images/acquisition.png",
            "Color": "50:100:200:150",
            "InTypes": "",
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Image Source"
        }

        self.properties = {
            "width": {
                "name": "Width",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
            "height": {
                "name": "Height",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.function_call = \
            'CvSize size$id$ = cvSize($width$,$height$);\n' + \
            'block$id$_img_o0 = cvCreateImage(size$id$,IPL_DEPTH_8U,3);\n' + \
            'cvSetZero(block$id$_img_o0);\n'

# ------------------------------------------------------------------------------
