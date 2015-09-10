# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from tutorial.items import AlquilerBiciItem

class ValenbisiSpider(scrapy.Spider):
    name = "Valenbisi"
    allowed_domains = ["Valenbisi.es"]
    start_urls = [
        "http://www.valenbisi.es/Abonate/Abono-de-larga-duracion/Una-inscripcion-economica-y-practica"
    ]

    def parse(self, response):
        #for sel in response.xpath('//div/[@class="desc_article"]/ul'):
        for sel in response.xpath('//div[@class="desc_article"]/ul/li'):
            item = AlquilerBiciItem()
            item['nombre'] = self.name
            item['url'] = self.start_urls[0]

            textos = sel.xpath('//li/b/text()').extract()
            datos = sel.xpath('//li/b/[contains(text(), "Importe del abono anual")]/text()')


            print(sel.xpath('//li/b/text()').extract())
            yield item




'''
<div class="desc_article">
<ul>

<li><b>Importe del abono anual Valenbisi</b> : 29,21 Euros.</li>

<li><b>Primeros treinta minutos de utilización </b>: Gratuitos.</li>

<li><b>De 30 a 60 minutos </b>: 0,52 céntimos de Euro por los 30 minutos adicionales.</li>

<li><b>Cada 60 minutos adicionales</b> : 2,08 Euros por cada 60 minutos adicionales.</li>

</ul>
</div>
'''