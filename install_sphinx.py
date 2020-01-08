#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess as sp

# ##################################
# install tools
cmd = "pip install sphinx commonmark recommonmark sphinx-markdown-tables sphinx_rtd_theme"
ret = sp.call(cmd)

