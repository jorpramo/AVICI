# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from scrapy.spiders import XMLFeedSpider
from items import DatosBiciItem
import datetime

class ZaragozabiciSpiderDatos(XMLFeedSpider):
    name = "BiziZaragoza"
    allowed_domains = ["http://www.bizizaragoza.com/"]
    start_urls = [
        "http://www.zaragoza.es/buscador/select?q=category:Bizi&rows=10000&wt=xml"
    ]
    itertag = 'doc'

    def parse_node(self, response, node):
        item = DatosBiciItem()
        item['nombre'] = self.name
        coordenada=node.xpath('str[@name="coordenadas_p"]/text()').extract()[0]
        print(coordenada)
        coma=coordenada.index(",")
        item['X'] = coordenada[:coma]
        item['Y'] = coordenada[coma+1:]
        item['estacion'] = node.xpath('arr[@name="text"]/str/text()').extract()[0]
        print(item['estacion'] )
        item['n_estacion'] = node.xpath('str[@name="id"]/text()').extract()
        item['direccion'] = node.xpath('arr[@name="text"]/str/text()').extract()[0]
        x =  node.xpath('int[@name="bicisdisponibles_i"]/text()').extract()[0]
        disp=float(x[0])
        item['disponibles'] = disp
        x =  node.xpath('int[@name="anclajesdisponibles_i"]/text()').extract()[0]
        libres=float(x[0])
        item['libres'] = libres
        item['total'] =  disp+libres
        item['fecha'] = node.xpath('date[@name="last_modified"]/text()').extract()[0]
        return item


