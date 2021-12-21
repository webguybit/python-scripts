import pymongo
import bson
from datetime import datetime, timedelta, date
from pytz import timezone
import pytz
mdb_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name = 'juice'

def setter_juice(setter_dict={}):
    database = mdb_client[database_name]
    cursor_object = database['comments']
    if bool(setter_dict):
        return_obj = cursor_object.insert_one(setter_dict)
        return return_obj.inserted_id
    else:
        return 0

def getter_juice(finder_dict = {}, projection_dict = {}):
    database = mdb_client[database_name]
    cursor_object = database['comments']
    projection_dict['_id'] = False
    cursor_result = cursor_object.find(finder_dict, projection = projection_dict)
    return list(cursor_result)

def del_comments_all():
    database = mdb_client[database_name]
    cursor_object = database['comments']
    cursor_object.drop()