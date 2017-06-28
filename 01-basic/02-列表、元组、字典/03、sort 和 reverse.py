# -*- coding:UTF-8 -*-

'''
    demo1:把全班成绩按从小到大顺序排列出来,并找出 80 分以上的成绩
'''
# 成绩
# scores = [60,54,80,99,45,79,26,72,76,75,88,89,95]
# # 定义一个空列表用下存大于 80 分成绩
# youxiu = []
# print("未排序之前的成绩:%s "%scores)
# scores.sort()
# print("排序之后的成绩:%s "%scores)
# for score in scores:
#     if(score>=80):
#         youxiu.append(score)
# print("全班达到 80 分以上部共有 %d 个 %s "%(len(youxiu),youxiu))

'''
    demo2:把全班的成绩按从大到小排序
'''
# scores = [60,54,80,99,45,79,26,72,76,75,88,89,95]
# scores.sort(reverse=True)
# print("成绩按从大小到排序结果是: %s "%scores)


'''
    demo3:把名字按从小到大排序
'''

# names = ["Air","Beta","Beab","Dock","Coder","Zy","Higer"]
# print("原来的顺序：%s"%names)
# names.sort()
# print("按从小到大的排序：%s"%names)

'''
    demo4:全班成绩反向排序
'''

scores = [60,90,87,56,43,88]
print("反向排序之前的成绩：%s"%scores)
scores.reverse()
print("反向排序之后的成绩：%s"%scores)
