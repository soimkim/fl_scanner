#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
import sys
import os
import fosslight_util
from datetime import datetime
from textblob import Word
import getopt
import markdown
from bs4 import BeautifulSoup
from textblob import TextBlob


def main():
    argv = sys.argv[1:]
    path_to_scan = ""

    try:
        opts, args = getopt.getopt(argv, 'p:')
        for opt, arg in opts:
            if opt == "-p":
                path_to_scan = arg
    except Exception as error:
        print(str(error))
    
    if os.path.isfile(path_to_scan):
        files = [path_to_scan]
    else:
        files = get_md_files(path_to_scan)
    check_typo(files)


def get_md_files(dir):
    file_ext = ".md"
    md_files = []
    if os.path.isdir(dir):
        md_files = [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith(file_ext)]
        print("Check md files in "+dir)
        print("|- Total count of md files:"+str(len(md_files)))
    else:
        print("Check path of dir:"+dir)

    return md_files


def check_typo(files):
    for file in files:
        print("|- Check for typos :"+file)
        contents = read_file(file)

        import re
        #str=re.findall("[a-zA-Z,.()\-0-9]+",contents)
        #updated_docx=(" ".join(str))
        #print(updated_docx)

        from spellchecker import SpellChecker
        spell = SpellChecker()

        
        #print(contents)
        #if contents != "":
        #    w = Word(contents)
        #    w.spellcheck()
        for line in contents:
           #test = False
           #if test:
           b = TextBlob(line)
           correct_line = str(b.correct())
           #misspelled = spell.unknown(line)
           #print(str(misspelled))
           if correct_line != line:
               print(line + "->" + correct_line)
           
           #   print(correct_line)
           for word in line.split():
               #b = TextBlob(word)
               #correct_line = str(b.correct())
               pass
               #if word != correct_line:
               #    print(word + "->" + correct_line)
               #w = Word('tets')
               #print(w.spellcheck())
               #break


def read_file_line(file):
    lines = []
    try:
        f = open(file, 'r')
        lines = f.readline()
        f.close()
    except Exception as error:
        print(str(error))
    return lines


def read_file(file):
    content = ""
    try:
        f = open(file, 'r')
        html = markdown.markdown(f.read())
        text = ''.join(BeautifulSoup(html, "html.parser").findAll(text=True))
        content = text.splitlines()
        f.close()
    except Exception as error:
        print(str(error))
    return content


if __name__ == '__main__':
    main()
