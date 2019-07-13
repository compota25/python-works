from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_string(''' 
<Caja>:
	anchor_x: 'right'
	anchor_y: 'bottom'
	Button:
		id: label1
		size_hint: 1, 1
		text: 'Boton1'
	Button:
		id: label2
		size_hint: 0.6, 0.6
		text: 'Boton2'
	Button:
		id: label3
		size_hint: 0.3, 0.3
		text: 'Boton3'
	Button:
		id: label4
		size_hint: 0.1, 0.1
		text: 'Boton4'
		
''')




class Caja(AnchorLayout):
	pass
	
class DemoApp(App):
	
	def build (self):
		""" Function doc """
		return Caja()
		
if __name__ == '__main__':
	DemoApp().run()
	
	
