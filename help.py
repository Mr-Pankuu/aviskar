import numpy as np
import pymongo
from pymongo import MongoClient
from faker import Faker
from random import randint, choice
import datetime
import time
import randomtimestamp
from os import system

raw_matirals = [
    ("Salt", "kg", 10),
    ("Papad (Sagun)", "kg", 50),
    ("Sugar", "kg", 40),
    ("Poha", "kg", 40),
    ("Maida", "kg", 40),
    ("Atta", "kg", 30),
    ("Sooji", "kg", 50),
    ("Shabji Biryani Masala", "kg", 550),
    ("Kitchen King", "kg", 750),
    ("Paw Bhaji Masala", "kg", 440),
    ("Sambhar Masala", "kg", 600),
    ("Chiken Masala", "kg", 1000),
    ("Chana Masala Chole Masala)", "kg", 800),
    ("Chat Masala (100gm pkt)", "pkt", 100),
    ("Kasoori Methi(250gm pkt)", "pkt", 200),
    ("Jeera", "kg", 400),
    ("Hing", "bott", 100),
    ("Rose Water", "bott", 200),
    ("Orange Red Powder", "bott", 340),
    ("Apple Green Powder", "bott", 440),
    ("Gole Marij Kali Mirch)", "kg", 560),
    ("Orange Red Powder Apple Green Powder", "kg", 1020),
    ("Gole Marij(Kali Mirch)", "kg", 560),
    ("Kala Jeera", "kg", 500),
    ("Bada", "kg", 400),
    ("Ajwain", "kg", 700),
    ("Mirchi Powder", "kg", 200),
    ("Haldi Powder", "kg", 200),
    ("Sendha Namak (500gm pkt)", "pkt", 30),
    ("Dhaniya Powder", "kg", 300),
    ("Bourn Vita", "kg", 300),
    ("Horlicks", "kg", 470),
    ("Javitri", "kg", 600),
    ("Dal Chini", "kg", 600),
    ("Sewai", "kg", 70),
    ("Arhar Dal (Toor Dal)", "kg", 100),
    ("Kabuli Chana", "kg", 120),
    ("Besan", "kg", 80),
    ("Rajma", "kg", 150),
    ("Chay Patti (Tea Leaves)", "kg", 250),
    ("Chay Patti (Tea Leaves)", "kg", 250),
    ("Phalli Dana (Peanut)", "kg", 130),
    ("Moong Dal", "kg", 120),
    ("Urad Dal", "kg", 160),
    ("Chana Dal", "kg", 80),
    ("Green Moong (Khada Moong)", "kg", 120),
    ("White Matar", "kg", 150),
    ("Dhaniya Khada", "kg", 200),
    ("Black Chana", "kg", 70),
    ("Sabudana", "kg", 80),
    ("Rice", "kg", 48),
    ("Idly Rice", "kg", 40),
    ("Soyabin Bari", "kg", 100),
    ("Tomato Souce", "bott", 80),
    ("Pickle", "bott", 400),
    ("Green Chilli (Souce)", "bott", 150),
    ("Red Chilli (Souce)", "bott", 150),
    ("Oil Dalda", "kg", 130),
    ("Soya Souce", "kg", 130),
    ("Vinegar", "kg", 200),
    ("Tomato Souce (Pouch)", "kg", 97),
    ("Water Tulsi", "kg", 340),
    ("oil", "bott", 157),
    ("Mazza", "bott", 57),
    ("Sprite", "bott", 55),
    ("Thums Up", "bott", 47),
    ("Magaj", "kg", 630),
    ("Methi", "kg", 230),
    ("Masoor Dal", "kg", 140),
    ("Mastered Seed Ajina Moto Salt", "kg", 70),
    ("Kewada Water", "kg", 300),
    ("Corn Flower (Makka Atta Ararot)", "kg", 340),
    ("Frymes (Tikona Papad)", "kg", 300),
    ("Tamrind (imali)", "kg", 90),
    ("Sattu Atta", "kg", 60),
    ("Rosted Chana", "kg", 100),
    ("Ghadi Powder", "kg", 58),
    ("V-Hari Mirch-K", "kg", 60),
    ("V-Karela", "kg", 40),
    ("V-Kheera", "kg", 30),
    ("V-Khekhasi", "kg", 80),
    ("V-Lauki", "kg", 20),
    ("V-Parval", "kg", 30),
    ("V-Mooli", "kg", 30),
    ("V-Methi bhaji", "kg", 50),
    ("V-Green Matar", "kg", 60),
    ("V-Palak Bhaji", "kg", 30),
    ("V-Kadhi Leaves V-Spring Onion", "kg", 30),
    ("V-Kela", "kg", 30),
    ("V-Nibu (PIC/NOS)", "kg", 50),
    ("V-Kundru", "kg", 50),
    ("-Kaddu", "kg", 40),
    ("V-Hari Mirchi Big-K", "kg", 80),
    ("V-Shimla", "kg", 30),
    ("V-Tamatar", "kg", 10),
    ("V-Lal Bhaji", "kg", 40),
    ("V-Semi V-Pyaj", "kg", 30),
    ("V-Aloo", "kg", 20),
    ("Lahspon", "kg", 50),
    ("Green Elaichi", "kg", 2000),
    ("Sauf", "kg", 100),
    ("Kaju Tukada", "kg", 800),
    ("Long", "kg", 1700),
    ("Kismis", "kg", 200),
    ("Soda", "kg", 70),
    ("Tartari", "kg", 1500),
    ("Mastered Oil", "kg", 155),
    ("Coffee (90gm pkt)", "pkt", 332),
    ("Pairie-G", "pkt", 200),
    ("Good Day", "pkt", 200),
    ("Chicken", "kg", 200),
    ("Amul Butter", "kg", 800),
    ("Amul Cheese", "kg", 600),
    ("Chocolate Syrup", "kg", 200),
    ("Pizza Souce", "kg", 170),
    ("Veg Mayonmise", "kg", 180),
    ("Sweet Corn", "kg", 52),
    ("GREEN MATAR", "kg", 40),
    ("Burger Tikki", "pkt", 25),
    ("French Fries", "kg", 340),
    ("Yellow Color", "bott", 50),
    ("Maggi (280g pkt)", "pkt", 40),
    ("Gulab Jal (250ml Bott)", "bott", 50),
]

