# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyListItem(scrapy.Item):
    title_text = scrapy.Field()
    url = scrapy.Field()
