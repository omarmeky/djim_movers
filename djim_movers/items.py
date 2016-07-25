# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DjimMoversItem(scrapy.Item):
    name = scrapy.Field()
    symbol = scrapy.Field()
    change = scrapy.Field()
    percentChange = scrapy.Field()
