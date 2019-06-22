# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import codecs
import json
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import pymysql
import pymysql.cursors

class Auto51ItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class ijiaotongItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class KsbbsItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class chinadailyItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class LookArtvItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()


class ijiaotongItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    content=scrapy.Field()


    def get_insert_sql(self):
        insert_sql = """
             insert into ijiaotong(title,url,publishtime,source,content)
            VALUES (%s, %s,%s, %s,%s) 
        """
        params = (self['title'], self['url'],self['publishtime'],self['source'],self['content'])
        return insert_sql, params


class Auto51Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url=scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    dealer_details = scrapy.Field()
    standard = scrapy.Field()
    mileage = scrapy.Field()
    licensetime= scrapy.Field()
    content= scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into car(title,url,price,location,dealer_details,standard,mileage,licensetime,content)
            VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['price'],self['location'],self['dealer_details'],self['standard'],self['mileage'],self['licensetime'],self['content'])
        return insert_sql, params



class KsbbsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    editor=scrapy.Field()
    content=scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into ksbbs(title,url,source,editor,publishtime)
            VALUES (%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['source'],self['editor'],self['publishtime'])
        return insert_sql, params


class LookArtvItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    editor=scrapy.Field()
    content=scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into ksbbs(title,url,source,editor,publishtime)
            VALUES (%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['source'],self['editor'],self['publishtime'])
        return insert_sql, params

class chinadailyItem(scrapy.Item):

    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    content=scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into chinadaily(title,url,source,publishtime,content)
             VALUES (%s, %s, %s, %s, %s) 
        """
        params = (self['title'], self['url'],self['source'],self['publishtime'],self['content'])
        return insert_sql, params

