# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    weixin_name = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into wxarticle(title,url,weixin_name,time,content)
            VALUES (%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['weixin_name'],self['time'],self['content'])
        return insert_sql, params


class AccountItem(scrapy.Item):
    name = scrapy.Field()
    account = scrapy.Field()
    recommend = scrapy.Field()
    Authentication = scrapy.Field()
    article_lately = scrapy.Field()
    time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
             insert into wxaccount(title,url,recommend , Authentication, article_lately,time)
            VALUES (%s,%s,%s,%s,%s,%s) 
        """
        params = (self['title'], self['url'],self['recommend'],self['Authentication'],self['article_lately'],self['time'])
        return insert_sql, params
