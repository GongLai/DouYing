# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyingHotSpiderItem(scrapy.Item):
    # define the fields for your item here like:

    # 视频排名
    video_position = scrapy.Field()
    # 热门标题
    hot_title = scrapy.Field()
    # 视频热度
    hot_value = scrapy.Field()


class DouYingVideoSpiderItem(scrapy.Item):
    """视频信息"""

    # 榜单更新时间
    update_time = scrapy.Field()
    # 榜单排名
    video_position = scrapy.Field()
    # 热门标题
    hot_title = scrapy.Field()
    # 视频热度
    hot_value = scrapy.Field()
    # 作者名
    author_name = scrapy.Field()
    # 作者抖音号
    short_id = scrapy.Field()
    # 作者签名
    signature = scrapy.Field()
    # 视频ID
    video_id = scrapy.Field()
    # 视频标题
    video_title = scrapy.Field()
    # 视频发布时间
    create_time = scrapy.Field()
    # 视频链接
    video_link = scrapy.Field()
    # 视频拍摄地点
    poi_name = scrapy.Field()
    # 背景音乐标题
    music_title = scrapy.Field()
    # 背景音乐链接
    music_link = scrapy.Field()
    # 点赞数
    Like_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 转发数
    share_count = scrapy.Field()


"""
gender



"""
