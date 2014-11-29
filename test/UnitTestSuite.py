#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
"""Test environment unit test suite to do unit testing over the whole
project. This will discover all tests that are in modules that match the
name 'test_*'."""
__author__ = ('Lance Finn Helsten',)
__version__ = '0.0'
__copyright__ = """Copyright (C) 2014 Lance Helsten"""
__docformat__ = "reStructuredText en"

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

__all__ = ['UnitTestSuite']

class UnitTestSuite(unittest.TestSuite):
    """Unit test suite."""

    def __init__(self):
        super().__init__()
        tl = unittest.TestLoader()
        for test in tl.discover(os.path.dirname(__file__), pattern="test_*"):
            self.addTest(test)


if __name__ == '__main__':
    suite = UnitTestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)


