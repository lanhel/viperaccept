#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#----------------------------------------------------------------------------
"""HTTP content negotiation application."""
__author__ = ('Lance Finn Helsten',)
__version__ = '0.0'
__copyright__ = """Copyright (C) 2014 Lance Finn Helsten"""
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
import setuptools
setuptools.setup(
    name = "viperaccept",
    version = __version__,
    author = 'Lance Finn Helsten',
    author_email = 'lanhel@flyingtitans.com',
    description = __doc__,
    long_description = open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    packages = [
        'viperaccept'
    ],
#    scripts = [
#    ],
)




