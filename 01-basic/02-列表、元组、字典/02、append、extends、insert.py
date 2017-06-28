# -*- coding:UTF-8 -*-

'''
    demo1:在已有姓名列表中添加 WangWu ---> append
'''
# names = ["TigerChain","XiaoHua","ZhangSan"]
# print("append 之前的列表：%s"%names)
# names.append("WangWu")
# print("append 之后的列表：%s"%names)

'''
    在姓名列表第 2 个位置插入 LiSi ---> insert
'''

# names = ["TigerChain","XiaoHua","ZhangSan"]
# print("insert 之前的列表：%s"%names)
# names.insert(1,"LiSi")
# print("insert 之后的列表：%s"%names)

'''
    demo3:将两个班级里合并成一个班级「按姓名」 ---> extend
'''

names1 = ["TigerChain","XiaoHua","ZhangSan"]
names2 = ["LiSi","WangWu","ZhaoLiu"]
print("1 班的同学们：%s"%names1)
print("2 班的同学们：%s"%names2)
names1.extend(names2)
print("extend 之后合成一个班：%s"%names1)
