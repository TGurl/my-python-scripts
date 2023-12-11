#!/usr/bin/env python
"""Config class"""
import os


class Config:  # pylint: disable=too-few-public-methods
    """General configurations"""

    title = "ScreenRec"
    version = "0.0.1"
    target_dir = os.path.join("/", "data", "videos", "recordings")
    record_mouse = False
    default_filename = "screenrec"
