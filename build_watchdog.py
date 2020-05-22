#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
# import textwrap
# import shutil
# import subprocess
import json
from pathlib import Path as p
# from distutils import dir_util as du

import datetime
from pprint import pprint as pp
import time

import make_html
import publish

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]

# set build target directory
curdir = p().cwd().absolute()
build_src_dirs = d["doc_source"]
# ##################################

def get_srcs(build_dirs):

    build_files = []
    for build_dir in build_dirs:
        build_files += list(p(build_dir).glob("**/*"))

    return set(build_files)

def main():

    epoctime_mem = 0

    while True:

        os.chdir(curdir)

        files = get_srcs(build_src_dirs)
        epoctime_new = 0

        for file in files:
            update_time = file.stat().st_mtime
            epoctime_new += update_time
            # update_time = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            # print(update_time)
        
        if epoctime_new != epoctime_mem:
            print("================================")
            print("epoctime_mem: ", epoctime_mem)
            print("epoctime_new: ", epoctime_new)
            epoctime_mem = epoctime_new
            print("--------------------------------")
            pp(files)
            print("--------------------------------")
            make_html.main()

            os.chdir(curdir)
            publish.main()
            dt = datetime.datetime.now()
            print("--------------------------------")
            print("Last build @ " + dt.strftime('%Y/%m/%d-%H:%M:%S'))
            print("Now watching ")
            pp(build_src_dirs)

        time.sleep(1)


if __name__ == '__main__':

    main()
