
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import sys
import re

def wildchar_to_regex(str):
    if not str: return ''
    return str.replace('.', '\\.').replace('*', '.*').replace('?', '.?') 


workdir = os.getcwd()

pattern = "*"

if len(sys.argv) > 1:
    pattern = wildchar_to_regex(sys.argv[1])

if len(sys.argv) > 2:
    workdir = sys.argv[2]

for root, dirs, files in os.walk(workdir):

    list = [path.join(root, dir, "") for dir in dirs]
    list += [path.join(root, file) for file in files]

    for l in list:

        if re.search(wildchar_to_regex(pattern), l):
            print l

