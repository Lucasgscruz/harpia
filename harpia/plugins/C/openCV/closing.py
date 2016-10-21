#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the closing plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Closing(OpenCVPlugin):
    """
    Closing plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.masksize = "7x7"

        self.help = "Operação de morfologia matemática para realizar o " + \
            "fechamento da imagem de acordo com o elemento estruturante." + \
            "Equivale a aplicação de uma dilatação seguida de uma erosão."

        self.description = {
            "Label": "Closing",
            "Icon": "images/closing.png",
            "Color": "180:230:220:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_INT", 2: "HRP_INT"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Morphological Operations"
        }

        self.properties = {
            "masksize": {"name": "Mask Size",
                         "type": HARPIA_COMBO,
                         "values": ["1x1", "3x3", "5x5", "7x7"]
                         }
        }

        # -------------------C/OpenCv code---------------------------------
        self.vars = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'int block$id$_int_i1 = ' + self.masksize[0] + ';\n' + \
            'int block$id$_int_i2 = ' + self.masksize[2] + ';\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplConvKernel * block$id$_arg_mask = NULL;\n'

        self.function_call = \
            '\nif(block$id$_img_i0){\n' + \
            'if (block$id$_int_i1 % 2 == 0) block$id$_int_i1++;\n' + \
            'if (block$id$_int_i2 % 2 == 0) block$id$_int_i2++;\n' + \
            'block$id$_arg_mask = ' + \
            'cvCreateStructuringElementEx(block$id$_int_i1 ,' + \
            'block$id$_int_i2, 1, 1,CV_SHAPE_RECT,NULL);\n' + \
            'IplImage * block$id$_auxImg;\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'block$id$_auxImg = cvCloneImage(block$id$_img_i0);\n' + \
            'cvMorphologyEx(block$id$_img_i0, block$id$_img_o0, NULL,' + \
            'block$id$_arg_mask, CV_MOP_CLOSE, 1);\n}\n'

        self.dealloc = \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseStructuringElement(&block$id$_arg_mask);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n'

# --------------------------------------------------------------------------
