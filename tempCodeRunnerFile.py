from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.lang import Builder
import numpy as np


x = np.array([0, 6,10,20,30,40,50,60,70,80,90,100])