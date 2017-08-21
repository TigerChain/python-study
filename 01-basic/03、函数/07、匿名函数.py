# -*- coding:utf-8 -*-
'''
    demo1:使用 lambda 来创建一个加法函数
'''
# # 定义一个 labmda 表达式
# sum = lambda a,b:a+b
# print sum(1,4)


'''
    demo2:使用 lambda 作为方法参数「函数式编程」
'''
# 定义一个函数，参数分别是普通变量和一个函数
def fun(a,b,func):
    return func(a,b)
result = 0

e = ''

while True:
    if e=='e':
        break
    if e == 'c' or e =='':
        a = int(raw_input("请输入一个整数 a = "))
        b = int(raw_input("请输入一个整数 b = "))
        calc = raw_input("选择 + - * / 其中一项:")
        # 加法运算
        if calc == '+':
            result = fun(a,b,lambda a,b:a+b)
        # 减法运算
        elif calc == '-':
            result = fun(a,b,lambda a,b:a-b)
        # 乘法运算
        elif calc == "*":
            result = fun(a,b,lambda a,b:a*b)
        else:
        # 除法运算
            if b==0:
                print("被除数不能为0")
                continue 
            result = fun(a,b,lambda a,b:a/b)
        print result
        e = raw_input("退出请输入 e 继续请输入 c : ")
