# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class CrawlerPipeline(object):

    redis_ = ''

    def open_spider(self, spider):
        self.redis_ = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        self.redis_.hset('baidu_res', item['url'], item['title_text'])
        return item
