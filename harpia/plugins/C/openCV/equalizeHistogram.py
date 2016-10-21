#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the equalizeHistogram plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class EqualizeHistogram(OpenCVPlugin):
    """
    EqualizeHistogram plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

        self.help = "A equalização do histograma de uma imagem visa " + \
            "alcançar maior contraste entre os " + \
            "diversos elementos de uma imagem."

        self.description = {
            "Label": "Equalize Histogram",
            "Icon": "images/equalizeHistogram.png",
            "Color": "0:0:0:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Histograms"
        }

        # -------------------C/OpenCv code-------------------------------------
        self.vars =  \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_SourceCx[3];\n' + \
            'IplImage * block$id$_EqCx[3];\n'

        self.function_call = \
            '\nif(block$id$_img_i0){\n' + \
            'CvSize size$id$ = cvGetSize(block$id$_img_i0);\n' + \
            'block$id$_img_o0 = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 3);\n' + \
            'block$id$_SourceCx[0] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_SourceCx[1] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_SourceCx[2] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[0] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[1] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[2] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'cvSplit(block$id$_img_i0, block$id$_SourceCx[0],' + \
            'block$id$_SourceCx[1],block$id$_SourceCx[2], NULL);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[0], block$id$_EqCx[0]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[1], block$id$_EqCx[1]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[2], block$id$_EqCx[2]);\n' + \
            'cvMerge( block$id$_EqCx[0],block$id$_EqCx[1],' + \
            'block$id$_EqCx[2], NULL,block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[0]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[1]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[2]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[0]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[1]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[2]);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
