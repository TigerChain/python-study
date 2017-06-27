# -*- coding:UTF-8 -*-

'''
    demo1: 如果查询你的考试得了 90 分以上，就要以出去旅游，否则就在家里学习
'''
# 导入随机数模块
import random

print("查看考试成绩：1、查询 ")
inputStr = int(raw_input())
if(inputStr == 1):
    # 生成 80 - 100 的随机整数
    a = random.randint(80, 100)
    if a >=90:
        print("你的成绩是 %d 分，恭喜你可以出去旅游，地点随便选"%a)
    else:
        print("很遗憾，没有到 90 分，你还需要加油！争取下次旅游")
else:
    print("请输入正确的查询指令！！！")
