#!/usr/bin/env python3
#coding:utf-8

from time import sleep
import os

source = 10

try:
	pid = os.fork()
	if pid == 0:
		print("this is child process.")
		source = source - 1
		sleep(3)
	else:
		print("this is parent process.")
	print(source)
except OSError as e:
	pass

