from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time

class Camara(BoxLayout):
	def capture (self):
		camera = self.ids['camera']
		file_name = 'capturado' + time.strftime("%Y%m%d_%H%M%S")
		camara.export_to_png(file_name + ".png")

class Plantilla(App):

	def build(self):
		return Camara()

class Conexion():
	def __init__ (self):
		

if __name__ == "__main__":
	Plantilla().run()
