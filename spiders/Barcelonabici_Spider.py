__author__ = 'jpradas'

# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from items import AlquilerBiciItem

class BarcelonabiciSpider(scrapy.Spider):
    name = "BicingBarcelona"
    allowed_domains = ["http://www.bicing.cat/"]
    start_urls = [
        "https://www.bicing.cat/es/informacion/tarifas"
    ]
    def parse(self, response):
        #for sel in response.xpath('//div/[@class="desc_article"]/ul'):
        item = AlquilerBiciItem()
        #for sel in
        anual=response.xpath("//div[@class='tarifas_box anual']")
        for a in anual:
            item['Desc1']=a.xpath('.//div[@class="tarifas_box_top"]/p/text()').extract()
            item['Desc1']=[c.strip() for c in item['Desc1']]
            item['Precio1']=a.xpath(".//div[@class='tarifas_box_bottom']/text()").extract()
            item['Precio1']=[c.strip() for c in item['Precio1']]

        anual=response.xpath("//div[@class='tarifas_box resto']")
        for a in anual:
            item['Desc2']=a.xpath('.//div[@class="tarifas_box_top"]/p/text()').extract()
            item['Desc2']=[c.strip() for c in item['Desc2']]
            item['Precio2']=a.xpath(".//div[@class='tarifas_box_bottom']/text()").extract()
            item['Precio2']=[c.strip() for c in item['Precio2']]
        anual=response.xpath("//div[@class='tarifas_box penalizacion']")
        for a in anual:
            item['Desc3']=a.xpath('.//div[@class="tarifas_box_top"]/p/text()').extract()
            item['Desc3']=[c.strip() for c in item['Desc3']]
            item['Precio3']=a.xpath(".//div[@class='tarifas_box_bottom']/text()").extract()
            item['Precio3']=[c.strip() for c in item['Precio3']]

        item['nombre'] = self.name
        item['url'] = self.start_urls[0]

        item['Online']='S'
        item['X']='41.39'
        item['Y']='2.17'
        yield item





