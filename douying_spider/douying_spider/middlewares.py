# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

from douying_spider.settings import USER_AGENT, PROXY_LIST


class RandomUserAgent(object):
    """随机User-Agent中间件"""

    def process_request(self, request, spider):

        ua = random.choice(USER_AGENT)
        request.headers['User-Agent'] = ua


class RandomProxy(object):
    """代理中间件"""

    def process_request(self, request, spider):

        proxy = random.choice(PROXY_LIST)
        request.meta['proxy'] = proxy['ip_port']
