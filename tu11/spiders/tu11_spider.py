__author__ = 'Aaron'
#coding:utf-8
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from tu11.items import Tu11Item
import re
class tu11Spider(CrawlSpider):
    name = "tu11"
    base_url = 'http://www.tu11.com'
    start_urls = [
        base_url+'/new100.html'
    ]
    counter = 0
    def generate_request_with_image_name(self, url, image_name=""):
        item = Tu11Item()
        if image_name=="":
            names = url.split("/")
            name = names[-3]+"_"+names[-2]+"_"+names[-1].split(".")[0]
            item['image_name'] = name.encode("utf-8")
        else:
            item['image_name'] = image_name
        request = Request(url, callback=self.parse_item)
        request.meta['item'] = item
        return request

    def parse_item(self, response):
        item = response.meta['item']
        lines = Selector(response).xpath('//div[@class="page-list"]/p/img/@src').extract()
        item['image_urls'] = lines
        yield item
        nextLines = Selector(response).xpath('//div[@class="dede_pages"]/ul/li/a/@href').extract()
        for nextLine in nextLines:
            if re.search('html',nextLine):
                nextUrl = ""
                elems = response.url.split("/")
                for elem in elems[:len(elems)-1]:
                    nextUrl += elem+"/"
                nextUrl +=nextLine
                yield self.generate_request_with_image_name(nextUrl, item['image_name'])


    def parse(self, response):
        lines = Selector(response).xpath('//li/a/@href').extract()
        for line in lines:
            if re.search('html',line):
                self.counter += 1
                nextUrl = self.base_url+line
                yield self.generate_request_with_image_name(nextUrl)
                return