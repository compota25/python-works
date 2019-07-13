from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(''' 
<caja>:
	orientation: 'vertical'
	padding: 20
	BoxLayout:
		Button:
			text: "Primera fila, Primera Columna"
			bold: True
		Button:
			text: "Primera fila, Segunda Columna"
			color: [1, 0, 0, 1]
			bold: True
	BoxLayout:
		Button:
			text: "Segunda Fila, Primera Columna"
			color: [0, 0, 1, 1]
			bold: True
		Button:
			text: "Segunda Fila, Segunda Columna"
			color: [1, 1, 0, 1]
			bold: True
''')

class Caja(BoxLayout):
	pass

class DemoApp(App):
	
	def build(self):
		return Caja()
		
if __name__ == "__main__":
	DemoApp().run()	
