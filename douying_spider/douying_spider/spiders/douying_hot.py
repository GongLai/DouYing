# -*- coding: utf-8 -*-
import scrapy
import json
import time

from ..items import DouYingVideoSpiderItem


class DouyingHotSpider(scrapy.Spider):
    name = 'douying_hot'
    allowed_domains = ['snssdk.com']
    start_urls = ['https://aweme.snssdk.com/aweme/v1/hot/search/list/']

    def parse(self, response):
        data_json = json.loads(response.text)
        datas = data_json['data']['word_list']
        for data in datas:
            temp = {}
            # 榜单更新时间
            temp['update_time'] = data_json['data']['active_time']
            # 榜单排名
            temp['video_position'] = data['position']
            # 热门标题
            temp['hot_title'] = data['word']
            # 视频热度
            temp['hot_value'] = data['hot_value']
            video_url = 'https://aweme.snssdk.com/aweme/v1/hot/search/video/list/?hotword={}'.format(temp['hot_title'])

            yield scrapy.Request(url=video_url, callback=self.get_video_parse, meta={'item': temp}, encoding='utf-8')

    def get_video_parse(self, response):
        temp = response.meta['item']
        item = DouYingVideoSpiderItem()
        html = json.loads(response.text)

        # 榜单更新时间
        item['update_time'] = temp['update_time']
        # 榜单排名
        item['video_position'] = temp['video_position']
        # 热门标题
        item['hot_title'] = temp['hot_title']
        # 视频热度
        item['hot_value'] = temp['hot_value']

        # 作者名
        item['author_name'] = html['aweme_list'][0]['author']['nickname']
        # 作者抖音号
        item['short_id'] = html['aweme_list'][0]['author']['short_id']
        # 作者签名
        item['signature'] = html['aweme_list'][0]['author']['signature']
        # 视频ID
        item['video_id'] = html['aweme_list'][0]['aweme_id']
        # 视频标题
        item['video_title'] = html['aweme_list'][0]['desc']
        # 视频发布时间
        ltime = time.localtime(html['aweme_list'][0]['create_time'])
        item['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        # 视频链接
        item['video_link'] = html['aweme_list'][0]['share_url']
        # 视频拍摄地点
        # item['poi_name'] = html['aweme_list'][0]['poi_info']['poi_name']
        # 背景音乐标题
        item['music_title'] = html['aweme_list'][0]['music']['title']
        # 背景音乐链接
        item['music_link'] = html['aweme_list'][0]['music']['play_url']['uri']
        # 点赞数
        item['Like_count'] = html['aweme_list'][0]['statistics']['digg_count']
        # 评论数
        item['comment_count'] = html['aweme_list'][0]['statistics']['comment_count']
        # 转发数
        item['share_count'] = html['aweme_list'][0]['statistics']['share_count']

        yield item
