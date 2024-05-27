import pymongo
from Sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class  MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://gkumardav:Gaurav1993@cluster.3kmskua.mongodb.net/?retryWrites=true&w=majority&appName=CLUSTER"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
        except Exception as e:
            raise e        

