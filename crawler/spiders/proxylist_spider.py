#!/usr/bin python
# -*- encoding: utf-8 -*-
# @Author: Joe
# @File: proxylist_spider.py
# @Time: 2021/2/5 15:42
import scrapy
import json

from crawler.items import ProxyListItem


class ProxyList(scrapy.Spider):
    name = 'proxylist'
    start_urls = ['http://proxylist.fatezero.org/proxy.list']

    def parse(self, response):
        item = ProxyListItem()
        text = response.text.replace('}', '},')
        obj = json.loads('[' + text.strip().strip(',') + ']')
        for obj_ in obj:
            if type(obj_['export_address']) == type([]):
                item['export_address'] = '-'.join(obj_['export_address'])
            else:
                item['export_address'] = obj_['export_address']
            item['response_time'] = obj_['response_time']
            item['country'] = obj_['country']
            item['type'] = obj_['type']
            item['fro'] = obj_['from']
            item['host'] = obj_['host']
            item['anonymity'] = obj_['anonymity']
            item['port'] = obj_['port']
            return item
