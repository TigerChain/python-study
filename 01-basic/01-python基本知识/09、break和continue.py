# -*- coding:UTF-8 -*-

'''
    demo1:demo1:输入字符串，遇到 o 就退出
'''
# a = raw_input("输入字符串「直到输入 o 就不会输出 o 之后的字符」:")
# for x in a:
#     if x=='o':
#         break
#     print x

'''
    demo2:输入字符串，只过滤不输出 o 其它的输出
'''
a = raw_input("输入字符串「输出过滤 o 之后的字符」:")
for x in a:
    if x=='o':
        continue
    print x
