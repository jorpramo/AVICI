__author__ = 'Jorge'

ITEM_PIPELINES = {'avici.pipelines.MongoPipeline':100,}

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGO_DATABASE = 'avici'
MONGODB_COLLECTION = 'servicios'
MONGODB_UNIQ_KEY = 'url'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True
#MONGO_URI = 'mongodb://localhost:27017/'
MONGO_URI = 'mongodb://avicibatch:avici2015@dbh63.mongolab.com:27637/avici'