#!/usr/bin/env python
#coding:utf-8

import pickle
dic = {"name":"ryan","age":18,"job":"IT"}
with open('account.pkl','wb') as obj_file:
    pickle.dump(dic,obj_file)