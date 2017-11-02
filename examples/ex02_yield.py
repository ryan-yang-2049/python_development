#!/usr/bin/env python
#coding:utf-8

def count(n):
    # print("cunting")
    while n > 0:
        yield n
        n -= 1

c = count(5)
c.next()
c.next()
c.next()













