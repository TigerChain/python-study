# -*- coding:utf-8 -*-

'''
    demo1:变量的作用域
'''
# def add(x,y):
#     z = x+y
#     print z
# def new_add():
#     print("===1====")
#     z+=4
#     print("===3===")
#     print z
#
# add(1,2)
# new_add()

'''
    demo2:局部变量和全局变量
    在方法中声明的变量叫做局部变量，只能在本方法中使用，在方法调用之前声明的变量叫做
    全局变量

    demo 1 中定义的 x 是局部变量还是修改全局变量呢 ？我们看一下
'''
# x = 0
# def demo1():
#     # global x  如果不使用 x 声明，这里的 x  指的就是局部变量 x， 和外面的 x 没有一点毛关系
#     x = 100
#     print("x 的值是%d "%x)
# def demo2():
#     print("x 的值是%d "%x)
#     pass
#
# demo1()
# demo2(）

'''
    demo3:可变类型型作为变量修改看结果
'''
# 定义一个列表「可变类型」
a = [1,2,3,4]

def demo1():
    a.append(5)
    print("a 的内容是 %s"%a)
def demo2():
    print("a 的内容是 %s"%a)
    pass
demo1()
demo2()






















