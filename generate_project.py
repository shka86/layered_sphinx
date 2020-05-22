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

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]
author = d["author"]
version = d["version"]
release = d["release"]

# ##################################
# generate sphinx project
p_prj = p(project).absolute()
if p_prj.is_dir():
    files = p_prj.glob("**/*")
    for f in files:
        os.chmod(f, 0o777)
    shutil.rmtree(p_prj)

src = str(p("./tool_box").absolute())
dst = str(p_prj / p("./source"))
du.copy_tree(src, dst)

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
