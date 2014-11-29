#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
"""High level generators for content negotiation."""
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

__all__ = []


class FileNames():
    """Generator that returns a filename that is built from the various
    header elements in order of highest quality value to lowest quality
    value and the sorted on the order of the elements as they appear in
    the ``headers``.

    The ``template`` is a path with variable parts in ``{}`` as follows:

        - ``{extension}``: Replaced with the filename extension associated with
          the media type.

        - ``{language}``: Replaced with the language code in the form of
          ``1*8ALPHA *( "-" 1*8ALPHA)``.

        - ``{charset}``: Replaced with the character set.

        - ``{encoding}``: Replaced with the encoding.

    The ``mediatypes`` is a mapping of media types to file extensions. If
    none is given then ``mimetypes`` will be used to generate this mapping.

    If a media type maps to more than one filename extension then the value
    should be a list of extensions. The default mapping values will be
    sorted by longest extension and then alphabetically: e.g. for ``video/mpeg``
    the extensions will be ``mpeg``, ``mpa``, ``mpe``, and ``mpg``.
    """
    def __init__(self, headers, template, mediatypes=None):
        self.template = template
        self.mediatypes = mediatypes if mediatypes != None else self.__mediatypes


    def __mediatypes(self):
        pass



class FileNameParts():
    """Generator that returns the filename parts from which a filename
    may be built in order of highest quality value to lowest quality
    value followed by the order of the elements as they appear in headers.
    """
    def __init__(self, headers):
        accept = Accept(headers)
        charset = AcceptCharset(headers)
        encoding = AcceptEncoding(headers)
        language = AcceptLanguage(headers)
        self.accept

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.acceptelems.pop(0)
        except IndexError:
            raise StopIteration
