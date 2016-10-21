#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the show plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Show(OpenCVPlugin):
    """
    Show plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.title = "My Image"
        self.window_type = "Image Size"

        self.help = "Mostra uma imagem da cadeia de processamento de imagens."

        self.description = {
            "Label": "Show Image",
            "Icon": "images/show.png",
            "Color": "50:100:200:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {},
            "TreeGroup": "General"
        }

        self.properties = {
            "title": {
                "name": "Window Title",
                "type": HARPIA_STRING
            },
            "window_type": {
                "name": "Window Type",
                "type": HARPIA_COMBO,
                "values": ["Window Size", "Image Size", "Resizable Window"]
            }
        }

        # -------------------C/OpenCv code------------------------------------

    # -------------------------------------------------------------------------
    def generate_vars(self):
        code = OpenCVPlugin.generate_vars(self)
        if self.window_type == "Window Size":
            code += 'cvNamedWindow("$title$",CV_WINDOW_NORMAL);\n'
        elif self.window_type == "Resizable Window":
            code += 'cvNamedWindow("$title$",CV_WINDOW_NORMAL);\n'
        else:
            code += 'cvNamedWindow("$title$",CV_WINDOW_AUTOSIZE);\n'
        return code

    # -------------------------------------------------------------------------
    def generate_function_call(self):
        code = '\nif(block$id$_img_i0){\n' + \
            'cvShowImage("$title$",block$id$_img_i0);\n'
        if self.window_type == "Window Size":
            code += 'cvSetWindowProperty("$title$", ' + \
                'CV_WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN);\n'
        code += '}\n'
        return code

# -----------------------------------------------------------------------------
