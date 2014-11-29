#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------------
"""viperaccept test case."""
__author__ = ('Lance Finn Helsten',)
__version__ = '0.0'
__copyright__ = """Copyright (C) 2014 Lance Helsten"""
__docformat__ = "reStructuredText en"
__license__ = """
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys
import unittest
from viperaccept import AcceptLanguage

class AcceptLanguage_Test(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_None(self):
        """Test non-existant Accept-Language header."""
        gen = AcceptLanguage({})
        self.assertEquals(next(gen), ("*", 1.0))
        self.assertRaises(StopIteration, next, gen)

    def test_Empty(self):
        """Test an empty Accept-Language header."""
        gen = AcceptLanguage({"Accept-Language":""})
        self.assertEquals(next(gen), ("*", 1.0))
        self.assertRaises(StopIteration, next, gen)

    def test_Single(self):
        """Test a single entry in the Accept-Language header."""
        gen = AcceptLanguage({"Accept-Language":"en"})
        self.assertEquals(next(gen), ("en", 1.0))

    def test_Multiple(self):
        """Test multiple entries in the Accept-Language header."""
        gen = AcceptLanguage({"Accept-Language":"en, fr"})
        self.assertEquals(next(gen), ("en", 1.0))
        self.assertEquals(next(gen), ("fr", 1.0))

    def test_QSort(self):
        """Test sorting entries with qvalue parameter."""
        gen = AcceptLanguage({"Accept-Language":"en, en-gb; q=0.5, fr, es-es-ios; q=0.8"})
        self.assertEquals(next(gen), ("en", 1.0))
        self.assertEquals(next(gen), ("fr", 1.0))
        self.assertEquals(next(gen), ("es-es-ios", 0.8))
        self.assertEquals(next(gen), ("en-gb", 0.5))
        self.assertEquals(next(gen), ("es-es", 0.0))
        self.assertEquals(next(gen), ("en", 0.0))
        self.assertEquals(next(gen), ("es", 0.0))
        self.assertRaises(StopIteration, next, gen)

