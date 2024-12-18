import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('localhost',27017)

db = client.appdb

user = db.users

#huhu_id = user.insert_one({'name':'huhu haha','age':69,'address':{'houseName':'tatya niwas'}}).inserted_id
#user.insert_one({'name':'huhu haha','age':69,'address':{'houseName':'tatya niwas','rasta':'babogruha'}})
#user.insert_one({'name':'king pin'})

for use in user.find():
    print(use)


print([p for p in user.find({'name':'huhu haha'})])
print()
print([p for p in user.find({'age':{'$gt':25}})])
print()
print(user.count_documents({'name':'huhu haha'}))
print()
print(x for x in user.find({'age':{'$exists':False}}))

user.update_one({'_id':ObjectId('6753ac178b7a9689bf893bf9')}, {'$set':{'age':21}})

user.delete_many({'address':{'houseName':'tatya niwas'}})
