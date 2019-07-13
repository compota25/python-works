from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(''' 
<caja>:
	StackLayout:
		spacing: 5
		padding: 5
		orientation: 'tb-rl'
		Button:
			text: "boton1"
			size_hint: 0.15, 0.15
		Button:
			text: "boton2"
			size_hint: 0.25, 0.25
		Button:
			text: "boton3"
			size_hint: 0.35, 0.35
''')

class Caja(BoxLayout):
	pass
	
class DemoApp(App):
	
	def build (self):
		""" Function doc """
		return Caja()

if __name__ == "__main__":
	DemoApp().run()
