__author__ = 'jpradas'
import settings
from spiders.Valenbisi_Spider import ValenbisiSpider
from spiders.Malagabici_Spider  import MalagabiciSpider
from spiders.Barcelonabici_Spider import BarcelonabiciSpider
from spiders.Zaragozabici_Spider import ZaragozabiciSpider

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(get_project_settings())

process.crawl(ValenbisiSpider)
process.crawl(MalagabiciSpider)
process.crawl(BarcelonabiciSpider)
process.crawl(ZaragozabiciSpider)

process.start()

