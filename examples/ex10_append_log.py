#!/usr/bin/env python
#coding:utf-8

import sys
stdout_backup = sys.stdout
log = open('./log.txt','a')
sys.stdout = log
for i in range(0,10):
	print('step %s'% i)
log.close()
