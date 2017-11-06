#!/usr/bin/env python3
#coding:utf-8

import csv
with open('test.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Column1', 'Column2', 'Column3'])
    writer.writerows([range(3) for i in range(5)])

