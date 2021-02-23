# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json
import hashlib

class CrawlerPipeline(object):

    # def process_item(self, item, spider):
    #     redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)
    #     key = hashlib.md5(item['host'] + item['port'])
    #     redis_.hset('proxylist', key, json.dumps(item))
    #     return item
    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item