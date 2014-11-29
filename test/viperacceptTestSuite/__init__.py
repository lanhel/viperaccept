#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
"""sbdstore test suite."""
__author__ = ('Lance Finn Helsten',)
__version__ = '0.0'
__copyright__ = """Copyright (C) 2014 Lance Helsten"""
__docformat__ = "reStructuredText en"

import os
import unittest
from ftpysetup.runtest.acceptlevel import *

def test_suite():
    return unittest.defaultTestLoader.discover(os.path.dirname(__file__), pattern='test_*')

def smoke_suite():
    suite = smoke_suite(os.path.dirname(__file__))
    return suite

def sanity_suite():
    suite = sanity_suite(os.path.dirname(__file__))
    return suite

def shakedown_suite():
    suite = shakedown_suite(os.path.dirname(__file__))
    return suite

