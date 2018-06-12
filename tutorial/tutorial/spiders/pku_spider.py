#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:26:51 2018

@author: qimindeng
"""

from scrapy.contrib.spiders import CrawlSpider
#from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from tutorial.items import TutorialItem

class pkuspider(CrawlSpider):
    name="pkuintern"
    start_urls =[
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=python',
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=算法',
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=量化',
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=人工智能',
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=学习',
            'https://bbs.pku.edu.cn/v2/search.php?days=500&bid=896&key=AI',
            ]

    def parse(self, response):
        print('.................')
        next_page= response.xpath('//div[contains(text(),"下一页")]/a/@href').extract()[0]
        intern_page=response.xpath('//a[@class="block-link"]/@href').extract()
  #      aburl="https://bbs.pku.edu.cn/v2/"
        for link in next_page:
            yield Request(url="https://bbs.pku.edu.cn/v2/search.php"+link,callback=self.parse)
        for link in intern_page:
            yield Request(url="https://bbs.pku.edu.cn/v2/"+link,callback=self.myparse,dont_filter=False)
    def myparse(self,response):
        items=[]
        item=TutorialItem()
        item['title']=response.xpath('//div[@id="post-read"]/header/h3/text()').extract()[0]
        item['date']=response.xpath('//div[@class="sl-triangle-container"]/span[1]/span/text()').extract()[0]
        item['url']="https://bbs.pku.edu.cn/v2/"+response.xpath('//div[@class="breadcrumb-trail"]/a[5]/@href').extract()[0]
        item['author']=response.xpath('//div[@class="post-owner"]/p[1]/a/text()').extract()[0]
        item['content']=response.xpath('//div[@class="content"]/div/p/text()').extract()
        items.append(item)
        return items
     