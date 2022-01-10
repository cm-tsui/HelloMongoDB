# Windows install MongoDB
# Open MongoDB Compass and connect with empty connection
# Create database 'newdb'
# Create collection 'lightmap'
# Create document {'name': '长城', 'city': '北京', 'country': '中国', 'gps': {'lat': 106.384, 'lng': 39.031}}
# pip install pymongo

# pymongo import MongoClient
from pymongo import MongoClient

# connect MongoDB
client = MongoClient('mongodb://localhost:27017')

database_name = 'newdb'
newdb = client[database_name]

collection_name = 'lightmap'
collection = newdb[collection_name]

# query documents
print('Before insert:')
query={'city':'北京'}
result=collection.find(query).limit(2)
for i in result:
    print(i)

# insert document
document={'name': '故宫', 'city': '北京', 'country': '中国', 'gps': {'lat': 116.403, 'lng': 39.924}}
collection.insert_one(document)

# query documents
print('After insert 故宫:')
query={'city':'北京'}
result=collection.find(query).limit(2)
for i in result:
    print(i)

# update document
query={'name':'故宫'}
present_data=collection.find_one(query)
new_data={'$set':{'name':'国家体育场'}}
collection.update_one(present_data,new_data)

# query documents
print('After update 故宫 to 国家体育场:')
query={'city':'北京'}
result=collection.find(query).limit(2)
for i in result:
    print(i)

# delete document
query={'name':'国家体育场'}
collection.delete_one(query)

# query documents
print('After delete 国家体育场:')
query={'city':'北京'}
result=collection.find(query).limit(2)
for i in result:
    print(i)
