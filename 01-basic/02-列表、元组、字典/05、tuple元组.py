# -*- coding:UTF-8 -*-

'''
    demo1:定义一个姓名元组，并且遍历出每个值
'''
# names = ("ZhangSan","LiSi","WangWu","ZhaoLiu")
# print(names)
# for name in names:
#     print("我是：%s "%name)

'''
    demo2:计算 ZhangSan 在姓名元组中出现在次数
'''

# names = ["ZhangSan","LiSi","ZhangSan","WangWu","ZhangSan"]
# # 把一个列表转化成元组使用 tuple 方法
# new_names = tuple(names)
# print(new_names)
# print("张三出现的次数：%d"%new_names.count('ZhangSan'))

'''
    demo3:修改元组组 LiSi 为 ZhaoLiu
'''
# names = ["ZhangSan","LiSi","ZhangSan","WangWu","ZhangSan"]
# new_names = tuple(names)
# # 尝试修改 LiSi 为 ZhaoLiu
# new_names[1] = "ZhaoLiu"
# print new_names
#
# # 此 demo 会挂，因为元组是不允许修改的


'''
    demo4:比较两个元组 cmp 方法
'''

tup1 = (1,2,3)
tup2 = (2,3,4)

tup3 = (1,"xyz")
tup4 = (1,"xyz")

print("元组是：%r"%tup1)

print cmp(tup1,tup2)

print cmp(tup3,tup4)

print cmp(tup2,tup1)
