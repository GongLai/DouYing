# -*- coding: utf-8 -*-
import scrapy


class DouyingSpider(scrapy.Spider):
    name = 'douying'
    allowed_domains = ['snssdk.com']
    start_urls = ['http://snssdk.com/']

    def parse(self, response):
        pass
