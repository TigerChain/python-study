# -*- coding:UTF-8 -*-
'''
    demo1:循环打印字条串中每个值
'''
# name = 'TigerChain'
# for x in name:
#     print x

'''
    demo2:定义一个姓名列表，然后逐个打印出来
'''
# names=["张三","李四","王五"]
# for name in names:
#     print name

'''
    demo3:打印九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print j, 'x', i, '=', j*i ,'\t',
    print ''

print range(0,10,2)
