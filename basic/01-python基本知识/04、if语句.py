# -*- coding:UTF-8 -*-
'''
    demo1：如果你 18 岁了，你就可以看血腥电影了
'''
# a = int(raw_input('请输入你的年龄:'))
# if a>=18:
#     print("你可以看血腥的电影了")


'''
    demo2 如果你 18 岁并且不害怕恐怖事件，那么你可以看血腥电影
'''
# 输入年龄
a = raw_input('你是否年满18岁？回答 yes 或 no :')
if a=='yes': # 年龄满足
    print('年龄符合了！请继续输入问题')
    # 对恐怖事件的看法
    b = raw_input('面对恐怖电影你会非常害怕吗？回答 yes 或 no :')
    if b =='yes': #满足条件
        print("你可以看恐怖血腥的电影了!!!")
