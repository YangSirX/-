# -*- coding: utf-8 -*-
import scrapy
"""//ul[@class="top-list  fn-clear"]/li/h5/text()"""

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):
        pass
