# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from scrapy.spiders import XMLFeedSpider
from items import DatosBiciItem
import datetime

class BarcelonabiciSpiderDatos(XMLFeedSpider):
    name = "BicingBarcelona"
    allowed_domains = ["http://www.bicing.cat/"]
    start_urls = [
        "http://wservice.viabicing.cat/v1/getstations.php?v=1"
    ]
    itertag = 'station'

    def parse_node(self, response, node):
        item = DatosBiciItem()
        item['nombre'] = self.name
        item['X'] = node.xpath('lat/text()').extract()[0]
        item['Y'] = node.xpath('long/text()').extract()[0]
        item['estacion'] = node.xpath('street/text()').extract()[0]
        item['n_estacion'] = node.xpath('id/text()').extract()[0]
        item['direccion'] = node.xpath('street/text()').extract()[0]
        x =  node.xpath('bikes/text()').extract()
        disp=float(x[0])
        item['disponibles'] = disp
        x =  node.xpath('slots/text()').extract()
        libres=float(x[0])
        item['libres'] = libres
        item['total'] =  disp+libres
        item['fecha'] = datetime.datetime.now()
        return item


