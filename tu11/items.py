# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tu11Item(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
    pass
