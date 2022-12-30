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
from kivy.metrics import dp
from kivy.uix.button import Button
import pymongo
from pymongo import MongoClient
from kivy.animation import Animation
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.clock import Clock
from kivymd.uix.screen import Screen

CLIENT = MongoClient("mongodb://localhost:27017")
Config.set("kivy", "keyboard_mode", "systemanddock")
Window.size = (310, 500)


class Test(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_it(self):
        pass


class Main(MDScreen):
    pass


class Menu(MDScreen):
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
    spinner_text = StringProperty("Hello")

    def spinner_clicked(self, value):
        data = """You are enter in the admin site"""

        if value == "Raw Materials analysis":
            self.manager.transition.direction = "left"
            self.manager.current = "raw_material"

        elif value == "Product analysis":
            self.manager.transition.direction = "left"
            self.manager.current = "in_out"

        elif value == "Sales analysis":
            self.manager.transition.direction = "left"
            self.manager.current = "salesdata"

        elif value == "User Data Analysis":
            self.manager.transition.direction = "left"
            self.manager.current = "userdata"

        self.spinner_text = data
        print(value)


class Admin_main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # size = dp(100)
        # b = Button(text=f"{i}", size_hint=(None, None), size=(size, size))
        # self.add_widget(b)


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


class UserDataTable(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_data = list(CLIENT["aviskar"]["users_data"].find({}, limit=1000))
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=20,
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
        self.add_widget(self.data_tables)


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


class MenuDataTable(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        meun_item = list(CLIENT["aviskar"]["menu_item"].find({}))
        self.data_table = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=20,
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
        self.add_widget(self.data_table)


class SalesData(MDScreen):
    def on_pre_enter(self):
        self.graph()

    def graph(self):
        sale_data = CLIENT["aviskar"]["sales"]
        sales_date_set = sorted(set([int(i["date"][:4]) for i in sale_data.find({})]))
        sales_time_set = sorted(set([int(i["time"][:2]) for i in sale_data.find({})]))

        year = {str(i):[] for i in sales_date_set}
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


class SalesTableData(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sales = list(CLIENT["aviskar"]["sales"].find({}, limit=100))
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
            rows_num=20,
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
        self.add_widget(self.data_tables)


class RawMaterial(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raw_material = list(CLIENT["aviskar"]["raw_material"].find({}, limit=100))
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(0.35, 0.65),
            use_pagination=True,
            # check=True,
            rows_num=20,
            column_data=[
                ("item_name", dp(30)),
                ("item_price", dp(30)),
                ("item_in_stock", dp(30)),
                ("total_items_worth", dp(30)),
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
        self.add_widget(self.data_tables)


class InOut(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        in_out = list(CLIENT["aviskar"]["in_out"].find({}, limit=100))
        self.data_tables = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.47},
            size_hint=(0.35, 0.65),
            use_pagination=True,
            # check=True,
            rows_num=20,
            column_data=[
                ("_id", dp(30)),
            ],
            row_data=[(i["_id"],) for i in in_out],
        )
        self.add_widget(self.data_tables)


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


class LoadingPage(MDScreen):
    pass


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.theme_cls.theme_style = "Dark"


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
