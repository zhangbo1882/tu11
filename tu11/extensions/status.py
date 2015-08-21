__author__ = 'Aaron'
import os
from scrapy import signals


class MyStatus(object):

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls("Aaron's Spider")
        crawler.signals.connect(obj.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
        return obj
    def spider_opened(self,spider):
        print("My Extensions: Spider is opened")
        pass
    def spider_closed(self,spider):
        print("My Extensions: Spider is closed")
        print("Couter: %d"%spider.counter)
        pass