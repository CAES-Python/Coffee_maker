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
'''def __init__(self, **kwargs):
			
		super(CoffeeScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)

	def _finish_init(self,dt):
		self.water_lights=self.ids.water_lv_lights
		self.temp = self.ids.water_temp_disp
		self.ftemp= self.ids.ftemp
		self.ctemp= self.ids.ctemp
		self.alt_light= self.ids.altitude_light
		self.air_light=self.ids.air_pump_light
		self.water_pump=self.ids.water_pump_light
		self.water_vol=self.ids.water_vol
		self.door_light=self.ids.pod_door_light
		self.color = self.ids.pod_color
		self.carafe_light= self.ids.carafe_light
		self.led_light= self.ids.led_light
		self.water_value=self.manager.get_screen('control').ids.water_lv_knob.value 
		self.alt_on=self.manager.get_screen('control').ids.alt_mode_on
		self.alt_off=self.manager.get_screen('control').ids.alt_mode_off
		self.air_on=self.manager.get_screen('control').ids.air_pump_on
		self.air_off=self.manager.get_screen('control').ids.air_pump_off
		self.water_on=self.manager.get_screen('control').ids.water_pump_on
		self.water_off=self.manager.get_screen('control').ids.water_pump_off
		self.sizes=self.manager.get_screen('control').ids.sizes
		self.door_open=self.manager.get_screen('control').ids.pod_door_open
		self.door_closed=self.manager.get_screen('control').ids.pod_door_closed
		self.pod_present=self.manager.get_screen('control').ids.pod_present
		self.pos_missing=self.manager.get_screen('control').ids.pod_missing
		self.pod_options=self.manager.get_screen('control').ids.pod_options
		self.carafe_present=self.manager.get_screen('control').ids.carafe_present
		self.carafe_missing=self.manager.get_screen('control').ids.carafe_missing
		self.led_off=self.manager.get_screen('control').ids.led_off
		self.led_on=self.manager.get_screen('control').ids.led_on
		self.led_flash=self.manager.get_screen('control').ids.led_flash'''

	
class ControlScreen(Screen):
	global event
	def __init__(self, **kwargs):
		
		super(ControlScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init,0.5)

	def _finish_init(self,dt):
		self.water_lights=self.manager.get_screen('coffee').ids.water_lv_lights
		self.temp = self.manager.get_screen('coffee').ids.water_temp_disp
		self.ftemp= self.manager.get_screen('coffee').ids.ftemp
		self.ctemp= self.manager.get_screen('coffee').ids.ctemp
		self.alt_light= self.manager.get_screen('coffee').ids.altitude_light
		self.air_light= self.manager.get_screen('coffee').ids.air_pump_light
		self.water_light=self.manager.get_screen('coffee').ids.water_pump_light
		self.water_vol=self.manager.get_screen('coffee').ids.water_vol
		self.door_light=self.manager.get_screen('coffee').ids.pod_door_light
		self.color = self.manager.get_screen('coffee').ids.pod_color
		self.carafe_light= self.manager.get_screen('coffee').ids.carafe_light
		self.led_light= self.manager.get_screen('coffee').ids.led_light
		self.pod_light= self.manager.get_screen('coffee').ids.pod_light
		self.water_value=self.ids.water_lv_knob.value 
		self.alt_on=self.ids.alt_mode_on
		self.alt_off=self.ids.alt_mode_off
		self.air_on=self.ids.air_pump_on
		self.air_off=self.ids.air_pump_off
		self.water_on=self.ids.water_pump_on
		self.water_off=self.ids.water_pump_off
		self.sizes=self.ids.sizes
		self.door_open=self.ids.pod_door_open
		self.door_closed=self.ids.pod_door_closed
		self.pod_present=self.ids.pod_present
		self.pos_missing=self.ids.pod_missing
		self.pod_options=self.ids.pod_options
		self.carafe_present=self.ids.carafe_present
		self.carafe_missing=self.ids.carafe_missing
		self.led_off=self.ids.led_off
		self.led_on=self.ids.led_on
		self.led_flash=self.ids.led_flash

	def alt_mode_on(self):
		self.alt_light.turn_on_l1()
	def alt_mode_off(self):
		self.alt_light.turn_off_l1()
	def turn_air_on(self):
		self.air_light.turn_on_l1()
	def turn_air_off(self):
		self.air_light.turn_off_l1()
	def turn_water_on(self):
		self.water_light.turn_on_l1()
	def turn_water_off(self):
		self.water_light.turn_off_l1()
	def open_door(self):
		self.door_light.color1='red'
	def close_door(self):
		self.door_light.color1='green'
	def insert_pod(self):
		self.pod_light.color1='green'
	def remove_pod(self):
		self.pod_light.color1='red'
	def insert_carafe(self):
		self.carafe_light.color1='green'
	def remove_carafe(self):
		self.carafe_light.color1='red'
	def LED_on(self):
		self.event.cancel()
		self.led_light.turn_on_l1()
	def LED_off(self):
		self.event.cancel()
		self.led_light.turn_off_l1()
	def LED_flash(self):
		self.event=Clock.schedule_interval(self.flash,0.1)
	def flash(self,dt):
		if self.led_light.bol1==True:
			self.led_light.bol1 =False
		else:
			self.led_light.bol1=True
		

#Building the app. The program will look for the file "nuclear.kv" because the app is called Nuclear			
class CoffeeApp(App):
	def build(self):
		Config.set('graphics','fullscreen', 'auto')
		return CoffeeScreenManager()
# Run the program
if __name__ == "__main__":
	CoffeeApp().run()

