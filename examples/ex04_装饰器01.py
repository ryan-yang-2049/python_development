#!/usr/bin/env python
#coding:utf-8
def auth(func):
    def user_auth():
        print('before')
        func()
    return user_auth

def one():
    print('one')
temp  = auth(one)
one = temp

def two():
    print('two')
two = auth(two)

@auth
def three():
    print('three')

if __name__ == '__main__':
    print('----one method----')
    one()
    print('---two method----')
    two()
    print('---three method---')
    three()
