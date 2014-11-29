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
from viperaccept import AcceptCharset

class AcceptCharset_Test(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_None(self):
        """Test non-existant Accept-Charset header."""
        gen = AcceptCharset({})
        self.assertEquals(next(gen), ("*", 1.0))
        self.assertRaises(StopIteration, next, gen)

    def test_Empty(self):
        """Test an empty Accept-Charset header."""
        gen = AcceptCharset({"Accept-Charset":""})
        self.assertEquals(next(gen), ("*", 1.0))
        self.assertRaises(StopIteration, next, gen)

    def test_Single(self):
        """Test a single entry in the Accept-Charset header."""
        gen = AcceptCharset({"Accept-Charset":"utf-8"})
        self.assertEquals(next(gen), ("utf-8", 1.0))

    def test_Multiple(self):
        """Test multiple entries in the Accept-Charset header."""
        gen = AcceptCharset({"Accept-Charset":"utf-8, unicode-1-1"})
        self.assertEquals(next(gen), ("utf-8", 1.0))
        self.assertEquals(next(gen), ("unicode-1-1", 1.0))

    def test_QSort(self):
        """Test sorting entries with qvalue parameter."""
        gen = AcceptCharset({"Accept-Charset":"utf-8, utf-16; q=0.5, unicode-1-1, iso-8859-5; q=0.8"})
        self.assertEquals(next(gen), ("utf-8", 1.0))
        self.assertEquals(next(gen), ("unicode-1-1", 1.0))
        self.assertEquals(next(gen), ("iso-8859-5", 0.8))
        self.assertEquals(next(gen), ("utf-16", 0.5))

