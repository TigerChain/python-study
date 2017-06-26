# -*- coding: UTF-8 -*-

'''
    demo1:将 x 变量 赋值给 y 变量，查看内存分配情况

'''

# x = 5
# y = x
# print ("x=%d"%(x))
# print ("x的地址是:%d"%(id(x)))
#
# print ("y=%d"%(y))
# print ("y的地址是:%d"%(id(y)))

'''
    demo2:修改变量 x 的的值，查看内存分配情况，

    结论：由此 demo 可以看到，值不相同，代表不相同的地址，
    修改 x 经分别的掷指向了两个不同的地址
'''

# x = 5
#
# print ("x=%d"%(x))
# print ("x的地址是:%d"%(id(x)))
#
# x = 8
#
# print ("x=%d"%(x))
# print ("x的地址是:%d"%(id(x)))

'''
    demo3: 变量指向赋相同的值,查看内存分配。
    结论：值相同，则变量对应的内存地址就一定相同
'''

x = 5
y = 5

print ("x=%d"%(x))
print ("x的地址是:%d"%(id(x)))

print ("y=%d"%(y))
print ("y的地址是:%d"%(id(y)))
