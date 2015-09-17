# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from scrapy.spiders import CSVFeedSpider
from items import DatosBiciItem

class ValenbisiSpiderDatos(CSVFeedSpider):
    name = "Valenbisi"
    allowed_domains = ["Valenbisi.es"]
    start_urls = [
        "http://mapas.valencia.es/lanzadera/opendata/Valenbisi/CSV"
    ]
    delimiter = ';'
    quotechar = "'"
    #headers = ['X','Y','name','number','address','open','available','free','total','ticket','updated_at']

    def parse_row(self, response, row):
        item = DatosBiciItem()
        item['nombre'] = self.name
        item['X'] = row['Y']
        item['Y'] = row['X']
        item['estacion'] = row['name']
        item['n_estacion'] = row['number']
        item['direccion'] = row['address']
        item['disponibles'] = float(row['available'])
        item['libres'] = float(row['free'])
        item['total'] = float(row['total'])
        item['fecha'] = row['updated_at']
        return item


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