# -*- coding:UTF-8 -*-

'''
    demo1: 如果你有 10 万你就是十万元户，如果有 100 万就是百万富翁，有 1000万就是千万富翁，超过千万你真是土豪。
'''
money = int(raw_input("请输入你的财富，输入整数「代表万元」即可:"))
if money>10 and money<100:
    print("你是十万元户，努力哦")
elif money>=100 and money<1000:
    print("你小有成就，不错，都是百万富翁了")
elif money>=1000 and money<10000:
    print("千万富翁，约吗？")
elif money>=10000:
    print("靠，你真是土豪，带我装逼带我飞好吧")
else:
    print("得瑟啥呢，好好努力赚钱吧，还不好好的学习 python ，看看 TigerChain 的简书吧")
