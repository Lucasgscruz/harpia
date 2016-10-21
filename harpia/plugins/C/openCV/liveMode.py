#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the liveMode plugin class.
"""

import os
from glob import glob
from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class LiveMode(OpenCVPlugin):
    """
    LiveMode plugin class.
    """

    # --------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.camera = "/dev/video0"

        self.help = "Realiza a aquisição de uma imagem a partir de câmera."

        self.description = {
            "Label": "Live Mode",
            "Icon": "images/acquisition.png",
            "Color": "50:100:200:150",
            "InTypes": "",
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Image Source"
        }

        # ------------------------------C/OpenCv code--------------------------
        self.function_call = \
            '// Live Mode \n' + \
            'int value = cvGrabFrame(block$id$_capture);\n' + \
            'block$id$_frame = cvRetrieveFrame(block$id$_capture);\n' + \
            'if(!block$id$_frame){\ncontinue;\n}\n' +\
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_frame);\n'

        self.out_dealloc = 'cvReleaseCapture(&block$id$_capture);\n'

    # ----------------------------------------------------------------------
    def get_properties(self):

        available_cams = 4
        device_list = []

        if os.name == 'posix':
            device_list = glob("/dev/video*")

        return {
            "camera": {
                "name": "Camera",
                "type": HARPIA_COMBO,
                "values": device_list
            }
        }

    # ----------------------------------------------------------------------
    def generate_vars(self):
        camera = self.camera[10:]

        return \
            '// Live Mode Cam \n' + \
            'CvCapture * block$id$_capture = NULL;\n' + \
            'block$id$_capture = cvCaptureFromCAM(' + camera + ');\n' + \
            'IplImage * block$id$_frame = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n'

# ------------------------------------------------------------------------------
