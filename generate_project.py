#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import json
import shutil
import subprocess as sp
from pathlib import Path as p
from distutils import dir_util as du
import datetime

import clear_project

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]
author = d["author"]
version = d["version"]
release = d["release"]

# ##################################
clear_project.main()

# generate sphinx project
p_prj = p(project).absolute()

src = p("./tool_box").absolute()
dst = p_prj / p("./source")
du.copy_tree(str(src), str(dst))

confpy = p_prj / p("./source/conf.py")
with open(confpy, 'r', encoding='utf-8') as f:
    body = f.read()

body = re.sub(r"^project.*", r"project = '" + project + "'", body, flags=re.MULTILINE)
body = re.sub(r"^copyright.*", r"copyright = '" + datetime.datetime.now().strftime('%Y') + ", " + author + "'", body, flags=re.MULTILINE)
body = re.sub(r"^author.*", r"author = '" + author + "'", body, flags=re.MULTILINE)
body = re.sub(r"^version.*", r"version = '" + version + "'", body, flags=re.MULTILINE)
body = re.sub(r"^release.*", r"release = '" + release + "'", body, flags=re.MULTILINE)

with open(confpy, 'w', encoding='utf-8') as f:
    f.write(body)
