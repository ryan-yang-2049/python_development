#!/usr/bin/env python
#coding:utf-8
'''
装饰器之--利用装饰器实现登录用户检查以及token认证。
'''
def login(key):
    name = input("login:")
    local_key = 'qwer'
    if key == local_key and name == "root":
        print("login success!")
        return True
    else:
        return False

def wrap(func):
    def auth(*args,**kwargs):
        key = kwargs.pop('token')
        is_login = login(key)
        if not is_login:
            return "login faild!"
        temp = func(*args,**kwargs)
        return temp
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
    key = input("please input key:")
    res = choice('dev',token=key)
    print(res)






