#!/usr/bin/env python3
#coding:utf-8
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",type=int,help="display a square of a given number")
parser.add_argument("-v","--verbose",action="store_true",help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
	print("the square of {} equals {}".format(args.square,answer))
else:
	print(answer)

'''
root:examples# python3 ex21_argparse.py 3
9
root:examples# python3 ex21_argparse.py 4 -v
the square of 4 equals 16
root:examples# python3 ex21_argparse.py -v 5
the square of 5 equals 25
注意：
1、我们输入了位置参数，所以程序会有反应
2、次序无关紧要
'''
