#!/usr/bin/env
#coding:utf-8
'''
日期转换成时间戳
'''
import time
while 1:
	atime = input("输入格式如[14.05.13 13:00]:")
	try:
		btime = time.mktime(time.strptime("%s:0" %atime,'%y.%m.%d %H:%M:%S'))
		print(btime)
		break
	except:
		print("时间格式输入错误，格式如[14.05.13 13:00]")
