#!/usr/bin/env python
#coding:utf-8

import csv
with open("test.csv",'w',newline="") as datacsv:
    csvwriter = csv.writer(datacsv,dialect=("excel"))
    csvwriter.writerow(["A","B","C","D"])


