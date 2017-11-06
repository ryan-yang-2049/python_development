#!/usr/bin/env python3
#coding:utf-8
'''
可选参数
短选项

'''
import argparse  
parser = argparse.ArgumentParser()  
parser.add_argument("-v","--verbosity", help="increase output verbosity",action="store_true")  
args = parser.parse_args()  
if args.verbosity:  
    print("verbosity turned on")  

'''
结果分析：

1、当--verbosity被指定时程序会输出回显，当没被指定时没有显示。
2、显示的那个参数是可选的，即使没有它程序也会正常运行。注意，在默认情况下如果参数没有被使用，那么相关的变量例如本例中的args.verbosity将被指定一个None值。
3、现在选项并不是需要一个值，我甚至改变了它的名字用来匹配这个说法。注意，我们指定了一个新的关键词action，并且给他赋值为"store_true"。它的意思是，如果选项被指定了则将True赋值给args.verbose，没有指定则赋值Flash。
4、当你指定一个值的时候它才被解释为True值。
5、-v 表示短选项
注意帮助信息的不同。
执行结果：
root:examples# python3 ex20_argparse.py -v
verbosity turned on
root:examples# python3 ex20_argparse.py --verbosity
verbosity turned on
提示：
root:examples# python3 ex20_argparse.py -h
usage: ex20_argparse.py [-h] [-v]

optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity  increase output verbosity
-v 参数如果不添加，那么在下面的optional arguments 则不会显示。
'''

