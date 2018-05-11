#!/usr/bin/env python3

# encoding: utf-8  

""" 
@version: v1.0 
@author: Bruce Long 
@license: Apache Licence  
@contact: lxing_1988@sina.com 
@site:  
@software: PyCharm 
@file: test.py 
@time: 12/29/17 7:24 PM 
"""

import re
import os

line = 'asdf fjdk; afed, fjek,asdf, foo'
spary = re.split(r'[;,\s]\s*', line)
#spary = re.split(r'(;|,|\s)\s*', line)
for char in spary:
    print('-> ' + char)

filenames = os.listdir('.')
print(filenames)