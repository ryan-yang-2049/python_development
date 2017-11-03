#!/usr/bin/env python3
#coding:utf-8
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3) 
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x: 
    print('ShortInputException:  %d | %d' % (x.length, x.atleast))
except Exception as err: 
    print(str(err))
else:
	print('No exception was raised.')
finally:
       print('finally')


