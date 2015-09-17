import pymongo

class MongoPipeline(object):

    collection_name = 'servicios'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item.__class__.__name__=='AlquilerBiciItem':
            self.collection_name='servicios'
            self.db[self.collection_name].replace_one({"nombre": item['nombre']},dict(item), True)
        if item.__class__.__name__=='DatosBiciItem':
            self.collection_name='datos'
            self.db[self.collection_name].insert(dict(item))
            self.collection_name='datos_actual'
            self.db[self.collection_name].replace_one({"nombre": item['nombre'], "estacion":item['estacion']},dict(item), True)

        return item