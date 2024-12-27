import mongomock


class Config:
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost',
        'mongo_client_class': mongomock.MongoClient
    }
