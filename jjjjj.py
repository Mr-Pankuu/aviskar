import pymongo
from pymongo import MongoClient
CLIENT = MongoClient("mongodb://localhost:27017")
# xx = list(CLIENT["aviskar"]["users_data"].find({}))
xx = CLIENT["aviskar"]["users_data"].delete_one({"username":"yuvraj"})
# print(*xx,sep="\n")
# # print(*xx,sep="\n")

# x=20
# exec('x=12')
# print(x)


# class xxx:
#     global x
#     x = 69

# class a:

#     def change_69(self, j):
#         global x
#         x = j
#     def sum_69(self,j):
#         global x
#         return x + j

# print(x)

# jjj = xxx()
# item = a()

# item.change_69(96)
# print(x)
# print(item.sum_69(100))
# item.change_69(69)
# print(x)
# print(item.sum_69(100))