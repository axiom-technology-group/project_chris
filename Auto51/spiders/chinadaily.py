# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from Auto51.settings import user_agent_list
from Auto51.items import chinadailyItemLoader,chinadailyItem

from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse

class ChinadailySpider(CrawlSpider):
    name = 'chinadaily'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = ['http://cn.chinadaily.com.cn//']
    # import random
    # random_agent = random.choice(user_agent_list)
    # headers = {
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Encoding':'gzip, deflate, sdch',
    #     'Accept-Language':'zh-CN,zh;q=0.8',
    #     'Cache-Control':'no-cache',
    #     'Connection':'keep-alive',
    #     'Cookie':'wdcid=56868a9990987035; UM_distinctid=16b787856f7336-047845d08958a9-4d045769-1fa400-16b787856f827a; U_COOKIE_ID=21963a62618cae231ad0238126f82386; pt9e8b=vt=1561094281095&cad=; wdlast=1561095390; wdses=15144b3f59d87d35; CNZZDATA1975683=cnzz_eid%3D711438673-1561090624-null%26ntime%3D1561090624; pt_37a49e8b=uid=GzZ7tZCtrMIxgLyYACddHw&nid=0&vid=H-Yo0-z3udgapFnnZCen8Q&vn=2&pvn=1&sact=1561095390110&to_flag=1&pl=t4NrgYqSK5M357L2nGEQCw*pt*1561095185647',
    #     'Host':'china.chinadaily.com.cn_s_37a4',
    #     'Pragma':'no-cache',
    #     'Referer':'http://cn.chinadaily.com.cn/',
    #     'Upgrade-Insecure-Requests':'1',
    #     'User-Agent': random_agent,
    # }
    rules = (
        Rule(LinkExtractor(allow=r'/a/.*'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'chinadaily.com.cn/'), follow=True),
    )

    def parse_item(self, response):
        item_loader = chinadailyItemLoader(item=chinadailyItem(), response=response)
        print(response.url)
        item_loader.add_xpath("publishtime", "//*[@class='fenx']/div[2]/text()")
        item_loader.add_xpath("title", "//*[@class='dabiaoti']/text()")
        item_loader.add_xpath("source", "//*[@class='fenx']/div[1]/text()")
        item_loader.add_css("content", "div.datu-a p::text")
         # item_loader.add_css("title", ".car-title h1::text")
        # item_loader.add_css("title", ".car-title h1::text")
        item_loader.add_value("url", response.url)
        bbs_item = item_loader.load_item()
        yield bbs_item
