#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
"""Generators that will produce sorted header values."""
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

__all__ = ['Accept', 'AcceptCharset', 'AcceptEncoding', 'AcceptLanguage']


class AcceptBase():
    """This is the base class for all the accept type header geneators. It
    do common parsing of a header."""
    def __init__(self, headers, name, defaultvalue):
        self.acceptelems = []
        accepthdr = headers.get(name)
        if not accepthdr:
            accepthdr = defaultvalue

        for elem in (e.strip() for e in accepthdr.split(',')):
            media, params = elem.split(';', 1) if ';' in elem else (elem, '')
            params = [p.strip().split("=") for p in params.split(';') if "=" in p]
            params = dict(params)
            if 'q' in params:
                q_value = float(params['q'])
                del params['q']
            else:
                q_value = 1.0
            #TODO need to handle quoted-string case
            self.acceptelems.append((media, q_value, params))
        self.acceptelems.sort(key=lambda e: e[1], reverse=True)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.acceptelems.pop(0)
        except IndexError:
            raise StopIteration


class Accept(AcceptBase):
    """This will parse the ``Accept`` header from the ``headers`` mapping
    type and return the media types with the associated qvalue and a mapping
    type of extensions.
    """
    def __init__(self, headers):
        super().__init__(headers, "Accept", "*/*")


class AcceptCharset(AcceptBase):
    """This will parse the ``Accept-Charset`` header from the ``headers``
    mapping type and return the character sets with the associated qvalue.
    """
    def __init__(self, headers):
        super().__init__(headers, "Accept-Charset", "*")

    def __next__(self):
        name, qvalue, params = super().__next__()
        return name, qvalue


class AcceptEncoding(AcceptBase):
    """This will parse the ``Accept-Encoding`` header from the ``headers``
    mapping type and return the encoding types with the associated qvalue.
    """
    def __init__(self, headers):
        super().__init__(headers, "Accept-Encoding", "*")

    def __next__(self):
        name, qvalue, params = super().__next__()
        return name, qvalue


class AcceptLanguage(AcceptBase):
    """This will parse the ``Accept`` header from the ``headers`` mapping
    type and return the media types with the associated qvalue.
    """
    def __init__(self, headers, defaults=[]):
        super().__init__(headers, "Accept-Language", "*")
        self.defaults = defaults

    def __next__(self):
        try:
            name, qvalue, params = super().__next__()
        except StopIteration:
            if not self.defaults:
                raise
            name = self.defaults.pop(0)
            qvalue = 0.0
        if name in self.defaults:
            self.defaults.remove(name)
        if '-' in name:
            self.acceptelems.append((name.rsplit('-', 1)[0], 0.0, params))
        return name, qvalue



