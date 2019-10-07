import scrapy
import re
from scrapy.selector import Selector
from appstore.items import AppstoreItem

class HuaweiSpider(scrapy.Spider):
    name = "huawei"
    allowed_domains = ["huawei.com"]

    start_urls = [
        "http://appstore.huawei.com/more/all"
    ]

    def parse(self,response):
        page = Selector(response)
        
        hrefs = page.xpath('//h4[@class="title"]/a/@href')
        
        for href in hrefs:
            url ="http://appstore.huawei.com" +  href.extract()
            # yield scrapy.Request(url,callback=self.parse_item)
            print ("*****url:%s"%url)

            yield scrapy.Request(url,self.parse_item,meta={
                'splash':{
                    'endpoint':'render.html',
                    'args':{'wait':10.5}
                    }
                })
            
    
    def parse_item(self,response):
        page = Selector(response)
        item = AppstoreItem()
        # print "page:%s"%page.get()        
        item['title'] = page.xpath('//ul[@class="app-info-ul nofloat"]/li/p/span[@class="title"]/text()').\
                    extract_first().encode('utf-8')
        item['url'] = response.url
        # print item['url']
        item['appid'] = page.xpath('//input[@id="appId"]/@value').extract_first().encode('utf-8')
#       item['appid'] = re.search('C\d*',item['url']).group()
        item['intro'] = page.xpath('//meta[@name="description"]/@content').extract_first().encode('utf-8')
        
        divs = page.xpath('//div[@class="open-info"]')
        recomm = ""
        #len(divs)==20, 10 for recommended and 10 for same type top10
        for div in divs[:10]:
            url = div.xpath('./p[@class="name"]/a/@href').extract_first()
            recom_appid = re.search('C\d*',url).group()
            name = div.xpath('./p[@class="name"]/a/@title').extract_first().encode('utf-8')
            recomm +="{0}:{1},".format(recom_appid,name)
        item['recommended'] = recomm
        yield item
        
