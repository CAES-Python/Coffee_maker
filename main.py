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
	cup_size = StringProperty('')
	pod_select = StringProperty('')
	h2o_ftemp = StringProperty('')
	h2o_ctemp = StringProperty('')

	def __init__(self, **kwargs):			
		super(CoffeeScreen, self).__init__(**kwargs)

class ControlScreen(Screen):
	global event
	size_text=StringProperty("")
	pod_text = StringProperty("")
	set_ftemp = StringProperty("")
	set_ctemp = StringProperty("")
	min=NumericProperty(80)
	max=NumericProperty(212)
	temp_value=NumericProperty(150)
	size_value=NumericProperty(6)
	min_size =NumericProperty(4)
	max_size =NumericProperty(14)
	def __init__(self, **kwargs):
		
		super(ControlScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)
		Clock.schedule_interval(self.disp_size,0.1)
		Clock.schedule_interval(self.disp_pod,0.5)
		Clock.schedule_interval(self.disp_temp,0.1)
		Clock.schedule_interval(self.water_level,0.5)
	def _finish_init(self,dt):
		self.water_lights=self.manager.get_screen('coffee').ids.water_lv_lights
		self.alt_light= self.manager.get_screen('coffee').ids.altitude_light
		self.air_light= self.manager.get_screen('coffee').ids.air_pump_light
		self.water_light=self.manager.get_screen('coffee').ids.water_pump_light
		self.door_light=self.manager.get_screen('coffee').ids.pod_door_light
		self.color = self.manager.get_screen('coffee').ids.pod_color
		self.carafe_light= self.manager.get_screen('coffee').ids.carafe_light
		self.led_light= self.manager.get_screen('coffee').ids.led_light
		self.pod_light= self.manager.get_screen('coffee').ids.pod_light
		self.home_sensor = self.manager.get_screen('coffee').ids.home_sensor
		self.pod_options=self.ids.pod_options
		self.f_to_c()
		self.alt_status=False
		self.air_status=False
		self.water_status=False
		self.door_status=False
		self.pod_status=False
		self.carafe_status=False
		self.home_status=False

	def alt_mode_on_off(self):
		if self.alt_status == False:
			self.alt_light.turn_on_l1()
			self.alt_status = True
		else:
			self.alt_light.turn_off_l1()
			self.alt_status = False

	def turn_air_on_off(self):
		if self.air_status == False:
			self.air_light.turn_on_l1()
			self.air_status = True
		else:
			self.air_light.turn_off_l1()
			self.air_status = False

	def turn_water_on_off(self):
		if self.water_status == False:
			self.water_light.turn_on_l1()
			self.water_status = True
		else:
			self.water_light.turn_off_l1()
			self.water_status = False


	def open_close_door(self):
		if self.door_status == False:
			self.door_light.color1='green'
			self.door_status =True
		else:
			self.door_light.color1='red'
			self.door_status =False

	def insert_remove_pod(self):
		if self.pod_status==False:
			self.pod_light.color1='green'
			self.pod_status=True
		else:
			self.pod_light.color1='red'
			self.pod_status = False
		
	def insert_remove_carafe(self):
		if self.carafe_status == False:
			self.carafe_light.color1='green'
			self.carafe_status = True
		else:
			self.carafe_light.color1='red'
			self.carafe_status = False
	def home_on_off(self):
		if self.home_status == False:
			self.home_sensor.turn_on_l1()
			self.home_status = True
		else:
			self.home_sensor.turn_off_l1()
			self.home_status = False

	def LED_on(self):
		try:
			self.event.cancel()
		except:
			pass
		self.led_light.turn_on_l1()

	def LED_off(self):
		try:
			self.event.cancel()
		except:
			pass		
		self.led_light.turn_off_l1()

	def LED_flash(self):
		self.event=Clock.schedule_interval(self.flash,0.1)

	def flash(self,dt):
		if self.led_light.bol1==True:
			self.led_light.bol1 =False
		else:
			self.led_light.bol1=True

	def disp_size(self,dt):
		self.size_text=str(self.size_value)

	def disp_pod(self,dt):
		self.pod_text = self.pod_options.text

	def water_level(self,dt):
		self.water_lights=self.manager.get_screen('coffee').ids.water_lv_lights
		self.water_value=self.ids.water_lv_knob.value 
		if self.water_value <25:
			self.water_lights.turn_off_l2()
			self.water_lights.turn_off_l3()
			self.water_lights.turn_on_l1()
			
		elif self.water_value > 80:
			self.water_lights.turn_off_l2()
			self.water_lights.turn_off_l1()
			self.water_lights.turn_on_l3()
			
		else:
			self.water_lights.turn_off_l1()
			self.water_lights.turn_off_l3()
			self.water_lights.turn_on_l2()

	def disp_temp(self,dt):
		self.set_ftemp = str(self.temp_value)

	def f_to_c(self):
		self.current_ctemp= str(round((self.temp_value -32)/1.8,1))
		self.set_ctemp = self.current_ctemp
		
	def increase_temp(self):
		if self.temp_value<self.max:
			self.temp_value+=1
			self.f_to_c()
			
	def decrease_temp(self):
		if self.temp_value>self.min:
			self.temp_value-=1
			self.f_to_c()

	def increase_size(self):
		if self.size_value<self.max_size:
			self.size_value+=0.5

	def decrease_size(self):
		
		if self.size_value>self.min_size:
			self.size_value-=0.5
			
#Building the app. The program will look for the file "coffee.kv" because the app is called Coffee			
class CoffeeApp(App):
	def build(self):
		Config.set('graphics','fullscreen', True)
		return CoffeeScreenManager()
# Run the program
if __name__ == "__main__":
	CoffeeApp().run()

