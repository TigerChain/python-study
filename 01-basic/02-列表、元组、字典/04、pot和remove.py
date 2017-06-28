# -*- coding:UTF-8 -*-
'''
    demo1:移除姓名列表中最后一个姓名
'''
# names = ["ZhangSan","LiSi","WangWu"]
# print("移除之前的姓名列表：%s"%names)
# names.pop()
# print("移除之后的姓名列表：%s"%names)

'''
    demo2:删除指定位置的姓名
'''
# names = ["ZhangSan","LiSi","WangWu"]
# print("移除之前的姓名列表：%s"%names)
# names.pop(1)
# print("移除之后的姓名列表：%s"%names)


'''
    demo3:输入你想要删除的姓名「前提是列表中有」
'''

names = ["TigerChain","ZhangSan","Lisi","WangWu","ZhaoLiu"]
print("列出所有的名字:%s "%names)
input_name = raw_input("输入你想要删除的名字：")
for name in names:
    if(name==input_name):
        names.remove(name)
print("删除之后名字列表：%s"%names)
