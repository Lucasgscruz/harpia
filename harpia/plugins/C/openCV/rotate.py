#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the rotate plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Rotate(OpenCVPlugin):
    """
    Rotate plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.isCenter = True
        self.isScalling = True
        self.isFilling = True
        self.xC = 20
        self.yC = 20
        self.angle = 0

        self.help = "Rotates input image the input angle degrees."

        self.description = {
            "Label": "Rotate Image",
            "Icon": "images/rotate.png",
            "Color": "90:5:10:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_DOUBLE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Experimental"
        }

        self.properties = {
            "isCenter": {
                "name": "Use Image Center",
                "type": HARPIA_CHECK
            },
            "isScalling": {
                "name": "Resize Image To Fit In",
                "type": HARPIA_CHECK
            },
            "isFilling": {
                "name": "Fill Leftovers",
                "type": HARPIA_CHECK
            },
            "xC": {
                "name": "Point X",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
            "yC": {
                "name": "Point Y",
                "type": HARPIA_INT,
                "lower": 0,
                "upper": 65535,
                "step": 1
            },
            "angle": {
                "name": "Angle",
                "type": HARPIA_FLOAT,
                "lower": 0,
                "upper": 360,
                "step": 1
            }
        }

        # -------------------C/OpenCv code------------------------------------
        self.vars = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'double block$id$_double_i1 = $angle$;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n'

    # ----------------------------------------------------------------------
    def generate_header(self):
        return \
            "#define PI 3.1415926535898\n" + \
            "double rads(double degs){\n" + \
            "   return (PI/180 * degs);\n" + \
            "}\n\n"

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        value = \
            '\n if(block$id$_img_i0)\n  {\n' + \
            '       double scale;\n int H;\n    int W;\n' + \
            '       W = block$id$_img_i0->width;\n' + \
            '       H = block$id$_img_i0->height;\n' + \
            '       block$id$_img_o0 = cvCreateImage(cvSize(W,H),' + \
            'block$id$_img_i0->depth,block$id$_img_i0->nChannels);\n' + \
            '       CvMat* mat = cvCreateMat(2,3,CV_32FC1);\n'
        if self.isCenter == "true":
            value += '      CvPoint2D32f center = cvPoint2D32f(W/2, H/2);\n'
        else:
            value += '      CvPoint2D32f center = cvPoint2D32f($xC$,$yC$);\n'

        if self.isScalling == "true":
            value += '      scale = H/(fabs(H*sin(rads' + \
                '(90-abs(block$id$_double_i1)))) + ' + \
                'fabs(W*sin(rads(abs(block$id$_double_i1)))));\n' + \
                '       cv2DRotationMatrix' + \
                '(center,block$id$_double_i1,scale,mat);\n'
        else:
            value += '      cv2DRotationMatrix' + \
                '(center,block$id$_double_i1,1.0,mat);\n'

        if self.isFilling == "true":
            value += '      cvWarpAffine(block$id$_img_i0, ' + \
                'block$id$_img_o0, mat, ' + \
                'CV_WARP_FILL_OUTLIERS, cvScalarAll(0));\n'
        else:
            value += '      cvWarpAffine(block$id$_img_i0,' + \
                'block$id$_img_o0,mat,0,cvScalarAll(0));\n'

        value += '  }\n'
        return value

# -----------------------------------------------------------------------------
