#!/usr/bin python
# -*- encoding: utf-8 -*-
# @Author: Joe
# @File: proxylist_spider.py
# @Time: 2021/2/5 15:42
import scrapy

from crawler.items import ProxyListItem


class ProxyList(scrapy.Spider):
    name = 'proxylist'
    start_urls = ['https://baike.baidu.com/item/%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92%E8%82%BA%E7%82%8E/24282529?fromtitle=%E6%96%B0%E5%86%A0&fromid=55458316&fr=aladdin']

    def parse(self, response):
        item = ProxyListItem()
        item['header'] = response.css('title::text').extract()
        pass

        next_pages = response.css('a::attr(href)').extract()
        for page in next_pages:
            pass
            # if



