# -*- coding:utf-8 -*-

'''
    demo1:按照拼音查找字
'''
# dic = {"zhangsan":"张三","lisi":"李四","piaoliang":"漂亮"}
#
# print(dic['zhangsan'])
# print(dic['lisi'])
# print(dic['piaoliang'])

'''
    demo2:修改字典中的 age
'''

# xiaoli = {"name":"xiaoli","age":22,"address":"中国陕西"}
# print("小李错误的年龄：%d"%xiaoli["age"])
# # 修改年龄
# xiaoli["age"] = 23
# print("小李的年龄修改为：%d"%xiaoli["age"])

'''
    demo3:demo3:遍历输出字典中的 key 值
'''
# TigerChain = {"name":"TigerChain","age":18,"address":"中国陕西","love":["看书","游泳","爬山"]}
# for key in TigerChain.keys():
#     print("TigerChain 字典中的key:%s"%key)

'''
    demo4:遍历字典中的 所有的 values
'''

# dict = {"name":"zhangsan","age":18,"height":"165CM"}
# print dict
# for value in dict.values():
#     print("dict 字典中的 value: %s"%value)
#

'''
    demo5：修改字典中某个 key 所对应的值
'''

dict = {"name":"zhangsan","age":18,"height":"165CM"}
print("修改之前的字典：%r"%dict)
dict["name"] = "junjun"
print("修改之后的字典：%r"%dict) 
