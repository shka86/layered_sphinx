#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path as p
from distutils import dir_util as du

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]
publish_to = p(d["publish_to"]).absolute()

# ##################################

def main():

    p_project = p(project).absolute()
    p_build = p_project / p("build")

    print("copy from: " + str(p_build))
    print("copy to  : " + str(publish_to))

    du.copy_tree(str(p_build), str(publish_to))

if __name__ == '__main__':

    main()
