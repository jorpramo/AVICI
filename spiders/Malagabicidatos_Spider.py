# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from scrapy.spiders import CSVFeedSpider
from items import DatosBiciItem
import datetime

class MalagabiciSpiderDatos(CSVFeedSpider):
    name = "Malagabici"
    allowed_domains = ["http://malagabici.malaga.eu/"]
    start_urls = [
        "http://datosabiertos.malaga.eu/recursos/transporte/EMT/estacionamientos/Estacionamientos.csv"
    ]
    delimiter = ','
    quotechar = "\""
    headers = ['ID','NOMBRE','NOMBRE_CIUDAD','DIRECCION','ID_ESTADO','NOMBRE_ESTADO','NUM_DERBIS','NUM_LIBRES','NUM_OCUPADOS','LAT','LON','ID_EXTERNO']

    def parse_row(self, response, row):
        if row['ID']!='ID':
            item = DatosBiciItem()
            item['nombre'] = self.name
            item['X'] = row['LAT']
            item['Y'] = row['LON']
            item['estacion'] = row['NOMBRE']
            item['n_estacion'] = row['ID']
            item['direccion'] = row['DIRECCION']
            item['disponibles'] = float(row['NUM_OCUPADOS'])
            item['libres'] = float(row['NUM_LIBRES'])
            item['total'] = float(row['NUM_DERBIS'])
            item['fecha'] = datetime.datetime.now()
            return item


