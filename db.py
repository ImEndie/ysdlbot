from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = os.getenv('MONGO_URI')
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['ysdlbot']
users=db.get_collection('users')

def ins(id):
    r=users.find_one({"user_id":int(id)},max_time_ms=500)
    if not r:
        users.insert_one({"user_id":int(id)})

def get_count():
    return users.count_documents(filter={})