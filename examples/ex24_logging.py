#!/usr/bin/env python3
#coding:utf-8

import logging

logging.basicConfig(level=logging.DEBUG,
			format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
			datefmt='%a, %d %b %Y %H:%M:%S',
			filename='test_logging.log',
			filemode='w')

while True:
	option = input('please a number:')
	if option.isdigit():
		print("input correct",option)
		logging.info('输入正确')
	else:
		print('your must input a number')
		logging.error('输入错误')



