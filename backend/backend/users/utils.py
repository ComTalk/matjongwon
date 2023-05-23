from utils import get_db_handle
from secrets import DATABASES

mongodb = DATABASES['mongodb']['CLIENT']

def get_user_by_email(email):
    db, client = get_db_handle(
        'sampledb', 
        mongodb['host'], 
        mongodb['port'], 
        mongodb['username'], 
        mongodb['password']
    )
    users_collection = db['user']
    user = users_collection.find_one({'email': email})
    return user
