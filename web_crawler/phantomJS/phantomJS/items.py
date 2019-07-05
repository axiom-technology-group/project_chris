# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import codecs
import json
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import pymysql
import pymysql.cursors


class PhantomjsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class KsbbsItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()


class KsbbsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    editor=scrapy.Field()
    content1=scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into ksbbs(title,url,source,editor,publishtime)
            VALUES (%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['source'],self['editor'],self['publishtime'])
        return insert_sql, params