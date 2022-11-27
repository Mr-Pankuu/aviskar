from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (310, 500)


class SlopeApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato\\Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato\\Lato-Bold.ttf")

    SlopeApp().run()
