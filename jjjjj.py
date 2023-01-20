import pymongo
from pymongo import MongoClient
CLIENT = MongoClient("mongodb://localhost:27017")
xx = list(CLIENT["aviskar"]["users_data"].find({}))
# xx = CLIENT["aviskar"]["users_data"].delete_one({"username":""})
print(*xx,sep="\n")
# # print(*xx,sep="\n")

# x=20
# exec('x=12')
# print(x)

