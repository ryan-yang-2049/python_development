#!/usr/bin/env python
#coding:utf-8
'''
利用装饰器写一个登录验证
getpass 在pycharm中不可用
'''
import getpass

def wrap(func):
    def auth(*args,**kwargs):
        user_key = 'qwer'
        name = input("login:")
        key = getpass.getpass("password:")
        if key == 'qwer' and name == 'root':
            print("login success!")
            temp = func(*args,**kwargs)
            return temp
        else:
            print("login faild!")
    return auth
@wrap
def choice(arg):
    host_list = ['host01','host02','host03']
    print('''
            0.查看主机列表
            1.查看本机IP地址
            2.查看防火墙是否开启
            3.查看端口
            4.查看cpu占用前5
       ''')
    your_choice = input("input your choice:")
    last_choice = int(your_choice)
    if last_choice == 0:
        print("check %s host list" % arg)
        return host_list

if __name__ == '__main__':
    res = choice('dev')
    print(res)