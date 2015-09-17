from scrapy.loader.processor import MapCompose, Identity
from scrapy.loader import XPathItemLoader
from scrapy import log

from avici.items import AlquilerBiciItem


class RootItemLoader(XPathItemLoader):
    default_item_class = AlquilerBiciItem
    default_input_processor = Identity()
    default_ouput_processor = Identity()