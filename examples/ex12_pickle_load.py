#!/usr/bin/env python
#coding:utf-8
import pickle

with open("account.pkl",'rb') as obj_read:
    info = pickle.load(obj_read)
    print(info)
    print("文件描述符：",obj_read.fileno())
    print("文件编码：",obj_read.encoding)