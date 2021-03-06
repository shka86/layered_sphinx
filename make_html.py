#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import textwrap
import shutil
import subprocess
import json
from pathlib import Path as p
from distutils import dir_util as du
from pprint import pprint as pp
import enc2utf8

# ##################################
# read paths
with open("settings.json", 'r', encoding='utf-8') as f:
    d = json.load(f)

project = d["project"]
p_doc_srcs = d["doc_source"]

p_project = p(project).absolute()
p_source = p_project / p("./source")
p_source_top = p_source / p("./top")

# ##################################

def _listprint(lists):
    for x in lists:
        print(x)


def listup_dir(search_path):
    return [x.relative_to(search_path)
            for x in search_path.iterdir()
            if x.is_dir()]


def listup_docsrc(search_path):
    return [x.relative_to(search_path)
            for x in search_path.iterdir()
            if (x.is_file() and (str(x).endswith(".md")) or (str(x).endswith(".rst")))]


def generate_toc(toc_title, tocs):
    body = textwrap.dedent('''
        {toc_title}
        ====================================

        .. toctree::
           :maxdepth: 2
           :caption: Contents:

        {tocs}

    ''').format(toc_title=toc_title, tocs=tocs)

    return body


def generate_spx_layer(p_tgt, if_top=False):
    """Construct sphinx-ready file tree.
    """
    # listup dirs and files
    list_dir = listup_dir(p_tgt)
    list_file = listup_docsrc(p_tgt)

    tocs = ""
    for dr in list_dir:
        line = str(dr) + "/" + str(dr) + ".rst\n"
        tocs += "   " + line
    for f in list_file:
        line = str(f) + "\n"
        tocs += "   " + line

    toc_title = p_tgt.stem
    index_body = generate_toc(toc_title, tocs)

    if if_top:
        idx_name = "index.rst"
    else:
        idx_name = str(p_tgt.stem) + ".rst"

    idx_name = p(idx_name)
    p_idx = p_tgt / idx_name

    with open(p_idx, 'w', encoding="utf-8") as f:
        f.write(index_body)

    # recursive
    for dr in list_dir:
        print(p().cwd())
        print(dr)
        generate_spx_layer(p_tgt / dr)


def update_spx_source(src=""):
    """Move a file tree to sphinx source. Old sources are deleted.
    """

    # delete old spx_prj source
    p_spxsrc = p(spx_src_dir)
    if p_spxsrc.is_dir():
        shutil.rmtree(p_spxsrc)
    p_spxsrc.mkdir()

    # prepare new spx_prj source dir
    p_spxsrc_org = p(str(p_spxsrc) + "_org")
    list_src = p_spxsrc_org.glob("**/*")
    _listprint(list_src)

    shutil.copytree(str(p_spxsrc_org), str(p_spxsrc))
    # du.copy_tree(str(p_spxsrc_org), str(p_spxsrc))

    # copy doc source
    list_src = src.glob("**/*")
    _listprint(list_src)

    shutil.copytree(str(src), str(p_spxsrc))
    # du.copy_tree(str(src), str(p_spxsrc))

def main():

    print("-- clean doc source ------------------------------")
    srcs = list(p_source.glob("*"))
    safelist = [
        p_source / p("./_static"),
        p_source / p("./_templates"),
        p_source / p("./conf.py")
        ]

    for src in srcs[:]:
        if not(src in safelist):
            print(src)
            if src.is_dir():
                shutil.rmtree(src)
            else:
                src.unlink()

    print("-- copy doc source ------------------------------")
    for p_doc_src in p_doc_srcs:
        p_doc_src = p(p_doc_src)
        print(p().cwd())
        p_html_top = p_source / p("./top")
        # shutil.copytree(str(p_doc_src), str(p_html_top))
        du.copy_tree(str(p_doc_src), str(p_html_top))

        files = p_html_top.glob("**/*")
        for f in files:
            os.chmod(f, 0o777)

    generate_spx_layer(p_html_top, if_top=True)

    print("-- convert encodings ------------------------------")
    os.chdir(p_project)
    print(p_project)
    print(p_source_top)
    files = []
    files += p_source_top.glob("**/*.rst")
    files += p_source_top.glob("**/*.md")

    for f in files:
        enc2utf8.main(f)

    print("-- execute sphinx ------------------------------")
    os.chdir(p_project)
    p_build = p_project / p("build")
    if p_build.exists():
        shutil.rmtree(p_build)

    cmd = "sphinx-build -M html source build"
    subprocess.run(cmd.split())


if __name__ == '__main__':

    main()
