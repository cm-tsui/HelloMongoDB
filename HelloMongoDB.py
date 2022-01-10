# pip install pymongo
# pymongo import MongoClient
from pymongo import MongoClient

# connect MongoDB
client = MongoClient('mongodb://localhost:27017')

# query documents
for i in client.newdb.lightmap.find({}):
    print(i)
