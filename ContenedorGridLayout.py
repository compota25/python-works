from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_string(''' 
<Grid>:
	cols:3
	rows:3
	Button:
		font_size: 40
		text: 'Uno'
	Button:
		font_size: 40
		text: 'Dos'
	Button:
		font_size: 40
		text: 'Tres'
	Button:
		font_size: 40
		text: 'Cuatro'
	Button:
		font_size: 40
		text: 'Cinco'
	Button:
		font_size: 40
		text: 'Seis'
''')

class Grid(GridLayout):
	pass

class DemoApp(App):
	
	def build (self):
		""" Function doc """
		return Grid()
	
if __name__ == '__main__':
	DemoApp().run()
