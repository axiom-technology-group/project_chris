# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from Auto51.settings import user_agent_list
from Auto51.items import ijiaotongItemLoader,ijiaotongItem

from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse

class IjiaotongSpider(CrawlSpider):
    name = 'ijiaotong'
    allowed_domains = ['www.ijiaotong.com']
    start_urls = ['https://www.ijiaotong.com/']
    import random
    random_agent = random.choice(user_agent_list)
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'UM_distinctid=16b69b9729ad3-051b68dffd6c81-4d045769-1fa400-16b69b9729b668; CNZZDATA1261099144=1442246537-1560919143-%7C1560919143; CNZZDATA391769=cnzz_eid%3D386581157-1560846896-%26ntime%3D1560919009; Hm_lvt_77f43391fff22dd5be4cd645339d6a52=1560846890,1560910293; Hm_lpvt_77f43391fff22dd5be4cd645339d6a52=1560919702',
        'Host':'www.ijiaotong.com',
        'Referer':'https://www.ijiaotong.com/list/5.html',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':random_agent,
    }
    rules = (
        Rule(LinkExtractor(allow=r'view/\d+'), callback='parse_item',follow=False),
        # 先去匹配列表页链接
        Rule(LinkExtractor(allow=r'list/\d+'), follow=True),
        # 匹配详情页数据
    )

    def parse_item(self, response):
        item_loader = ijiaotongItemLoader(item=ijiaotongItem(), response=response)
        print(response.url)
        item_loader.add_xpath("publishtime", "//*[@class='qf b dx']/span[1]/text()")
        item_loader.add_xpath("title", "//*[@class='qf b dx']/h1/text()")
        item_loader.add_xpath("source", "//*[@class='qf b dx']/span[2]/text()")
        item_loader.add_css("content", ".b div div p::text")
        # item_loader.add_css("title", ".car-title h1::text")
        # item_loader.add_css("title", ".car-title h1::text")
        item_loader.add_value("url", response.url)
        jt_item = item_loader.load_item()
        yield jt_item
