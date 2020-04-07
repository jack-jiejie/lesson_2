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
        print("抓取的url地址是：" + str(response.url))
        # 帖子的标题
        title = response.css(".core_title_txt.pull-left.text-overflow::text").extract()
        print("当前获取的帖子的主题是：" + str(title))

        if title:
            # 获取的作者们（list）
            author_list = response.css(".p_author_name.j_user_card::text").extract()

            # 获取帖子的内容
            content_list = response.css(".d_post_content.j_d_post_content").extract()

            bbs_sendtime_list, bbs_floor_list = self.get_sendtime_and_floor(response)
            for i in range(len(author_list)):
                print(author_list[i])
                print(content_list[i])
                print(bbs_floor_list[i])
                print(bbs_sendtime_list[i])
        # 详情页面的翻页
        # 拿到详情页面的url的list
        detail_next_page_list = response.css(".l_pager.pager_theme_4.pb_list_pager a::attr(href)").extract()


        if detail_next_page_list:
            for next_page in detail_next_page_list:
                yield scrapy.Request(url=parse.urljoin(response.url, next_page), callback=self.parse_detail)



    def get_sendtime_and_floor(self, response):
        # 获取帖子的时间和楼数
        bbs_sendtime_and_floor_list =  response.css(".tail-info::text").extract()
        # 遍历列表，取出来自
        for lz in bbs_sendtime_and_floor_list:
            if lz == "来自":
                bbs_sendtime_and_floor_list.remove(lz)

        # 存储发帖时间
        bbs_sendtime_list = []

        # 存储发帖楼数
        bbs_floor_list = []

        i = 0 # 记录bbs_sendtime_and_floor_list的索引位置
        for bbs_sendtime_and_floor in bbs_sendtime_and_floor_list:
            if i%2 == 0:
                bbs_floor_list.append(bbs_sendtime_and_floor)

            if i%2 == 1:
                bbs_sendtime_list.append(bbs_sendtime_and_floor)

            i += 1
        return bbs_sendtime_list, bbs_floor_list












