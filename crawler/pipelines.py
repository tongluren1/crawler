# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json
import hashlib

class CrawlerPipeline(object):

    redis_ = ''

    def open_spider(self, spider):
        self.redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)
        print(self.redis_)

    def process_item(self, item, spider):
        key = hashlib.md5(item['host'] + item['port'])
        print(key)
        self.redis_.hset('proxylist', key, json.dumps(item))
        return item
