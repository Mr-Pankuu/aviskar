import importlib
import os
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivymd.uix.widget import MDWidget
from kivy.core.text import LabelBase
from kivymd.uix.datatables import MDDataTable
from kivy.properties import StringProperty
from kivy.config import Config
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.dropdown import DropDown
from kivymd.material_resources import STANDARD_INCREMENT
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.list import ImageRightWidget, OneLineListItem
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.image import Image
import pymongo
from pymongo import MongoClient
from kivy.animation import Animation
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from twilio.rest import Client
from random import randint
import math
from os import system

client = Client(
    "AC07a81f1226651d58932b3890f2aa5e65", "24581999d659aed4f1b079b84016aab0"
)
CLIENT = MongoClient("mongodb://localhost:27017")
Config.set("kivy", "keyboard_mode", "systemanddock")
Window.size = (310, 500)
DATATABLE_PAGE_ROW_LIMIT = 100


class Test(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_it(self):
        pass


class Main(MDScreen):
    pass


class Tool:
    def on_row_press(self, instance_table, instance_row):
        row_index = int(instance_row.index)
        try:
            for i in range(
                math.floor(
                    int(instance_table.pagination.ids.label_rows_per_page.text[:3])
                    / DATATABLE_PAGE_ROW_LIMIT
                )
            ):
                row_index += len(instance_table.column_data) * DATATABLE_PAGE_ROW_LIMIT
        except:
            pass

        row_index = math.floor(row_index / len(instance_table.column_data))
        row_data = instance_table.row_data[row_index]

        print(row_data)


class Menuxx(MDScreen):
    spinner_text = StringProperty("Hello")

    def spinner_clicked(self, value):
        data = """You are enter in the Menuu site"""
        if value.lower() == "menu":
            # on_release:
            self.manager.transition.direction = "left"
            self.manager.current = "table"

        self.spinner_text = data
        print(value)


class MyLayout(MDWidget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"You select {value}"


class Admin(MDScreen):
    pass


class Admin_main(BoxLayout):
    pass


class Employee(MDScreen):
    spinner_text = StringProperty("Hello")

    def spinner_clicked(self, value):
        data = """You are enter in the admin site"""
        if value.lower() == "raw materials":
            # on_release:
            self.manager.transition.direction = "left"
            self.manager.current = "table"

        # elif value.lower() == "data analysis":

        # elif value.lower() == "sales":
        #     data= '''Now , You can see the sales analysis.'''

        self.spinner_text = data
        print(value)


class UserData(MDScreen):
    def on_pre_enter(self):
        self.graph()

    def graph(self):
        user_data = CLIENT["aviskar"]["users_data"]
        account_created_on = [i["account_created_on"][:4] for i in user_data.find({})]
        account_data_on_count = [
            (i, account_created_on.count(str(i)))
            for i in sorted([int(i) for i in set(account_created_on)])
        ]

        account_created_at = [i["account_created_at"][:2] for i in user_data.find({})]
        account_data_at_count = [
            (i, account_created_at.count(str(i)))
            for i in sorted([int(i) for i in set(account_created_at)])
        ]

        x = [i[0] for i in account_data_on_count]
        y = [i[1] for i in account_data_on_count]

        # x = [i[0] for i in account_data_at_count]
        # y = [i[1] for i in account_data_at_count]
        plt.clf()
        plt.plot(x, y)
        plt.ylabel("Account")
        plt.xlabel("Year")


class UserDataGraph(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class UserDataTable(MDBoxLayout, Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_data = list(CLIENT["aviskar"]["users_data"].find({}, limit=1000))
        self.data_table = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=DATATABLE_PAGE_ROW_LIMIT,
            column_data=[
                ("username", dp(30)),
                ("email", dp(30)),
                ("password", dp(30)),
                ("date of birth", dp(30)),
                ("you are", dp(30)),
                ("gender", dp(30)),
                ("age", dp(30)),
                ("favorite color", dp(30)),
                ("address", dp(30)),
                ("phone", dp(30)),
                ("account_created_on", dp(30)),
                ("account_created_at", dp(30)),
                ("privilege", dp(30)),
            ],
            row_data=[
                (
                    i["username"],
                    i["email"],
                    i["password"],
                    i["date_of_birth"],
                    list(i["you_are"].keys())[0],
                    i["gender"],
                    i["age"],
                    i["favorite_color"],
                    i["address"],
                    i["phone"],
                    i["account_created_on"],
                    i["account_created_at"],
                    i["privilege"],
                )
                for i in user_data
            ],
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)


class MenuData(MDScreen):
    def on_pre_enter(self):
        self.graph()

    def graph(self):
        data = CLIENT["aviskar"]["menu_item"]
        menu_data = [(i["name"], i["price"]) for i in data.find({})]

        x = [i[0] for i in menu_data]
        y = [i[1] for i in menu_data]

        plt.clf()
        plt.plot(x, y)
        plt.ylabel("Price")
        plt.xlabel("Item")


class MenuDataGraph(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class MenuDataTable(MDBoxLayout, Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        meun_item = list(CLIENT["aviskar"]["menu_item"].find({}))
        self.data_table = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=DATATABLE_PAGE_ROW_LIMIT,
            column_data=[
                ("item-name", dp(30)),
                ("price", dp(30)),
                ("helf-plate", dp(30)),
                ("full-plate", dp(30)),
                ("discount", dp(30)),
            ],
            row_data=[
                (
                    i["name"],
                    i["price"],
                    i["quantity"]["half"],
                    i["quantity"]["full"],
                    i["discount"],
                )
                for i in meun_item
            ],
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)


class SalesData(MDScreen):
    def on_pre_enter(self):
        self.graph()

    def graph(self):
        sale_data = CLIENT["aviskar"]["sales"]
        sales_date_set = sorted(set([int(i["date"][:4]) for i in sale_data.find({})]))
        sales_time_set = sorted(set([int(i["time"][:2]) for i in sale_data.find({})]))

        year = {str(i): [] for i in sales_date_set}
        print(year)
        for i in sale_data.find({}):
            year[i["date"][:4]].append(i["bought"]["total"])

        x = [int(i) for i in year.keys()]
        y = [sum(i) for i in year.values()]
        print(x)
        print(y)
        # x = [i[0] for i in account_data_at_count]
        # y = [i[1] for i in account_data_at_count]

        plt.clf()
        plt.plot(x, y)
        plt.ylabel("Sales")
        plt.xlabel("Year")


class SalesDataGraph(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class SalesTableData(MDBoxLayout, Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sales = list(CLIENT["aviskar"]["sales"].find({}, limit=1000))
        self.data_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=DATATABLE_PAGE_ROW_LIMIT,
            column_data=[
                ("username", dp(30)),
                ("email", dp(30)),
                ("phone", dp(30)),
                ("sales_of", dp(30)),
                ("date", dp(30)),
                ("time", dp(30)),
            ],
            row_data=[
                (
                    i["username"],
                    i["email"],
                    i["phone"],
                    i["bought"]["total"],
                    i["date"],
                    i["time"],
                )
                for i in sales
            ],
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)


class RawMaterial(MDScreen):
    pass


class RawMaterialDataTable(MDBoxLayout, Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raw_material = list(CLIENT["aviskar"]["raw_material"].find({}))
        self.data_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=DATATABLE_PAGE_ROW_LIMIT,
            column_data=[
                ("Item_name", dp(30)),
                ("Item_price", dp(30)),
                ("Item_in_stock", dp(30)),
                ("Total_items_worth", dp(30)),
            ],
            row_data=[
                (
                    i["item_name"],
                    i["item_price"],
                    i["item_in_stock"],
                    i["total_items_worth"],
                )
                for i in raw_material
            ],
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)


class InOut(MDScreen):
    def on_pre_enter(self):
        self.graph()

    def graph(self):
        month_name_data = {
            "01": ("January", 31),
            "02": ("February", 28),
            "03": ("March", 31),
            "04": ("April", 30),
            "05": ("May", 31),
            "06": ("June", 30),
            "07": ("July", 31),
            "08": ("August", 31),
            "09": ("September", 30),
            "10": ("October", 31),
            "11": ("November", 30),
            "12": ("December", 31),
        }
        inout_data = CLIENT["aviskar"]["in_out"]
        data = [
            (
                list(i.keys())[1],
                len(list(i.values())[1]["in"]),
                len(list(i.values())[1]["out"]),
                list(i.values())[1]["total_in"],
                list(i.values())[1]["total_out"],
            )
            for i in inout_data.find({})
        ]
        month_set = [
            "0" + str(i) if len(str(i)) == 1 else str(i)
            for i in sorted([int(i) for i in set([i[0][5:7] for i in data])])
        ]
        month_in_data = []
        month_out_data = []

        for i in month_set:
            in_item_sum = sum([j[3] for j in data if i == j[0][5:7]])
            out_item_sum = sum([j[4] for j in data if i == j[0][5:7]])

            month_in_data.append((i, in_item_sum))
            month_out_data.append((i, out_item_sum))

        x = [month_name_data[i[0]][0] for i in month_in_data]
        y = [i[1] / month_name_data[i[0]][1] for i in month_out_data]
        print(x)
        print(y)

        plt.clf()
        plt.plot(x, y)
        plt.ylabel("In")
        plt.xlabel("Year")


class InOutGraph(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class InOutDataTable(MDBoxLayout, Tool):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        in_out = list(CLIENT["aviskar"]["in_out"].find({}, limit=1000))
        self.data_table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=DATATABLE_PAGE_ROW_LIMIT,
            column_data=[
                ("Date", dp(30)),
                ("In-Count", dp(30)),
                ("Out-Count", dp(30)),
                ("In-Total-Cost", dp(30)),
                ("Out-Total-Cost", dp(30)),
            ],
            row_data=[
                (
                    list(i.keys())[1],
                    len(list(i.values())[1]["in"]),
                    len(list(i.values())[1]["out"]),
                    list(i.values())[1]["total_in"],
                    list(i.values())[1]["total_out"],
                )
                for i in in_out
            ],
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)


class Account(MDScreen):
    already_exist_message = StringProperty("")

    def account(self):
        data = {
            "username": self.ids.user_name_data.text,
            "email": self.ids.email_data.text,
            "password": self.ids.password_data.text,
            "privilege": self.ids.privilege_data.text,
        }
        if (
            CLIENT["aviskar"]["users_data"].find_one({"username": data["username"]})
            != None
        ):
            print("User of this name already exists.")
            self.already_exist_message = "User of this name already exists."
        else:
            CLIENT["aviskar"]["users_data"].insert_one(data)
            self.already_exist_message = ""
            print(data)

    def p_show_unshow(self):
        if self.ids.password_data.password == True:
            self.ids.password_data.password = False
            self.ids.p_password_icon.icon = "eye"

        elif self.ids.password_data.password == False:
            self.ids.password_data.password = True
            self.ids.p_password_icon.icon = "eye-off"


class Login(MDScreen):
    invalid_message = StringProperty("")

    def check_user(self):
        email = self.ids.email_data.text
        password = self.ids.password_data.text
        user = CLIENT["aviskar"]["users_data"].find_one(
            {"email": email, "password": password}
        )
        if user == None:
            self.invalid_message = "Invalid username or password."
            print("Invalid username or password.")
        else:
            self.invalid_message = ""
            print(user)
            if user["privilege"] == "admin":
                self.manager.transition.direction = "left"
                self.manager.current = "admin"
            elif user["privilege"] == "employee":
                self.manager.transition.direction = "left"
                self.manager.current = "employee"
            elif user["privilege"] == "user":
                self.manager.transition.direction = "left"
                self.manager.current = "Menuu"

    def p_show_unshow(self):
        if self.ids.password_data.password == True:
            self.ids.password_data.password = False
            self.ids.p_password_icon.icon = "eye"

        elif self.ids.password_data.password == False:
            self.ids.password_data.password = True
            self.ids.p_password_icon.icon = "eye-off"


class Signup(MDScreen):
    message = StringProperty("")

    def send_otp(self):
        global mess
        mess = randint(0, 999999)
        message = client.messages.create(
            body=mess,
            from_="+12017206236",
            to="+917247477955",
        )

    def sign_up(self):
        data = {
            "username": self.ids.user_name_data.text,
            "email": self.ids.email_data.text,
            "password": self.ids.password_data.text,
            "privilege": "user",
        }
        if (
            CLIENT["aviskar"]["users_data"].find_one({"username": data["username"]})
            != None
        ):
            print("User of this name already exists.")
            self.message = "User of this name already exists."
        elif self.ids.password_data.text != self.ids.confirm_password_data.text:
            self.message = "Password are not equal."
        elif self.ids.otp_data.text != str(mess):
            self.message = "Invalid OTP"
            self.ids.otp_button.text = "Resend OTP"
        else:
            CLIENT["aviskar"]["users_data"].insert_one(data)
            self.message = ""
            self.manager.transition.direction = "left"
            self.manager.current = "login"
            print(data)

    def p_show_unshow(self):
        if self.ids.password_data.password == True:
            self.ids.password_data.password = False
            self.ids.p_password_icon.icon = "eye"

        elif self.ids.password_data.password == False:
            self.ids.password_data.password = True
            self.ids.p_password_icon.icon = "eye-off"

    def cp_show_unshow(self):
        if self.ids.confirm_password_data.password == True:
            self.ids.confirm_password_data.password = False
            self.ids.cp_password_icon.icon = "eye"

        elif self.ids.confirm_password_data.password == False:
            self.ids.confirm_password_data.password = True
            self.ids.cp_password_icon.icon = "eye-off"


class Menu(MDScreen):
    pass
    # KV_FILES = {
    #     os.path.join(os.getcwd(), "foodlist_screen.kv"),
    #     os.path.join(os.getcwd(), "foodlist_screen.kv"),

    # }
    # CLASSES = {
    #     "Foody": "foodlist_screen",
    # }
    # AUTORELOADER_PATH = [
    #     (".", {"recursive": True}),
    # ]

    # def build_app(self):
    #     import foodlist_screen

    #     Window.bind(on_keyboard=self._rebuild)
    #     importlib.reload(foodlist_screen)

    #     return foodlist_screen.Foody()

    # def _rebuild(self, *args):
    #     if args[1] == 32:
    #         self._rebuild()


class Profile(MDScreen):
    pass


class LoadingPage(MDScreen):
    pass


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Orange"


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
#  ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
