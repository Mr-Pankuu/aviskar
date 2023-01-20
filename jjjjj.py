import pymongo
from pymongo import MongoClient
CLIENT = MongoClient("mongodb://localhost:27017")
xx = list(CLIENT["aviskar"]["users_data"].find({}))

print(*xx,sep="\n")
