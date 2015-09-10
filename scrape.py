__author__ = 'jpradas'
import scrapy
from tutorial.spiders.Valenbisi_Spider import ValenbisiSpider
from scrapy.crawler import CrawlerProcess



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(ValenbisiSpider)
process.start()

