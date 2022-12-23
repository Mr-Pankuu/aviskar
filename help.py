import numpy as np
import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint, choice
import datetime
import time

raw_matirals = [
    ("Salt", "kg"),
    ("Papad (Sagun)", "kg"),
    ("Sugar", "kg"),
    ("Poha", "kg"),
    ("Maida", "kg"),
    ("Atta", "kg"),
    ("Sooji", "kg"),
    ("Shabi Biryani Masala", "kg"),
    ("Kitchen King", "kg"),
    ("Paw Bhaji Masala", "kg"),
    ("Sambhar Masala", "kg"),
    ("Chiken Masala", "kg"),
    ("Chana Masala Chole Masala)", "kg"),
    ("Chat Masala (100gm) 1Pkt", "kg"),
    ("Kasoori Methi(250gm) 1pkt", "kg"),
    ("Jeera", "kg"),
    ("Hing", "bo"),
    ("Rose Water", "bo"),
    ("Orange Red Powder", "bo"),
    ("Apple Green Powder", "bo"),
    ("Gole Marij Kali Mirch)", "kg"),
    ("Orange Red Powder Apple Green Powder", "kg"),
    ("Gole Marij(Kali Mirch)", "kg"),
    ("Kala Jeera", "kg"),
    ("Bada", "kg"),
    ("Ajwain", "kg"),
    ("Mirchi Powder", "kg"),
    ("Haldi Powder", "kg"),
    ("Sendha Namak (500gm) 1pkt", "kg"),
    ("Dhaniya Powder", "kg"),
    ("Bourn Vita", "kg"),
    ("Horlicks", "kg"),
    ("Javitri", "kg"),
    ("Dal Chini", "kg"),
    ("Sewai", "kg"),
    ("Arhar Dal (Toor Dal)", "kg"),
    ("Kabuli Chana", "kg"),
    ("Besan", "kg"),
    ("Rajma", "kg"),
    ("Chay Patti (Tea Leaves)", "kg"),
    ("Chay Patti (Tea Leaves)", "kg"),
    ("Phalli Dana (Peanut)", "kg"),
    ("Moong Dal", "kg"),
    ("Urad Dal", "kg"),
    ("Chana Dal", "kg"),
    ("Green Moong (Khada Moong)", "kg"),
    ("White Matar", "kg"),
    ("Dhaniya Khada", "kg"),
    ("Black Chana", "kg"),
    ("Sabudana", "kg"),
    ("Rice", "kg"),
    ("Idly Rice", "kg"),
    ("Soyabin Bari", "kg"),
    ("Tomato Souce", "bo"),
    ("Pickle", "bo"),
    ("Green Chilli (Souce)", "bo"),
    ("Red Chilli (Souce)", "bo"),
    ("Oll Dalda", "kg"),
    ("Soya Souce", "kg"),
    ("Vinegar", "kg"),
    ("Tomato Souce (Pouch)", "kg"),
    ("Water Tulsi", "kg"),
    ("oil", "kg"),
    ("Maza", "kg"),
    ("Sprite", "kg"),
    ("Thums Up", "kg"),
    ("Maza", "kg"),
    ("Maza", "kg"),
    ("Sprite", "kg"),
    ("Thums Up", "kg"),
    ("Magaj", "kg"),
    ("Methi", "kg"),
    ("Masoor Dal", "kg"),
    ("Mastered Seed Ajina Moto Salt", "kg"),
    ("(Raai)", "kg"),
    ("Kewada Water", "kg"),
    ("Corn Flower (Makka Atta Ararot)", "kg"),
    ("Frymes (Tikona Papad)", "kg"),
    ("Tamrind (imali)", "kg"),
    ("Sattu Atta", "kg"),
    ("Rosted Chana", "kg"),
    ("Ghadi Powder", "kg"),
    ("V-Hari Mirch-K", "kg"),
    ("V-Karela", "kg"),
    ("V-Kheera", "kg"),
    ("V-Khekhasi", "kg"),
    ("V-Lauki", "kg"),
    ("V-Parval", "kg"),
    ("V-Mooli", "kg"),
    ("V-Methi bhaji", "kg"),
    ("V-Green Matar", "kg"),
    ("V-Palak Bhaji", "kg"),
    ("V-Kadhi Leaves V-Spring Onion", "kg"),
    ("V-Kela", "kg"),
    ("V-Nibu (PIC/NOS)", "kg"),
    ("V-Kundru", "kg"),
    ("-Kaddu", "kg"),
    ("V-Hari Mirchi Big-K", "kg"),
    ("V-Shimla", "kg"),
    ("V-Tamatar", "kg"),
    ("V-Lal Bhaji", "kg"),
    ("V-Semi", "kg"),
    ("V-Hari Mirchi Big-K", "kg"),
    ("V-Shimla", "kg"),
    ("V-Tamatar", "kg"),
    ("V-Lal Bhaji", "kg"),
    ("V-Semi V-Pyaj", "kg"),
    ("V-Aloo", "kg"),
    ("Lahspon", "kg"),
    ("Green Elaichi", "kg"),
    ("Sauf", "kg"),
    ("Kaju Tukada", "kg"),
    ("Long", "kg"),
    ("Kismis", "kg"),
    ("Soda", "kg"),
    ("Tartari", "kg"),
    ("Mastered Oil", "kg"),
    ("Coffee (90gm) 1pkt ", "kg"),
    ("Pairie-G (Rs-5/-)", "kg"),
    ("Good Day (Rs-10/-)", "kg"),
    ("Chicken", "kg"),
    ("Amul Butter", "kg"),
    ("Amul Cheese", "kg"),
    ("Chocolate Syrup", "kg"),
    ("Pizza Souce", "kg"),
    ("Veg Mayonmise", "kg"),
    ("Sweet Corn", "kg"),
    ("GREEN MATAR", "kg"),
    ("Burger Tikki", "kg"),
    ("French Fries", "kg"),
    ("Yellow Color", "bo"),
    ("Maggi (280g pkt)", "kg"),
    ("Gulab Jal (250ml) 1Bott", "bo"),
]


