from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.config import Config
import pymongo
from pymongo import MongoClient

CLIENT = MongoClient("mongodb://localhost:27017")
Config.set("kivy", "keyboard_mode", "systemanddock")

Window.size = (310, 500)


class Main(MDScreen):
    def email(self, data):
        print(type(data))


class Login(MDScreen):
    def email(self, data):
        print(data)

    def login(self):
        email = self.ids.email_data.text
        password = self.ids.password_data.text
        user = CLIENT["aviskar"]["users_data"].find_one(
            {"email": email, "password": password}
        )
        if user == None:
            print("Invalid username or password.")
        else:
            print(user)


class Signup(MDScreen):
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
        else:
            CLIENT["aviskar"]["users_data"].insert_one(data)
            print(data)


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    pass


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
