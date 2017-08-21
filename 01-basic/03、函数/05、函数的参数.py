# -*- coding:utf-8 -*-

'''
    demo1:缺省参数
'''

#def demo1(age,name='TigerChain'):
#    print("name = %s"%name)
#    print("age = %d"%age)
##demo1(12)
#demo1(12,'TigerChain001')

'''
    demo2:可变参数「不定长参数」
'''

#def demo2(param1,param2,*param3):
#    print "param1 = ",param1
#    print "param2 = ",param2
#    print "param3 = ",param3
#demo2(1,2,3,4,5,6)

'''
    demo3:可变参数二
'''

def demo3(param1,param2,*param3,**param4):
    print "param1 = ",param1
    print "param2 = ",param2
    print "param3 = ",param3
    for key,value in param4.items():
        print key ," = ",value

#demo3(1,2,3,4,5,name='TigerChain',age=12,address='中国')
c = (7,8,9)
d = {"name":"TigerChain","age":12,"sex":"男"}
# demo3(1,2,3,c,d)
demo3(1,2,3,*c,**d)
