#!/usr/bin/env python
#coding:utf-8
'''
with open('./passwd','r') as f:
	for line in f.readlines():
		print(line.rstrip())
'''

with open('./passwd','r') as f:
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		x = line.split(':')
		print(x[6])

	
    
	

