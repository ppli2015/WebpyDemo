# -*-coding:utf-8-*-
__author__ = 'lpp'

import pymongo
from datetime import datetime


def checkAndPrint(item):
    tt = type(item)
    if tt == type([]):
        print '['
        for i in item:
            checkAndPrint(i)
        print ']'
    elif tt == type({}):
        print '{'
        for i in item:
            print i, ':'
            checkAndPrint(item[i])
        print '}'
    else:
        print item


client = pymongo.MongoClient('192.168.1.133', 27017)
db = client.test
print db.name
# coll = db.dataset
# print coll

# result = db.restaurants.insert_one(
#     {
#         "address": {
#             "street": "2 Avenue",
#             "zipcode": "10075",
#             "building": "1480",
#             "coord": [-73.9557413, 40.7720266]
#         },
#         "borough": "Manhattan",
#         "cuisine": "Italian",
#         "grades": [
#             {
#                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
#                 "grade": "A",
#                 "score": 11
#             },
#             {
#                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
#                 "grade": "B",
#                 "score": 17
#             }
#         ],
#         "name": "Vella",
#         "restaurant_id": "41704620"
#     }
# )
# print result
# print result.inserted_id

# cursor = db.restaurants.find()
# cursor = db.restaurants.find({"address.zipcode": "10075"})
cursor = db.restaurants.find({"grades.grade": "B"}).sort([("name", pymongo.ASCENDING)])
count = 0
for document in cursor:
    count += 1
    for item in document:
        print item, ':', document[item]
    # print item, ':'
    # checkAndPrint(document[item])
    print '=' * 20
print 'count : ', count
