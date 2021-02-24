#!/usr/bin python
# -*- encoding: utf-8 -*-
# @Author: Joe
# @File: proxylist_spider.py
# @Time: 2021/2/5 15:42
import scrapy
import redis
from urllib.parse import urlparse

from crawler.items import ProxyListItem


class ProxyList(scrapy.Spider):
    name = 'proxylist'
    # start_urls = ['http://proxylist.fatezero.org/proxy.list']
    start_urls = ['https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%96%B0%E5%86%A0']

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
    }

    def start_requests(self):
        redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)
        start_url_ = redis_.lpop('baidu_url')
        if start_url_ is None:
            start_url_ = 'http://top.baidu.com/buzz?b=1&fr=topindex'
        yield scrapy.Request(start_url_, self.parse)

    def parse(self, response):
        redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)
        href_list = response.xpath('//a/@href').getall()
        for href in href_list:
            if href[0:2] == './' or href[0:2] == '/':
                tmp_url_ = 'http://' + urlparse(response.request.url).netloc + '/' + href.strip('.').strip('/')
            elif href[0:4] == 'http':
                tmp_url_ = href
            else:
                tmp_url_ = False
            if tmp_url_:
                redis_.lpush('baidu_url', tmp_url_)

        item = ProxyListItem()
        item['url'] = response.request.url
        item['title_text'] = response.xpath('//title/text()').get()
        yield item

        next_url = redis_.lpop('baidu_url')
        if not next_url is None:
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
        else:
            print('url empty!')
            quit()
