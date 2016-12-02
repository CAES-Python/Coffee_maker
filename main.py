from kivy.app import App

from kivy.clock import Clock
from kivy.clock import Clock as clock

from kivy.config import Config
from kivy.gesture import Gesture,GestureDatabase

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse)
from kivy.graphics.context_instructions import Color

from kivy.lang import Builder

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown

from kivy.garden.knob import Knob
from kivy.garden.gauges import Gauges
from kivy.garden.light_indicator import  Light_indicator

from kivy.properties import ListProperty, ObjectProperty



import collections 
import math
import os
import random
import sys
from math import *


import gesture_box as gesture

# This is where Kivy captures gestures.
class Runner(gesture.GestureBox):
	pass


#define the Screen Manager
class CoffeeScreenManager(ScreenManager):
	pass
#define the screens

class MenuScreen(Screen):
	pass
class CoffeeScreen(Screen):
	pass
class ControlScreen(Screen):
	pass

#Building the app. The program will look for the file "nuclear.kv" because the app is called Nuclear			
class CoffeeApp(App):
	def build(self):
		Config.set('graphics','fullscreen', 'auto')
		return CoffeeScreenManager()
# Run the program
if __name__ == "__main__":
	CoffeeApp().run()

