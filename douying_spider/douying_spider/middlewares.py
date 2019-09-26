# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

from douying_spider.settings import PROXY_LIST

class RandomProxy(object):
    """代理中间件"""

    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)
        request.meta['proxy'] = proxy['ip_port']
        # return None
