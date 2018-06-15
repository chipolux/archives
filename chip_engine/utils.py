# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:35:12 2013

@author: chipolux
"""
from os import path
import json
import sys

def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")

def module_path():
    encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return path.dirname(unicode(sys.executable, encoding))
    return path.dirname(unicode(__file__, encoding))

CURRENT_DIR = module_path()

def parse_jsonfile(filepath):
    try:
        with open(filepath) as f:
            obj = json.load(f)
    except ValueError, e:
        raise ValueError, '%s in %s' % (e.message, filepath)
    return obj