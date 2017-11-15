#python每日一解：
	1.在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)
		方法1):
			for i in range(len(numbers)):
				print('({0},{1})'.format(i,numbers[i]))
		
		方法2):
			for index,value in enumerate(numbers):
				print('({0},{1})'.format(index,value))
		
		解题说明：内置函数 enumerate 还可以接收一个默认参数 start ，用于指定 index 从哪个数开始，默认是0。
			for index,value in enumerate(numbers,1):
				print('({0},{1})'.format(index,value))
				
			(1,10)
			(2,29)
			(3,30)
			(4,41)

	
	2.设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
		#!/usr/bin/env python3
		#coding:utf-8
		import random
		class GuessGame:
			def __init__(self,min_num,max_num,choice):
				'''
				:param min_num:最小值
				:param max_num:最大值
				:param choice: 中奖机会
				'''
				self.max_num = max_num
				self.min_num = min_num
				self.target = random.randint(min_num,max_num)
				self.choice = choice
			def guess(self):
				'''
				猜数字
				'''
				choice = self.choice
				while choice > 0:
					choice -= 1
					try:
						num = int(input("输入幸运数字:"))
					except ValueError as e:
						print("请输入有效数字:")	
						continue
					if num == self.target:
						print("恭喜你猜中了")
						break
					elif num <= self.target:
						print("你猜的数字太小了,还剩下 %d 次机会" %choice)
					else:
						print("你猜的数字太大了,还剩下 %d 次机会" %choice)
				else:
					print("很遗憾, %d 次机会都用完了，只差一点点就猜中了，正确答案是 %d" % (self.choice,self.target))
		if __name__ == '__main__':
			game = GuessGame(1,10,5)
			game.guess()

			
		解题说明：	
			1.函数用小写加下划线，类用驼峰式命名
			2.尽量用到异常处理
			3.编写代码尽量简洁
			4.代码抽象化
			5.现在如果产品要求更改猜测的次数或者扩大随机数的范围，我们不需要修改这个类里面的任何一行代码，只需要在调用的时候改变一下即可。话说回来， 有时我们没必要为了一个很小的功能而这样去设计，但是，如果随着这个游戏的功能，复杂度越来越高的时候，这样的设计就很有必要了。然而在真实场景中，需求是一点点往上加的，如果我们能站在更高的角度来思考问题，就能避免被产品牵着鼻子走，走在产品的前面，面对他们的需求游刃有余。可以看到使用了python中特有的 while ... else 语法，在这样的场景非常适合，免去了使用额外的标识变量来表示是否猜中，同样还有 for ... else 和 try ... else 语法，大家可以总结下这些语法是如何使用的。
			
			
	3.统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。		
		分析：
			1.如何正确读写文件
				在python中读写文件可以使用内置函数open()，而 open 函数在python2 和 python3 中有一定的区别，比如 Python3中可以指定读写文件的编码格式，而 Python 则不可以，为了同时兼容2和3，我们通常会使用io模块下面的 open 函数
			2.如何对数据进行排序
				sorted函数是一个使用频率很高的内置函数，它的用法也很强大，因为它可以通过指定参数 key 来进行自定义排序，也就意味着你不仅可以对数字排序、对字母排序、还可以对列表、字典、自定义的对象进行排序，你只需要要告诉 sorted 函数的排序规则是什么.对于列表对象有自带的 sort 方法，如果能区分清楚 list.sort 与 sorted 之间区别那说明你已经能灵活运用了
			3.字典数据类型的运用
				做词频统计，用字典无疑是最合适的数据类型，单词作为字典的key,单词出现的次数作为字典的 value      ，很方便地就记录好了每个单词的频率，字典很像我们的电话本，每个名字关联一个电话号码。另外，字典最大的特点就是它的查询速度会非常快。理想情况下时间复杂度为O(1)，我是说理想情况，如果你想深入了解字典的话，建议看看这篇文章 https://www.laurentluce.com/posts/python-dictionary-implementation/
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			