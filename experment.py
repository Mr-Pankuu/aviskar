from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.lang import Builder
import numpy as np


x = np.array([0, 6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2050, 2250, 2500])

# x = [
#     1,
#     2,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
# ]
# y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")
# plt.show()

class Test(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    def save_it(self):
        pass


class GraphApp(MDApp):
    pass

GraphApp().run()
