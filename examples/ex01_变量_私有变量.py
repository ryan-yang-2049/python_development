#!/usr/bin/env python
#coding:utf-8
'''
单下划线变量，Pyhthon规定为内部变量（私有变量），from M import * 时，这种变量并不会导入进来
特殊变量命名

1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示
如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。
2、 __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），
调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
3、 __xx__定义的是特列方法。
在这里强调说一下私有变量,python默认的成员函数和成员变量都是公开的,
没有像其他类似语言的public,private等关键字修饰.但是可以在变量前面加上两个下划线"_",这样的话函数或变量就变成私有的.
这是python的私有变量轧压(这个翻译好拗口),英文是(private name mangling.) **情况就是当变量被标记为私有后,
在变量的前端插入类名,再类名前添加一个下划线"_",即形成了_ClassName__变量名.**
'''

class Foo(object):
    boo = 40
    _boo = 50
    __boo = 60
    def __init__(self):
        self.__booo = 70

    def __test(self):
        print("__test")

if __name__ == '__main__':
    print("boo:",Foo.boo)
    print("_boo:",Foo._boo)
    print("_Foo__boo:",Foo._Foo__boo)
    foo = Foo()
    print("_Foo__booo:",foo._Foo__booo)
    foo._Foo__test()




