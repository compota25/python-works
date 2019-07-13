import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label

texto_largo = (""" En 1991, van Rossum publicó el código de la versión 0.9.0 en alt.sources.8​ En esta etapa del desarrollo ya estaban presentes clases con herencia, manejo de excepciones, funciones y los tipos modulares, como:  str, list, dict, entre otros. Además en este lanzamiento inicial aparecía un sistema de módulos adoptado de Modula-3;  van Rossum describe el módulo como “una de las mayores unidades de programación de Python”. """)

class LabelTextSizeTest(App):
	def build (self):
		""" Function doc """
		z = Label(
			text = texto_largo,
			text_size = (600, None),
			line_height = 2.5
		)
		return z
		
if __name__ == "__main__":
	LabelTextSizeTest().run()
