#!/usr/bin/env python
#coding:utf-8
import traceback
import sys
try:
    s = input()
    print(int(s))
except ValueError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("\n%s \n %s \n %s\n" %(exc_type, exc_value, exc_tb ))
    traceback.print_exc()

