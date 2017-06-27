# -*- coding:UTF-8 -*-

'''
    demo1:基本的输出
'''

# # python2 上可以支持，在python3上会报错
# print "hello world"
#
# # python2 和 3 上都支持
# print("hello world")
#
# # 输出多个字符串在 python2 中去掉 () 即可
# print("hello world","Hi TigerChain")
#
# x = 13
# print x
#
# y = 13.56
# print y
#


'''
    demo2:打印美女
'''
# print("******************************************************************")
# print("*                       .::::.                                   *")
# print("*                    .::::::::.                                  *")
# print("*                    :::::::::::                                 *")
# print("*                 ..:::::::::::'                                 *")
# print("*              '::::::::::::'                                    *")
# print("*                .::::::::::                                     *")
# print("*           '::::::::::::::..                                    *")
# print("*                ..::::::::::::.                                 *")
# print("*              ``::::::::::::::::                                *")
# print("*             ::::``:::::::::'        .:::.                      *")
# print("*              ::::'   ':::::'       .::::::::.                  *")
# print("*            .::::'      ::::     .:::::::'::::.                 *")
# print("*           .:::'       :::::  .:::::::::' ':::::.               *")
# print("*          .::'        :::::.:::::::::'      ':::::.             *")
# print("*         .::'         ::::::::::::::'         ``::::.           *")
# print("*     ...:::           ::::::::::::'              ``::.          *")
# print("*    ```` ':.          ':::::::::'                  ::::..       *")
# print("*                       '.:::::'                    ':'````..    *")
# print("******************************************************************")


'''
    demo3:格式化输出使用 %+
'''

# x = 0x123
# print("0x123 的进制输出---十六进制:%x,十进制:%d,八进制:%o"%(x,x,x))
#
# y = '你好'
# c = 13.56
# d = 13
#
# print("%s,%f,%d"%(y,c,d))
#

'''
    demo4:格式化输出使用 fromat()
'''
# print('{0} {1} {2}').format('Hello','ThgerChain',"Good")



'''
    demo5:一个简单的乘法运算
'''

# num = raw_input("请输入数字:")
# print(num+"*2=%d"%(int(num)*2))

'''
    demo6:模拟一个简单的取钱过程
'''
# 定义密码输入次数
inputPasscount = 0
# 提示你是否插入银联卡 输入 yes 即可
chaka = raw_input('你是否插入银联卡：')
if(chaka=='yes'):
    password = int(raw_input('请输入卡密码：'))
    # 只给你三次输入密码的机会，错了卡就被吞了
    while inputPasscount < 3:
        if(password==123456):
            money = raw_input('输入你要取的钱数：')
            if money.isdigit():# 全部是数字则正确
                print("你成功的取了 %d "%(int(money))+"元")
                break
            else:
                print("请输入正确的金额")
        else:
            if inputPasscount == 2:
                print("密码输错三次，卡被锁定，请联系管理员")
                break
            password = int(raw_input('输入的密码错误，请重新输入：'))
            inputPasscount += 1
