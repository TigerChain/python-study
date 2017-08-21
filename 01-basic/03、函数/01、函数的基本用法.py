# -*- coding:UTF-8 -*-

'''
    demo1:定义一个返回两个整数和的函数
'''
# def addFun(x,y):
#     return x+y
#
# # 调用
# print(" 5+6 = %d"%addFun(5,6))


'''
    demo2:将后一个姓名列表添加到第一个列表的末尾
'''
names = ["tigerchain","xiaoming","liubing"]

print("原始的姓名列表是：%s"%names)

def appendList(lists):
    names.append(lists)
    print("添加后的姓名列表是：%s"%names)

new_names = ["sulei","xiaozhang"]
appendList(new_names)

print("最终的姓名列表是: %s "%names)
