#!/usr/bin/env python3
#coding:utf-8
import difflib,sys
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
for line in difflib.context_diff(s1, s2, fromfile='txt-s1', tofile='txt-s2'):
    sys.stdout.write(line)

difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])       

