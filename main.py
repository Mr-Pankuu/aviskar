from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
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


CLIENT = MongoClient("mongodb://localhost:27017")
Config.set("kivy", "keyboard_mode", "systemanddock")
Window.size = (310, 500)


class Main(MDScreen):
    pass


class Men(MDScreen):
    pass


class MyLayout(MDWidget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"You select {value}"


class Admin(MDScreen):
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


class Admin_main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # size = dp(100)
        # b = Button(text=f"{i}", size_hint=(None, None), size=(size, size))
        # self.add_widget(b)


class UserDataTable(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_data = list(CLIENT["aviskar"]["users_data"].find({}, limit=1000))
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(1, 1),
            use_pagination=True,
            # check=True,
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
                    i["privilege"],
                )
                for i in user_data
            ],
        )
        self.add_widget(self.data_tables)


# class Table(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.data_tables = MDDataTable(
#             pos_hint={"center_y": 0.5, "center_x": 0.5},
#             size_hint=(1, 1),
#             use_pagination=True,
#             # check=True,
#             column_data=[
#                 ("No.", dp(30)),
#                 ("Head 1", dp(30)),
#                 ("Head 2", dp(30)),
#                 ("Head 3", dp(30)),
#                 ("Head 4", dp(30)),
#             ],
#             row_data=((f"{i + 1}", "Salt", "Besan", "Maida", "Aata") for i in range(60)),
#         )
#         self.add_widget(self.data_tables)


class Account(MDScreen):
    already_exist_message = StringProperty("")

    def account(self):
        data = {
            "username": self.ids.user_name_data.text,
            "email": self.ids.email_data.text,
            "password": self.ids.password_data.text,
            "privilege": "user",
            "privilege": "emplyoee",
            "privilege": "admin",
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
                self.manager.current = "menu"


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
            print(data)


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
