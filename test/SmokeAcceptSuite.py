#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
"""Test environment smoke acceptance test suite. This may be executed
directly to run all of the smoke tests against the `build` directory."""
__author__ = ('Lance Finn Helsten',)
__version__ = '0.0'
__copyright__ = """Copyright (C) 2014 Lance Helsten"""
__docformat__ = "reStructuredText en"

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

class SmokeAcceptSuite(unittest.TestSuite):
    """Smoke test suite."""
    def __init__(self):
        super().__init__()
        tl = unittest.defaultTestLoader
        pwd = os.path.dirname(__file__)
        for path in os.listdir(pwd):
            fpath = os.path.join(pwd, path)
            ipath = os.path.join(fpath, '__init__.py')
            if path.endswith('TestSuite') and os.path.isfile(ipath):
                m = __import__(path)
                for t in m.smoke_suite():
                    self.addTest(t)

if __name__ == '__main__':
    from test import utils

    utils.set_accept_level(utils.SMOKE)
    suite = SmokeAcceptSuite()
    unittest.TextTestRunner(verbosity=2).run(suite)

