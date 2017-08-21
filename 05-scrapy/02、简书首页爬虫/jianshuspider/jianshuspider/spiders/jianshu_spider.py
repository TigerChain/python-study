# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from jianshuspider.items import CnblogItem

class CnblogSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "https://www.cnblogs.com/"
    ]
    def parse(self, response):
        print("-----------------------------")
        selector = Selector(response)
        divs = selector.xpath("//div[@class='post_item']")
        print("xxxxx %s"%len(divs))

        for div in divs:
            cnblogItem = CnblogItem()
            print("***************")
            # 用户头像地址
            author_avator_url = div.xpath('div[@class="post_item_body"]/p[@class="post_item_summary"]/a/img/@src').extract()
            print("头像地址是：%s"%author_avator_url)
            cnblogItem['author_avator_url'] = "https:".join(author_avator_url)

            # 文章标题地址
            article_title_url = div.xpath('div[@class="post_item_body"]/h3/a[@class="titlelnk"]/@href').extract()
            cnblogItem['article_title_url'] = article_title_url
            print("文章标题地址：%s"%article_title_url)

            # 文章标题
            article_title = div.xpath('div[@class="post_item_body"]/h3/a[@class="titlelnk"]/text()').extract()
            cnblogItem['article_title'] = article_title
            print("文章标题：%s"%article_title)

            # 文章简介
            article_des = div.xpath('div[@class="post_item_body"]/p/text()').extract()
            cnblogItem['article_des'] = article_des
            print("文章简介：%s"%article_des)

            # 作者
            author_name = div.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/a[@class="lightblue"]/text()').extract()
            cnblogItem['author_name'] = author_name

            # 作者链接
            atuhor_url = div.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/a[@class="lightblue"]/@href').extract()
            cnblogItem['atuhor_url'] = atuhor_url
            # 生成条目
            yield cnblogItem
