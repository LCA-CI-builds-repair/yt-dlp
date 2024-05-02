#!/usr/bin/env python3

# Execute with
# $ python -m yt_dlp

import sys
import os.path as path

if __package__ is None and not getattr(sys, 'frozen', False):
    # direct call of __main__.py
    path = path.realpath(path.abspath(__file__))
    sys.path.insert(0, path.dirname(path.dirname(path)))

import yt_dlp
if __name__ == '__main__':
    yt_dlp.main()
