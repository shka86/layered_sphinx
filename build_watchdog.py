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
# import pprint
import time

import make_html

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]

# ##################################

def main():

    epoctime_mem = 0

    curdir = p().cwd().absolute()
    build_src = curdir / p("doc_source")

    while True:

        os.chdir(curdir)
        files = list(build_src.glob("**/*"))
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

            make_html.main()
            dt = datetime.datetime.now()
            print("================================")
            print("Last build @ " + dt.strftime('%Y/%m/%d-%H:%M:%S'))
            print("Now watching " + str(build_src))
            print("finished")

        time.sleep(1)


if __name__ == '__main__':

    main()
