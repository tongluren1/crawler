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

    def __init__(self):
        self.redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        pass
        # key = hashlib.md5(item['host'] + item['port'])
        # self.redis_.hset('proxylist', key, json.dumps(item))
        # return item
