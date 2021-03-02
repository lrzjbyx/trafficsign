# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from trafficsign.items import TrafficsignItem
from scrapy.utils import response



class TsSpider(CrawlSpider):
    name = 'ts'
    allowed_domains = ['jiakaobaodian.com']
    start_urls = ['https://www.jiakaobaodian.com/sign/']

#                                /core-assets/static/images/sign//biaozhi/1/jl1.jpg
#   https://www.jiakaobaodian.com/core-assets/static/images/sign//biaozhi/1/jl1.jpg


    rules = (
        Rule(LinkExtractor(allow=r'https://www.jiakaobaodian.com/sign/flag.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        category = response.xpath("//div[@class='right']//h3/text()").get()
        names = response.xpath("//div[@class='com-sign-container com-part']/ul[@class='clearfix']/li/p/text()").getall()
        srcs = response.xpath("//div[@class='com-sign-container com-part']/ul[@class='clearfix']/li//img/@src").getall()
        srcs = list(map(lambda x: response.urljoin(x),srcs))
        yield TrafficsignItem(category=category,image_urls=srcs,names=names)