system("clear")

CLIENT = MongoClient("mongodb://localhost:27017")
user_data = CLIENT["aviskar"]["users_data"]

faker_data = Faker(locale="en_IN")
while True:
    print("user, menu, sales, in out, raw material")
    genrate_data_of = input("Enter what kind of data to genrate:- ")

    if genrate_data_of == "user":
        for i in range(int(input("Enter the number of user to input:- "))):
            while True:
                phone = faker_data.phone_number()
                if phone[0] == "+":
                    break
                else:
                    continue
            today = str(datetime.date.today())
            age = randint(15, 65)
            dob = str(int(today[:4]) - age) + today[4:]

            collage = "RCST"
            course = "BCA"
            collage_year = randint(1, 4)

            you_are_data_list = ["student", "non-student"]
            you_are = choice(you_are_data_list)
            account_created_on = str(
                randomtimestamp.random_date(
                    start=datetime.datetime.strptime("2012-01-01", "%Y-%m-%d").date()
                )
            )

            if you_are != "student":
                collage = None
                course = None
                collage_year = None

            user = {
                "username": faker_data.name(),
                "email": "nico.zero.0x@gmail.com",
                "password": "nicozero",
                "date_of_birth": dob,
                "you_are": {
                    you_are: {
                        "collage": collage,
                        "course": course,
                        "collage_year": collage_year,
                    }
                },
                "gender": choice(["Male", "Female"]),
                "age": age,
                "favorite_color": faker_data.color_name(),
                "address": faker_data.address().replace("\n", " "),
                "phone": phone,
                "account_created_on": account_created_on,
                "account_created_at": faker_data.time(),
                "privilege": "user",
            }
            print(user)
            user_data.insert_one(user)
    elif genrate_data_of == "menu":
        food_list = {
            "plain dosa": 20,
            "masala dosa": 25,
            "cutpiece dosa": 30,
            "uttapam": 25,
            "sambhar vada (2cps)": 20,
            "idly (2pcs)": 15,
            "poha": 15,
            "chana poha": 20,
            "samosa (2pcs)": 20,
            "samosa mutter": 25,
            "dahi samosa": 30,
            "aalu gunda (2pcs)": 15,
            "aalu gunda mutter": 20,
            "tea": 10,
            "coffee": 15,
            "sabudana khichdi": 20,
            "sabudana vada (3pcs)": 20,
            "hot milk per glass": 15,
            "aalo paratha": 30,
            "paneer paratha": 30,
            "chhole bhature": 30,
            "veg sandwitch": 20,
            "bread pakoda (1pcs)": 10,
            "bhajiya piyagi": 15,
            "pyaji vada": 10,
            "momos (6pcs)": 20,
        }
        food = [
            {
                "name": i,
                "price": j,
                "quantity": {"half": round(j / 2), "full": j},
                "discount": None,
            }
            for i, j in food_list.items()
        ]
        print(food)
        user_data = CLIENT["aviskar"]["menu_item"].insert_many(food)

    elif genrate_data_of == "sales":
        data = list(user_data.find({}, limit=int(input("Number of user:- "))))        menu_data = list(CLIENT["aviskar"]["menu_item"].find({}))

        for i in data:
            item = {}
            for _ in range(randint(1, 10)):
                x = choice(menu_data)
                item.update(
                    {x["name"]: {"price": x["price"], "quantity": randint(1, 10)}}
                )

            bought = {
                "items": item,
                "total": sum([i["price"] * i["quantity"] for i in item.values()]),
            }
            date = str(faker_data.date_this_year())

            start_time_object = datetime.datetime.strptime(
                "09::00::00", "%H::%M::%S"
            ).time()
            end_time_object = datetime.datetime.strptime(
                "18::00::00", "%H::%M::%S"
            ).time()

            rand_time = str(
                randomtimestamp.random_time(
                    start=start_time_object, end=end_time_object
                )
            )

            item_data = {
                "username": i["username"],
                "email": i["email"],
                "phone": i["phone"],
                "bought": bought,
                "date": date,
                "time": rand_time,
            }
            print(item_data)
            user_data = CLIENT["aviskar"]["sales"].insert_one(item_data)

    elif genrate_data_of == "in out":

        def genrate_date(from_, to):
            return [str(i) for i in np.arange(from_, to, dtype="datetime64[D]")]

        def generate_raw_matarial(x: int, qu_r: int):
            raw_m = list(set([choice(raw_matirals) for _ in range(x)]))
            g_r_m = {}
            for i in raw_m:
                q = randint(5, qu_r)
                d = {
                    i[0]: {
                        "quintity": q,
                        "unit": i[1],
                        "item_price": i[2],
                        "total_price": q * i[2],
                    }
                }
                g_r_m.update(d)
            return g_r_m

        def cal_total_price(data: dict):
            return sum([i["total_price"] for i in data.values()])

        date_data = genrate_date("2022-01", "2022-12-23")

        i_data = []
        for i in date_data:
            in_data = generate_raw_matarial(randint(5, 25), 100)
            total_in = cal_total_price(in_data)
            out_data = generate_raw_matarial(randint(5, 20), 40)
            total_out = cal_total_price(out_data)

            di = {
                i: {
                    "in": in_data,
                    "total_in": total_in,
                    "out": out_data,
                    "total_out": total_out,
                }
            }
            print(di)
            i_data.append(di)

        raw_mar_data = CLIENT["aviskar"]["in_out"]
        raw_mar_data.insert_many(i_data)

    elif genrate_data_of == "raw material":
        raw_matiral_name = [i[0] for i in raw_matirals]

        in_out_data = CLIENT["aviskar"]["in_out"].find({})
        f_in_out_data = [tuple(i.values())[1] for i in list(in_out_data)]

        in_data = [i["in"] for i in f_in_out_data]
        out_data = [i["out"] for i in f_in_out_data]

        def short_the_data(data):
            shorted_data = []
            for i in data:
                d = [
                    (x, y["quintity"]) if y["quintity"] >= 0 else (x, 100)
                    for x, y in i.items()
                ]
                shorted_data = shorted_data + d
            return shorted_data

        f_in_data = short_the_data(in_data)
        f_out_data = short_the_data(out_data)

        def calculate_data(data):
            calculated_data = []
            for i in raw_matiral_name:
                c_d = sum([x[1] for x in data if x[0] == i])
                calculated_data.append((i, c_d))
            return calculated_data

        summed_in_data = calculate_data(f_in_data)
        summed_out_data = calculate_data(f_out_data)

        calculated_raw_material_data = [
            (i[0], i[1] - j[1])
            for i, j in zip(summed_in_data, summed_out_data)
            if i[0] == j[0]
        ]

        org_raw_matiral_data = [
            {
                "item_name": i[0],
                "item_price": j[2],
                "item_in_stock": i[1],
                "total_items_worth": j[2] * i[1],
            }
            for i, j in zip(calculated_raw_material_data, raw_matirals)
            if i[0] == j[0]
        ]

        print(org_raw_matiral_data)
        raw_material = CLIENT["aviskar"]["raw_material"]
        raw_material.insert_many(org_raw_matiral_data)

    if input("Want to insert more data (Yes or No):- ").lower() in ["yes", "y"]:
        system("clear")
        continue
    else:
        system("clear")
        print("Thank you for using my services.")
        break
