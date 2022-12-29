from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.lang import Builder
import numpy as np
import pymongo
from pymongo import MongoClient

CLIENT = MongoClient("mongodb://localhost:27017")


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        
        print(account_data_on_count)
        print(account_data_at_count)
        
        x = [i[0] for i in account_data_on_count]
        y = [i[1] for i in account_data_on_count]

        # x = [i[0] for i in account_data_at_count]
        # y = [i[1] for i in account_data_at_count]

        plt.plot(x, y)
        plt.ylabel("Y Axis")
        plt.xlabel("X Axis")
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_it(self):
        pass


class GraphApp(MDApp):
    pass


GraphApp().run()

