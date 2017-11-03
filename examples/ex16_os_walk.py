#!/usr/bin/env python3
#coding:utf-8

import os
[os.path.join(x[0],y) for x in os.walk('/opt/gitcode/') for y in x[2] ]

