#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the newRect plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class NewRect(OpenCVPlugin):
    """
    newRect plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.x0 = 0
        self.y0 = 0
        self.width = 640
        self.height = 480

        self.help = "Creates new rectangle"

        self.description = {
            'Label': 'New Rectangle',
            'Icon': 'images/newRect.png',
            'Color': '50:50:200:150',
            'InTypes': "",
            'OutTypes': {0: 'HRP_RECT'},
            'TreeGroup': 'Basic Data Type'
        }

        self.properties = {
            "x0": {
                "name": "X",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
            "y0": {
                "name": "Y",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
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
            'block$id$_rect_o0 = cvRect($x0$, $y0$, $width$, $height$);\n'

# -----------------------------------------------------------------------------
