import pymongo
from pymongo import MongoClient
from faker import Faker

CLIENT = MongoClient("mongodb://localhost:27017")
user_data = CLIENT["aviskar"]["users_data"]

faker_data = Faker()
print(dir(faker_data))

print(faker_data.date())
