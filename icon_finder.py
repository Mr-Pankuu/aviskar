from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.config import Config
Config.set("kivy", "keyboard_mode", "systemanddock")



class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_list_md_icons
    

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


class Icon_finderApp(MDApp):
    pass


Icon_finderApp().run()