CLIENT = MongoClient("mongodb://localhost:27017")
user_data = CLIENT["aviskar"]["users_data"]

# faker_data = Faker(locale="en_IN")

# genrate_data_of = input("Enter what kind of data to genrate:- ")

# if genrate_data_of == "user":
#     for i in range(int(input("Enter the number of user to input:- "))):
#         while True:
#             phone = faker_data.phone_number()
#             if phone[0] == "+":
#                 break
#             else:
#                 continue
#         today = str(datetime.date.today())
#         age = randint(15, 65)
#         dob = str(int(today[:4]) - age) + today[4:]

#         collage = "RCST"
#         course = "BCA"
#         collage_year = randint(1, 4)

#         you_are_data_list = ["student", "non-student"]
#         you_are = choice(you_are_data_list)
#         if you_are != "student":
#             collage = None
#             course = None
#             collage_year = None

#         user = {
#             "username": faker_data.name(),
#             "email": faker_data.email(),
#             "password": faker_data.password(),
#             "date_of_birth": dob,
#             "you_are": {
#                 you_are: {
#                     "collage": collage,
#                     "course": course,
#                     "collage_year": collage_year,
#                 }
#             },
#             "gender": choice(["Male", "Female"]),
#             "age": age,
#             "favorite_color": faker_data.color_name(),
#             "address": faker_data.address().replace("\n", " "),
#             "phone": phone,
#             "privilege": "user",
#         }
#         user_data.insert_one(user)

# elif genrate_data_of == "menu":
#     food_list = {
#         "plain dosa": 20,
#         "masala dosa": 25,
#         "cutpiece dosa": 30,
#         "uttapam": 25,
#         "sambhar vada (2cps)": 20,
#         "idly (2pcs)": 15,
#         "poha": 15,
#         "chana poha": 20,
#         "samosa (2pcs)": 20,
#         "samosa mutter": 25,
#         "dahi samosa": 30,
#         "aalu gunda (2pcs)": 15,
#         "aalu gunda mutter": 20,
#         "tea": 10,
#         "coffee": 15,
#         "sabudana khichdi": 20,
#         "sabudana vada (3pcs)": 20,
#         "hot milk per glass": 15,
#         "aalo paratha": 30,
#         "paneer paratha": 30,
#         "chhole bhature": 30,
#         "veg sandwitch": 20,
#         "bread pakoda (1pcs)": 10,
#         "bhajiya piyagi": 15,
#         "pyaji vada": 10,
#         "momos (6pcs)": 20,
#     }
#     user = [
#         {
#             "name": i,
#             "price": j,
#             "quantity": {"half": round(j / 2), "full": j},
#             "discount": None,
#         }
#         for i, j in food_list.items()
#     ]

#     user_data = CLIENT["aviskar"]["menu_item"].insert_many(user)

# elif genrate_data_of == "sales":
#     data = list(user_data.find({}, limit=int(input("Number of user:- "))))
#     menu_data = list(CLIENT["aviskar"]["menu_item"].find({}))

#     for i in data:
#         item = {}
#         for _ in range(randint(1, 10)):
#             x = choice(menu_data)
#             item.update({x["name"]: {"price": x["price"], "quantity": randint(1, 10)}})

#         bought = {
#             "items": item,
#             "total": sum([i["price"] * i["quantity"] for i in item.values()]),
#         }
#         date_time = str(faker_data.date_time_this_year()).split(" ")
#         item_data = {
#             "username": i["username"],
#             "email": i["email"],
#             "phone": i["phone"],
#             "bought": bought,
#             "date": date_time[0],
#             "time": date_time[1],
#         }
#         user_data = CLIENT["aviskar"]["sales"].insert_one(item_data)


# today = datetime.date.today()
# print(str(today))
# print(*user_data.find({}, limit=1), sep="\n")

# users_data = CLIENT["aviskar"]["users_data"].find({}, limit=100)
# names = users_data[0]

# print(list(dict(names["you_are"]).keys()))
# print(len(raw_matirals))
print(time.time())

def generate_raw_matarial(x: int):
    raw_m = list(set([choice(raw_matirals) for _ in range(x)]))

    return {i[0]: {"quintity": randint(5, 100), "unit": i[1]} for i in raw_m}


generate_raw_matarial(randint(5, 30))


def genrate_date(from_, to):
    return [str(i) for i in np.arange(from_, to, dtype="datetime64[D]")]


date_data = genrate_date("2022-01", "2022-12-23")

i_data = [
    {
        i: {
            "in": generate_raw_matarial(randint(5, 30)),
            "out": generate_raw_matarial(randint(5, 30)),
        }
    }
    for i in date_data
]

raw_mar_data = CLIENT["aviskar"]["in_out"]
raw_mar_data.insert_many(i_data)

print(raw_mar_data.find({}))