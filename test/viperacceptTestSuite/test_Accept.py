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
from viperaccept import Accept

class Accept_Test(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_None(self):
        """Test non-existant Accept header."""
        gen = Accept({})
        self.assertEquals(next(gen), ("*/*", 1.0, {}))
        self.assertRaises(StopIteration, next, gen)

    def test_Empty(self):
        """Test an empty Accept header."""
        gen = Accept({"Accept":""})
        self.assertEquals(next(gen), ("*/*", 1.0, {}))
        self.assertRaises(StopIteration, next, gen)

    def test_Single(self):
        """Test a single entry in the Accept header."""
        gen = Accept({"Accept":"text/plain"})
        self.assertEquals(next(gen), ("text/plain", 1.0, {}))

    def test_Multiple(self):
        """Test multiple entries in the Accept header."""
        gen = Accept({"Accept":"text/plain, image/jpeg"})
        self.assertEquals(next(gen), ("text/plain", 1.0, {}))
        self.assertEquals(next(gen), ("image/jpeg", 1.0, {}))

    def test_QSort(self):
        """Test sorting entries with qvalue parameter."""
        gen = Accept({"Accept":"text/plain, application/octet; q=0.5, image/jpeg, text/rtf; q=0.8"})
        self.assertEquals(next(gen), ("text/plain", 1.0, {}))
        self.assertEquals(next(gen), ("image/jpeg", 1.0, {}))
        self.assertEquals(next(gen), ("text/rtf", 0.8, {}))
        self.assertEquals(next(gen), ("application/octet", 0.5, {}))

