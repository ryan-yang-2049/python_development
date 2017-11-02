#!/usr/bin/env python
#coding:utf-8

def auth(func):
    def user_auth(arg):
        print('--before--')
        func(arg)
        print('--after--')
    return user_auth

@auth
def one(arg):
    print('I',arg)

if __name__ == '__main__':
    one("love you")



