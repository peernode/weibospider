# -*- coding: utf-8 -*-
import scrapy


class WeibouserSpider(scrapy.Spider):
    name = 'weibouser'
    allowed_domains = ['api.weibo.cn']
    start_urls = ['http://api.weibo.cn/']

    def parse(self, response):
        pass
