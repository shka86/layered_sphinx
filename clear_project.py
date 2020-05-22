#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import shutil
from pathlib import Path as p

# ##################################

def main():
    # read paths
    with open("settings.json", 'r', encoding='utf-8') as f:
        d = json.load(f)

    project = d["project"]

    # generate sphinx project
    p_prj = p(project).absolute()
    if p_prj.is_dir():
        files = p_prj.glob("**/*")
        for f in files:
            os.chmod(f, 0o777)
        shutil.rmtree(p_prj)

if __name__ == '__main__':
    main()
