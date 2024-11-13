from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"

client = MongoClient(MONGO_URL)
admin_db = client.admin
db_list = admin_db.command("listDatabases")
pprint(db_list)
