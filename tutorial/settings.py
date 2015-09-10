__author__ = 'Jorge'

ITEM_PIPELINES = [
  'scrapymongodb.MongoDBPipeline',
]

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items'
MONGODB_UNIQ_KEY = 'url'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True