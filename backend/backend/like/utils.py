from utils import get_db_handle
from secret import DATABASES
from bson.objectid import ObjectId

mongodb = DATABASES['mongodb']['CLIENT']

def access_db():
    db, client = get_db_handle(
        'sampledb', 
        mongodb['host'], 
        mongodb['port'], 
        mongodb['username'], 
        mongodb['password']
    )
    return db['user'], client

def get(user_id):
    collection, client = access_db()

    try:
        user = collection.find_one({'_id': ObjectId(user_id)})
        return user
    finally:
        client.close()

def update_liked(user_id, place_id, rating):
    collection, client = access_db()
    result = collection.update_one(
        {'_id': ObjectId(user_id), 'liked.restaurant_id': str(place_id)},
        {'$set': {'liked.$.rating': rating}}
    )

    client.close()

def remove_liked(user_id, place_id):
    collection, client = access_db()
    result = collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$pull': { 
            'liked': { 
                'restaurant_id': str(place_id)
                }
            }
        }
    ) 

    client.close()

def create_liked(user_id, place):
    collection, client = access_db()
    result = collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$push': { 
            'liked': place
            }
        }
    )
    if result.matched_count > 0:
        print("Created another liked")
    else:
        print("Creating another liked Failed")

    client.close()
