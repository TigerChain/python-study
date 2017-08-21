# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 作者头像地址
    author_avator_url = scrapy.Field()

    # 文章标题
    article_title = scrapy.Field()
    # 文章标题地址
    article_title_url = scrapy.Field()
    # 文章简介
    article_des = scrapy.Field()

    # 作者姓名
    author_name = scrapy.Field()

    # 作者链接

    atuhor_url = scrapy.Field() 

    # # 文章内容图片
    # article_img_url = scrapy.Field()
    # # 文章浏览数量
    # article_see_count = scrapy.Field()
    # # 文章回复数量
    # article_reply_count = scrapy.Field()
    # # 文章喜欢数量
    # article_love_count = scrapy.Field()

    # # 作者发送文章时间
    # author_send_time = scrapy.Field()
