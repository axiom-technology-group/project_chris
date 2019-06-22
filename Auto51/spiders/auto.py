# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from Auto51.items import Auto51ItemLoader, Auto51Item
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from Auto51.settings import user_agent_list
import re
from scrapy.http import Request
from urllib import parse

class A51autoSpider(CrawlSpider):
    name = '51auto'
    allowed_domains = ['51auto.com']
    start_urls = ['http://51auto.com/']
    import random
    random_agent = random.choice(user_agent_list)
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Host': 'search.51auto.com',
    'Cookie':'PClocationHanzi=%E5%B9%BF%E4%B8%9C_%E5%B9%BF%E5%B7%9E; ',
    'Upgrade-Insecure-Requests':'1',
    'Referer': 'https://www.51auto.com',
    'User-Agent':random_agent,
    }
    rules = (
        # Rule(xiangxi_link, callback='parse_item',),
        Rule(LinkExtractor(allow=('http://item.51auto.com/buycar/',)), callback='parse_item',follow='true'),
        Rule(LinkExtractor(allow=('search.51auto.com/',), )),

    )

    def parse_item(self, response):
        item_loader = Auto51ItemLoader(item=Auto51Item(), response=response)
        print(response.url)
        item_loader.add_css("location", ".left-info p a::text")
        item_loader.add_css("dealer_details", ".h1_box i::attr(title)")
        item_loader.add_css("price", ".price::text")
        item_loader.add_css("title", ".car-title h1::text")
        item_loader.add_css("standard", ".br0 span::text")
        item_loader.add_xpath("mileage", "//*[@class='section-km clearfix']/ul/li/span/text()")
        item_loader.add_xpath("licensetime", "//*[@class='section-km clearfix']/ul/li[2]/span/text()")
        item_loader.add_css("content", ".car-detail-container p::text")
        # item_loader.add_css("title", ".car-title h1::text")
        # item_loader.add_css("title", ".car-title h1::text")
        item_loader.add_value("url", response.url)
        car_item = item_loader.load_item()
        yield car_item
