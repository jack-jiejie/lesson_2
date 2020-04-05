# -*- coding: utf-8 -*-
from urllib import parse

import scrapy


class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E9%98%B2%E8%AF%88%E9%AA%97']

    def parse(self, response):
        # 页面中帖子的url数组
        url_list = response.css(".j_th_tit::attr(href)").extract()



        # 遍历帖子中的URL地址， 然后去解析帖子中的具体内容
        for url in url_list:
            # url地址拼接
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

        # 获取下一页的url， 然后交给spider继续处理
        next_url = response.css(".next.pagination-item::attr(href)").extract()[0]

        if next_url:
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse)




    def parse_detail(self, response):
        pass