#!/usr/bin/env python

from setuptools import setup, find_packages

import os
execfile(os.path.join('indextank', 'version.py'))

setup(
    name = 'indextank',
    version = VERSION,
    description = 'IndexTank API Client for Python',
    packages = find_packages(),
    install_requires = ["anyjson"],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
