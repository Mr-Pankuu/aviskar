import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint, choice
import datetime

raw_matirals = [
    "Salt",
    "Papad (Sagun)",
    "Sugar",
    "Poha",
    "Maida",
    "Atta",
    "Sooji",
    "Shabi Biryani Masala",
    "Kitchen King",
    "Paw Bhaji Masala",
    "Sambhar Masala",
    "Chiken Masala",
    "Chana Masala Chole Masala)",
    "Chat Masala (100gm) 1Pkt",
    "Kasoori Methi(250gm) 1pkt",
    "Jeera",
    "Hing",
    "Rose Water",
    "Orange Red Powder",
    "Apple Green Powder",
    "Gole Marij Kali Mirch)",
    "Orange Red Powder Apple Green Powder",
    "Gole Marij(Kali Mirch)",
    "Kala Jeera",
    "Bada",
    "Ajwain",
    "Mirchi Powder",
    "Haldi Powder",
    "Sendha Namak (500gm) 1pkt",
    "Dhaniya Powder",
    "Bourn Vita",
    "Horlicks",
    "Javitri",
    "Dal Chini",
    "Sewai",
    "Arhar Dal (Toor Dal)",
    "Kabuli Chana",
    "Besan",
    "Rajma",
    "Chay Patti (Tea Leaves)",
    "Chay Patti (Tea Leaves)",
    "Phalli Dana (Peanut)",
    "Moong Dal",
    "Urad Dal",
    "Chana Dal",
    "Green Moong (Khada Moong)",
    "White Matar",
    "Dhaniya Khada",
    "Black Chana",
    "Sabudana",
    "Rice",
    "Idly Rice",
    "Soyabin Bari",
    "Tomato Souce",
    "Pickle",
    "Green Chilli (Souce)",
    "Red Chilli (Souce)",
    "Oll Dalda",
    "Soya Souce",
    "Vinegar",
    "Tomato Souce (Pouch)",
    "Water Tulsi",
    "oil",
    "Maza",
    "Sprite",
    "Thums Up",
    "Maza",
    "Maza",
    "Sprite",
    "Thums Up",
    "Magaj",
    "Methi",
    "Masoor Dal",
    "Mastered Seed Ajina Moto Salt",
    "(Raai)",
    "Kewada Water",
    "Corn Flower (Makka Atta Ararot)",
    "Frymes (Tikona Papad)",
    "Tamrind (imali)",
    "Sattu Atta",
    "Rosted Chana",
    "Ghadi Powder",
    "V-Hari Mirch-K",
    "V-Karela",
    "V-Kheera",
    "V-Khekhasi",
    "V-Lauki",
    "V-Parval",
    "V-Mooli",
    "V-Methi bhaji",
    "V-Green Matar",
    "V-Palak Bhaji",
    "V-Kadhi Leaves V-Spring Onion",
    "V-Kela",
    "V-Nibu (PIC/NOS)",
    "V-Kundru",
    "-Kaddu",
    "V-Hari Mirchi Big-K",
    "V-Shimla",
    "V-Tamatar",
    "V-Lal Bhaji",
    "V-Semi",
    "V-Hari Mirchi Big-K",
    "V-Shimla",
    "V-Tamatar",
    "V-Lal Bhaji",
    "V-Semi V-Pyaj",
    "V-Aloo",
    "Lahspon",
    "Green Elaichi",
    "Sauf",
    "Kaju Tukada",
    "Long",
    "Kismis",
    "Soda",
    "Tartari",
    "Mastered Oil",
    "Coffee (90gm) 1pkt Gulab Jal (250ml) 1Bott",
    "Pairie-G (Rs-5/-)",
    "Good Day (Rs-10/-)",
    "Chicken",
    "Amul Butter",
    "Amul Cheese",
    "Chocolate Syrup",
    "Pizza Souce",
    "Veg Mayonmise",
    "Sweet Corn",
    "GREEN MATAR",
    "Burger Tikki",
    "French Fries",
    "Yellow Color",
    "Maggi (280g",
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

users_data = CLIENT["aviskar"]["users_data"].find({}, limit=100)
names = users_data[0]

# print(list(dict(names["you_are"]).keys()))
print(len(raw_matirals))