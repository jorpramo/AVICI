__author__ = 'jpradas'

# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from items import AlquilerBiciItem

class MalagabiciSpider(scrapy.Spider):
    name = "Malagabici"
    allowed_domains = ["http://malagabici.malaga.eu/"]
    start_urls = [
        "http://malagabici.malaga.eu/webpublica/tarifas-2014.html"
    ]
    def parse(self, response):
        #for sel in response.xpath('//div/[@class="desc_article"]/ul'):
        item = AlquilerBiciItem()
        for sel in response.xpath('//table[@class="table responsive"]'):

            item['nombre'] = self.name
            item['url'] = self.start_urls[0]
            todo = sel.xpath('//li')
            textos = sel.xpath('.//thead/tr/th/text()').extract()
            datos = sel.xpath('.//tbody/tr/td/text()').extract()
            if textos[0]=="Alta":
                item['Precio1']=datos[0]
                item['Desc1']=textos[0]
            if textos[0]=="Suplementos":
                item['Precio2']=datos[0]
                item['Desc2']=textos[0]
                '''item['Precio3']=datos[3]
                item['Desc3']=textos[3]'''
            item['Online']='S'
            item['X']='36.7'
            item['Y']='-4.42'
        yield item





