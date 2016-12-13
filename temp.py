# -*- coding: cp850 -*-
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
from kivy.uix.spinner import Spinner

from kivy.garden.knob import Knob
from kivy.garden.gauges import Gauges
from kivy.garden.light_indicator import  Light_indicator

from kivy.properties import NumericProperty, BoundedNumericProperty, ListProperty, ObjectProperty, StringProperty



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
	
	h2o_ftemp = StringProperty('')
	h2o_ctemp = StringProperty('')
	
	def __init__(self, **kwargs):
			
		super(CoffeeScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
#		Clock.schedule_interval(self.disp_temp,0.1)

	def _finish_init(self,dt):
		
		self.set_ftemp=self.manager.get_screen('control').set_ftemp
		self.temp_value=self.manager.get_screen('control').temp_value
		self.my_temp=self.manager.get_screen('control').ids.my_temp
		#self.current_ctemp= str((self.temp_value -32)/1.8)





#	def disp_temp(self,dt):
#		self.set_ftemp = str(self.temp_value) 
#		self.h2o_temp = self.set_ftemp
		#self.my_temp = self.set_ftemp
		#self.temp_value = float(self.set_ftemp)
class ControlScreen(Screen):
	global event
	set_ftemp = StringProperty("")
	set_ctemp = StringProperty("")
	min=NumericProperty(80)
	max=NumericProperty(212)
	temp_value=NumericProperty(150.0)
	def __init__(self, **kwargs):
		
		super(ControlScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)
		
		Clock.schedule_interval(self.disp_temp,0.1)

	def _finish_init(self,dt):


		self.my_temp= self.ids.my_temp
		self.f_to_c()



	def disp_temp(self,dt):
		self.set_ftemp = str(self.temp_value)

	def f_to_c(self):

		self.current_ctemp= str(round((self.temp_value -32)/1.8,1))
		self.set_ctemp = self.current_ctemp
		
		
		print "set_temp is: ",self.set_ftemp 
		print "temp_val is: ",self.temp_value 
		
	def increase_temp(self):


		if self.temp_value<self.max:
			self.temp_value+=1
			self.f_to_c()
			

			
			print "set_temp is: ",self.set_ftemp 
			print "temp_value is: ",self.temp_value 
	def decrease_temp(self):
		
		if self.temp_value>self.min:
			self.temp_value-=1
			self.f_to_c()

 
#Building the app. The program will look for the file "nuclear.kv" because the app is called Nuclear			
class TempApp(App):
	def build(self):
		Config.set('graphics','fullscreen', True)
		return CoffeeScreenManager()
# Run the program
if __name__ == "__main__":
	TempApp().run()

