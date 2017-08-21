# -*- coding:utf-8 -*-
'''
    demo1:对add 函数作文档说明
'''
def addFun(a,b):
    ''' 这个函数是返回两个整数的和 '''
    return a+b
# help(addFun) 显示方法体中的文档说明
print __doc__
