# -*- coding:UTF-8 -*-

'''
    demo1：输出1-100的和
'''
# # 定义结果 变量
# total = 0
# # 定义循环条件变量
# i = 1
# while i<=100:
#     # 把上一次的结果+1 然后赋值变成新的
#     total=total+i
#     # 循环+1
#     i+=1
# print ("1~100的和是：%d"%total)

'''
    demo2:输出1-100的奇数的和
'''
# total = 0
# i = 1
# while i<=100:
#     total = total+i
#     # 奇数的算法
#     i+=2
# print("1~100的所有奇数和是：%d"%total)
#


'''
    demo3:输入用户名和密码直到正确为止
'''
# # 输入用户名
# username = raw_input('请输入用户名:')
# # 输入用户密码
# password = raw_input('请输入密码:')
#
# # 如果用户名和密码不对，那么就提示错误，再次输入
# while username!='admin' or password!='123456':
#     print('用户名或密码错误，请重新输入')
#     username = raw_input('请输入用户名:')
#     password = raw_input('请输入密码:')
# # 如果输入成功，则提示
# print("欢迎 %s 登录"%username)


'''
    demo4:用户不断的输入一个数字，直到输入 bye 则退出程序
'''

# while True:
#     num = raw_input("请输入一个数字「直到输入 bye 就结束了」：")
#     if num=='bye':
#         print('结束了')
#         break
#     else:
#         print num

'''
    demo5:使用 while 嵌套打印九九乘法表
'''
#初始一个变量x
x=1
#判断x小于等于9
while x<=9:
    #初始一个变量y
    y=1
    #确定y的循环次数，小于等于x
    while y<=x:
        #格式化打印输出
        print y,'*',x,'=',y*x,' ',
        #计数器
        y+=1
    #打印换行,前面用逗号隔开过，没有这行代码就连成一片了。
    print
    #外围的另一个计数器
    x+=1
