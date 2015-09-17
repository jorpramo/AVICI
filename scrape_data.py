__author__ = 'jpradas'
import scrapy

from spiders.Valenbisidatos_Spider import ValenbisiSpiderDatos
from spiders.Malagabicidatos_Spider import MalagabiciSpiderDatos
from spiders.Barcelonabicidatos_Spider import BarcelonabiciSpiderDatos

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess



process = CrawlerProcess(get_project_settings())
process.crawl(BarcelonabiciSpiderDatos)
process.crawl(ValenbisiSpiderDatos)
process.crawl(MalagabiciSpiderDatos)
process.start()


