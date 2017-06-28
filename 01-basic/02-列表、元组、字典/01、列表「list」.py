# -*- coding:UTF-8 -*-

'''
    demo1:输出姓名列表的值
'''
# # 定义一个姓名列表
# names = ["TigerChain","XiaoHua","ZhangSan"]
# # 输出每个列表的值
#
# print(names[0])
# print(names[1])
# print(names[2])

'''
    demo2:遍历输出姓名列表的值
'''

# names = ["TigerChain","XiaoHua","ZhangSan"]
#
# print("列表的长度是：%d"%len(names))
#
# # 遍历输出
# for name in names:
#     print name

'''
    demo3:while 遍历输出姓名列表
'''
names = ["TigerChain","XiaoHua","ZhangSan"]

size = len(names)
i = 0
while i<size:
    print(names[i])
    i+=1
