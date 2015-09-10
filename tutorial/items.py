# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AlquilerBiciItem(scrapy.Item):
    nombre = scrapy.Field()
    url = scrapy.Field()
    Precio1 = scrapy.Field()
    Desc1 = scrapy.Field()
    Precio2 = scrapy.Field()
    Desc2 = scrapy.Field()
    Precio2 = scrapy.Field()
    Desc2 = scrapy.Field()
    Seguro = scrapy.Field()
    Online  = scrapy.Field()
    Usuarios =  scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
