#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import os
# import sys
# from pathlib import Path as p
import codecs
import chardet

# ##################################

def main(f):

    body = open(f, 'rb').read()
    enc = chardet.detect(body)['encoding']

    if enc == 'UTF-8-SIG':
        print(enc, " -> utf-8: ", f)
        with open(f, 'r', encoding='utf-8-sig') as g:
            body = g.read()
        with open(f, 'w', encoding='utf-8') as g:
            g.write(body)

    elif enc == 'SHIFT-JIS':
        print(enc, " -> utf-8: ", f)
        with open(f, 'r', encoding='shift-jis') as g:
            body = g.read()
        with open(f, 'w', encoding='utf-8') as g:
            g.write(body)

    elif enc == 'utf-8':
        print(enc, " : ", f)

    else:
        print(enc, " : ", f)


if __name__ == '__main__':
    main(f)
