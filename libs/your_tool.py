#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is an example of tool.
Put your tool or interface under the libs directory, it will run.
"""

def lowercase(text):
    """
    A simple exmple of tool.
    This function lowercases input string.
    """
    return [(word, word.lower()) for word in text.rstrip().split()]
