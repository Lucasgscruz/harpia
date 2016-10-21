#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing the comment plugin class.
"""

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin


class Comment(OpenCVPlugin):
    """
    Comment plugin class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.comment = ""

        self.help = "Insert a comment"

        self.description = {
            "Label": "Comment",
            "Icon": "images/comment.png",
            "Color": "50:100:200:150",
            "InTypes": "",
            "OutTypes": "",
            "TreeGroup": "General"
        }

        self.properties = {
            "comment": {
                "name": "Comment",
                "type": HARPIA_COMMENT
            }
        }

        # ----------------C/OpenCv code--------------------------------
        self.vars = '/* $comment$ */ \n'

# -----------------------------------------------------------------------------
