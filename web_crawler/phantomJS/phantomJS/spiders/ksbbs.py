# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy import Spider,Request
from selenium import webdriver
from phantomJS.settings import user_agent_list
from phantomJS.items import KsbbsItemLoader,KsbbsItem
from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse

class KsbbsSpider(CrawlSpider):
    name = 'ksbbs'
    allowed_domains = ['auto.ksbbs.com']
    start_urls = ['http://auto.ksbbs.com/news']
    import random
    random_agent = random.choice(user_agent_list)

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='D:\coding\LinuxShare\chromedriver')
        super(KsbbsSpider, self).__init__()

    def closed(self, reason):
        self.browser.close()  # 记得关闭
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'newsvisit=2019-06-20%2011%3A01%3A22; newsvisit=2019-06-19%2017%3A23%3A18; UM_distinctid=16b6f16c5a40-06e3b9926bf2f3-4d045769-1fa400-16b6f16c5a5517; ASP.NET_SessionId=dmdfh5j4k3nd11pqj0ujjhwa; newsvisit=2019-06-20%2010%3A58%3A41',
        'Host':'auto.ksbbs.com',
        'Referer':'http://auto.ksbbs.com/',
        'Upgrade-Insecure-Requests':'1',
        # 'User-Agent':random_agent,
    }
    rules = (
        Rule(LinkExtractor(allow=r'news/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('http://auto.ksbbs.com/news/',), )),
        Rule(LinkExtractor(allow=r'column/\d+'), follow=True),

    )


    def parse_item(self, response):
        item_loader = KsbbsItemLoader(item=KsbbsItem(), response=response)
        print(response.url)
        item_loader.add_xpath("publishtime", "//*[@class='info']/span[3]/text()")
        item_loader.add_xpath("title", "//*[@class='title']/text()")
        item_loader.add_xpath("source", "//*[@class='info']/span[1]/text()")
        item_loader.add_xpath("editor", "//*[@class='info']/span[2]/text()")
        item_loader.add_xpath("content1", '//div[@class="content"]/p/span/text()')
        # item_loader.add_css("title", ".car-title h1::text")
        # item_loader.add_css("title", ".car-title h1::text")
        item_loader.add_value("url", response.url)
        bbs_item = item_loader.load_item()
        yield bbs_item