from kivy.core.window import Window
from kivy.lang import Builder
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
    def email(self):
        print("Helo world!!!")


class Login(MDScreen):
    def check_and_upload(self):
        pass

    def upload_data(self):
        data = {
            "email": self.ids.email_data.text,
            "password": self.ids.password_data.text,
        }
        CLIENT["aviskar"]["users_data"].insert_one(data)
        print(data)


class Signup(MDScreen):
    pass


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    pass


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
