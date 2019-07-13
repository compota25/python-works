import kivy
#indicamos la version de kivy
kivy.require('1.10.0')
#importamos la calse base desde app
from kivy.app import App
#el uix.button es la seccion que contiene elementos de la UI
from kivy.uix.button import Label

class MiAplicacion(App):

	def build(self):
		return Label(text='Hola Mundo')
		
if __name__ == "__main__":
	MiAplicacion().run()
