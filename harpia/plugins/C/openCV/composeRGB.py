#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the composeRGB plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class ComposeRGB(OpenCVPlugin):
    """
    ComposeRGB plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

        self.help = "BLOCO Composição RGB"

        self.description = {
            "Label": "Compose RGB",
            "Icon": "images/composeRGB.png",
            "Color": "50:125:50:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE", 2: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Filters and Color Conversion"
        }

        # ------------------------C/OpenCv code-------------------------------
        self.vars = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_i1 = NULL;\n' + \
            'IplImage * block$id$_img_i2 = NULL;\n' + \
            'IplImage * block$id$_img_t0 = NULL;\n' + \
            'IplImage * block$id$_img_t1 = NULL;\n' + \
            'IplImage * block$id$_img_t2 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n'

        self.function_call = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'CvSize size$id$ = cvSize' + \
            '(block$id$_img_i0->width,block$id$_img_i0->height);\n' + \
            'block$id$_img_t0 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'block$id$_img_t1 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'block$id$_img_t2 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'cvSplit(block$id$_img_i0 ,' + \
            'block$id$_img_t0  ,NULL, NULL , NULL);\n' + \
            'cvSplit(block$id$_img_i1 ,' + \
            'NULL ,block$id$_img_t1, NULL, NULL);\n' + \
            'cvSplit(block$id$_img_i2 ,' + \
            'NULL ,NULL, block$id$_img_t2 , NULL);\n' + \
            'cvMerge(block$id$_img_t2 ,block$id$_img_t1 ,' + \
            'block$id$_img_t0 , NULL, block$id$_img_o0);}\n'

        self.dealloc = \
            'cvReleaseImage(&block$id$_img_t0);\n' + \
            'cvReleaseImage(&block$id$_img_t1);\n' + \
            'cvReleaseImage(&block$id$_img_t2);\n' + \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_i1);\n' + \
            'cvReleaseImage(&block$id$_img_i2);\n'

# -----------------------------------------------------------------------------
