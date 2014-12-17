#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import lip2sql

setup(name='lip2sql',
      version = '1.0',
      author = 'TK' ,
      author_email = 'john.joseph.horton@gmail.com',
      url = 'http://github.com/johnjosephhorton/lip2sql',
      packages = [''],
      package_dir= {'':'.'},
      entry_points={
        'console_scripts':
            ['lip2sql = lip2sql:main',
             ]},
      classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 or '
        'later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ),
      install_requires=['Jinja2>=2.6'],
      )
