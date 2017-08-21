# -*- coding: UTF-8 -*-
'''
    1、定义函数后面的()中的参数称为形参
    2、调用函数的方法，传递给函数的参数称为实参
'''
'''
    demo1:定义一个函数，输入三条边，看其能不能组成三角形
'''
# def sanjiao(x,y,z):#实际开发中不要使用拼音作为函数名
#     if(x+y>z and x+z>y and y+z>x):
#         print("%d,%d,%d 可以组成三角形"%(x,y,z))
#         if(x==y==z):
#             print("并且这是一个等边三角形")
#         elif(x==y or y==z or x==z):
#             print("并且这是一个等腰三角形")
#         elif(x*x+y*y==z*z or y*y+z*z==x*x or x*x+z*z==y*y):
#             print("并且这是一个直角三角形")
#         else:
#             print("并且这是一个普通的其解形")
#     else:
#         print("不好意思，你三角形的概念好好学学吧，不能构成三角形")
#
# print("请输入三角形的三条边")
#
# x = raw_input("第一条边：")
# y = raw_input("第二条边：")
# z = raw_input("第三条边：")
#
# sanjiao(int(x),int(y),int(z))

'''
    demo2:输入三个数，输出最大数
'''

def getMax(x,y,z):
    max = x
    if(y>max):
        max=y
        if(z>max):
            max=z

    return max

a = raw_input("请输入第一个数：")
b = raw_input("请输入第二个数：")
c = raw_input("请输入第三个数：")

print("%d,%d,%d 中最大的数是：%d"%(int(a),int(b),int(c),getMax(int(a),int(b),int(c))))
