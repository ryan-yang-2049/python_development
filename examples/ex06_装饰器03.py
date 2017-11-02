#!/usr/bin/env python
#coding:utf-8
'''
装饰含返回值的函数
'''

def warp(func):
    def change_info(*args,**kwargs):
        print('--before--')
        temp = func(*args,**kwargs)
        print('--after--')
        return temp
    return change_info

@warp
def check_info(arg):
    print("check host list:",arg)
    host_list = ['host01','host02','host03']
    return host_list

if __name__ == '__main__':
    print(check_info('host01'))







