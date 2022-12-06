from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.config import Config

Config.set("kivy", "keyboard_mode", "systemanddock")

Window.size = (310, 500)


class Main(MDScreen):
    def email(self):
        print("Helo world!!!")
        pass


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    pass


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
