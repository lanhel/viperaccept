#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
"""Negotiation system to find closest matching resource."""
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

__all__ = ['negotiate']

import os
import mimetypes
from .headers import *

def negotiate(path, headers, language_priority=['en'], media_parameter_filter=lambda name, mediatype, qvalue, params: True):
    """Given a ``path`` and a set of HTTP ``headers`` determine the best
    resource variant and return that path. The ``language_priority`` is
    a list of language codes to be used after all language codes in the
    ``Accept-Language`` header.

    This will not filter based on parameters in the ``Accept`` header, but
    will call ``media_parameter_filter`` with the ``name`` of the file
    (not the full path), the ``mediatype``, the ``qvalue``, and the
    ``params`` (as a mapping of param key to value). This callable should
    return ``True`` if the file matches and ``False`` to filter it out.
    This may be called multiple times on the same file with different
    ``mediatype``, ``qvalue``, and ``params``.

    This expects filenames to be of the form:

    ::
        filename = basename "." typeext *(("." lang) / ("." charset) / ("." content-coding) / ("." user-defined))

        basename = [\.]*                                ; basename from path

        typeext = 1*(ALPHA / DIGIT)                     ; extension recognized by mimetypes

        lang = 1*8ALPHA *( "-" 1*8ALPHA)                ; language code

        charset = 1*(ALPHA / DIGIT / "-" / "_")         ; character set of the file

        content-coding = 1*(ALPHA / DIGIT / "-" / "_")  ; content coding (e.g. compress, gzip)

        user-defined = 1*(ALPHA / DIGIT / "-" / "_")    ; user defined "meta-data"

    The algorithm used is to look at all the variants and find the best one
    via elimination. After filtering on ``Accept`` if at any time there is
    only a single variant then it is returned.

    Elimination steps:

    1. For each mediatype in ``Accept`` will be filtered against the
       ``typeext`` by using the extensions from ``mimetypes`` package. This
       set will then be filtered through ``media_parameter_filter``.

    2. Filter the list by ``Accept-Language`` against ``lang``. This will
       first check against all the entries in the ``Accept-Language`` then
       for each language code that has multiple fields (e.g. ``en-gb``) the
       last component will be stripped and added to the end of the list.
       So if ``Accept-Language`` is ``en, fr-CA-linux, en-gb`` then the
       languages checked will be ``en``, ``fr-CA-linux``, ``en-gb``,
       ``fr-CA``, ``en``, ``fr``.

    3. Filter the list by ``Accept-Charset`` against ``charset``.

    4. Filter the list by ``Accept-Encoding`` against ``content-coding``.

    5. Allow the user to filter the list over ``user-defined`` data.
       UNIMPLEMENTED AT THIS TIME.

    After elimination if there is still more than one variant then they are
    sorted and the one with the shortest ``Content-Length`` will be returned.
    """
    dirname, basename = os.path.split(path)
    files = [(f.split(".", 1)[0], f.split(".")[1:], f) for f in os.listdir(dirname) if f.startswith(basename)]

    ###
    ### Accept filter and sort
    mediafiles = []
    for mediatype, qvalue, params in Accept(headers):
        if mediatype == '*/*':
            keep = files
        elif mediatype.split('/')[1] == '*':
            keep = []
            mediatype = mediatype.split('/')[0]
            for base, extensions, path in files:
                for ext in extensions:
                    mtype, msubtype = mimetypes.guess_type(base + "." + ext).split('/')
                    if mtype == mediatype:
                        keep.append((base, extensions, path))
        else:
            extensions = [mt.lstrip('.') for mt in mimetypes.guess_all_extensions(mediatype)]
            keep = [f for f in files if f[1][0] in extensions]

        keep = [f for f in keep if media_parameter_filter(f[2], mediatype, qvalue, params)]

        mediafiles = mediafiles + keep
        for k in keep:
            files.remove(k)
        if not files:
            break
    files = [(f[0], f[1][1:], f[2]) for f in mediafiles]
    if len(files) == 1:
        return os.path.join(dirname, files[0][2])

    ###
    ### Accept-Langauge filter and sort
    for lang, qvalue in AcceptLanguage(headers, defaults=language_priority):
        keep = [f for f in files if lang in f[1]]
        if keep:
            files = keep
            break
    if len(files) == 1:
        return os.path.join(dirname, files[0][2])

    ###
    ### Accept-Charset filter and sort
    for charset, qvalue in AcceptCharset(headers):
        keep = [f for f in files if charset in f[1]]
        if keep:
            files = keep
            break
    if len(files) == 1:
        return os.path.join(dirname, files[0][2])

    ###
    ### Accept-Encoding filter and sort
    for encoding, qvalue in AcceptEncoding(headers):
        keep = [f for f in files if encoding in f[1]]
        if keep:
            files = keep
            break
    if len(files) == 1:
        return os.path.join(dirname, files[0][2])

    ###
    ### User content handling

    ###
    ### Content-Length sort
    def file_size(f):
        path = os.path.join(dirname, f[2])
        try:
            return os.path.getsize(path)
        except OSError:
            return sys.maxsize
    files.sort(key=file_size)

    return os.path.join(dirname, files[0][2])





