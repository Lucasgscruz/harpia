#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the save plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Save(OpenCVPlugin):
    """
    Save plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.filename = ""

        self.help = "Salva uma imagem em uma mídia indicada pelo usuário." + \
            "Atualmente a imagem é salva como PNG por padrão."

        self.description = {
            "Label": "Save Image",
            "Icon": "images/save.png",
            "Color": "50:100:200:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "General"
        }

        self.properties = {
            "filename": {
                "name": "File Name",
                "type": HARPIA_SAVE_FILE
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.function_call = \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'if(block$id$_img_i0)\n' + \
            'cvSaveImage("$filename$" ,block$id$_img_i0);\n'

# -----------------------------------------------------------------------------
