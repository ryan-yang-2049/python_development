#!/usr/bin/env python3
#coding:utf-8

'''
heapq:在Python中也对堆这种数据结构进行了模块化，我们可以通过调用heapq模块来建立堆这种数据结构，同时heapq模块也提供了相应的方法来对堆做操作
heap = [] #创建了一个空堆 
heappush(heap,item) #往堆中插入一条新的值 
item = heappop(heap) #从堆中弹出最小值 
item = heap[0] #查看堆中最小值，不弹出 
heapify(x) #以线性时间讲一个列表转化为堆 
item = heapreplace(heap,item) #弹出并返回最小值，然后将heapqreplace方法中item的值插入到堆中，堆的整体结构不会发生改变。这里需要考虑到的情况就是如果弹出的值大于item的时候我们可能就需要添加条件来满足function的要求
'''

from heapq import *

def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h,value)
	#return [heappop(h) for i in range(len(h))]
	return h

res=heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

print(res)


