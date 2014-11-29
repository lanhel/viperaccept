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
import os
import unittest
from viperaccept import negotiate

class Negotiate_Test(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.dirname(__file__), "data_Negotiate", "spam")

    def test_NoHeaders(self):
        """Test with no headers."""
        res = negotiate(self.path, {})
        self.assertIsNotNone(res)

    def test_Mediatype(self):
        """Test for a given media type."""
        res = negotiate(self.path, {"Accept":"text/plain, text/html"})
        res = os.path.basename(res)
        self.assertEquals(res, "spam.txt")

    def test_Language(self):
        """Test for a given media type."""
        res = negotiate(self.path, {"Accept":"text/plain", "Accept-Language":"en, fr, de"})
        res = os.path.basename(res)
        self.assertEquals(res, "spam.txt.fr")

