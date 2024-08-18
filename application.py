import kivy
from kivy import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio.audio_sdl2 import SoundLoader
import random
import webbrowser
import time
	

class SigmaApp(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols = 1
		Window.size = (1250, 2500)
		
		#Label
		self.label_text= Label(text="Ciao bro, vediamo quanto sei sigma!1!1(BETA)",   size_hint=(1, 50), font_size = "20sp")
		self.window.add_widget(self.label_text)
		
		#Skibidi Image
		self.skibidi = Image(source="skibidi.jpg", size_hint=(1, 150), allow_stretch=True, keep_ratio=False)
		self.window.add_widget(self.skibidi)
		
		#Er pursante maggico
		self.godo = Button(text="Testa quanto sei sigma", size_hint=(0.5, 25), font_size="20sp", italic=True, background_color = "#dc143c",)
		self.window.add_widget(self.godo)
		
		#Er Mega pursantone home
		self.home = Button(text="Restart", size_hint=(0.5, 300), font_size="30sp", italic = True, background_color="#8B4513", on_press = self.HomeFunc)
		

		
		
		
		#Funzionalità der pursante maggico
		self.godo.bind(on_press=self.SigmaFunc)
		
		return self.window
		
			
				
	def SigmaFunc(self, instance):
		self.number = random.randint(1, 100)
		#<50 Sigma%
		if self.number < 50:
			self.window.clear_widgets()
			self.window.add_widget(self.home)
			self.home.text = "Restart"
			self.home.background_color = "#8B4513"
			self.window.add_widget(Image(source="notsigma.jpg", size_hint=(1, 1800), allow_stretch=True, keep_ratio=True))
			self.window.add_widget(Label(text=f"Il bro ha una bassa percentuale di sigma ({self.number}%)", size_hint = (1, 100), font_size="20sp", bold=True))
		
		#Easter Egg
		elif self.number == 69:
			self.song=SoundLoader.load("inside-the-matrix.mp3").play()
			self.window.clear_widgets()
			self.window.add_widget(Label(text="Per fermare la musica chiudi app", size_hint = (1, 200), font_size = "20sp", bold=True))
			self.window.add_widget(Label(text="Ora, dimmi, pillola rossa o pillola blu?", size_hint=(1,300), font_size = "20sp", bold=False))
			self.window.add_widget(self.home)
			self.home.text = "Pillola rossa"
			self.home.background_color="#dc143c"
			self.window.add_widget(Button(text="Pillola blu", size_hint=(0.5, 300), font_size = "20sp", italic =True, background_color = "#1919e6", on_press= self.OpenWeb ))
			self.window.add_widget(Image(source="Matrix.jpg", size_hint=(1, 2000), allow_stretch=True, keep_ratio=True))
			
			self.window.add_widget(Label(text="Benvenuto nella tana del bianconiglio, \n Sei entrato nel matrix amico", size_hint = (1, 300), font_size= "25sp", bold=True, italic=True))
			
		#Classic	
		elif self.number > 50 and self.number != 69 and self.number != 100:			
			self.window.clear_widgets()
			self.window.add_widget(self.home)
			self.home.text = "Restart"
			self.home.background_color = "FFFF33"
			self.window.add_widget(Image(source="socialpoints.jpeg",size_hint=(1, 600), allow_stretch=True, keep_ratio=False))

			self.sigmavalue=self.window.add_widget(Label(text=f"Il bro è al {self.number}% sigma!", size_hint=(1, 100), font_size= "20sp", bold=True))
			
		#True Sigma
		elif self.number == 100:
			SoundLoader.load("letsgoski.mp3").play()
			self.window.clear_widgets()
			self.gif=self.window.add_widget(Image(source="image.jpeg", size_hint = (0.3, 800), allow_stretch =True, keep_ratio=False))			
			
			self.window.add_widget(Label(text=f"Il bro è il VERO sigma({self.number}%)", size_hint=(1, 250), font_size = "20sp", bold=True))
			

									
			self.home.bind(on_press=self.HomeFunc)
			
			return self.window
			

			
	def HomeFunc(self, instance):	  	
	  self.window.clear_widgets()
	  self.window.add_widget(self.label_text)
	  self.window.add_widget(self.skibidi)
	  self.window.add_widget(self.godo)
	  
	  
	def  OpenWeb(istance, self):
	  url = ["https://it.m.wikipedia.org/wiki/Matrix", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9-Lz78HbbGr3aPTOmLt5gq3zVz4dRZC2fOw&usqp=CAU", "https://youtu.be/V71YZDHwGFY?si=khbxnQn6aM7cG7L4", "https://youtu.be/8tPhxQCJPjQ?si=-YdT5Xc5O0TdjF33"]
	  site = random.choice(url)
	  webbrowser.open(site)
	  
	  
	  

  
	  
		  	   				
SigmaApp().run()
	