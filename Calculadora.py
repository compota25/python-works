from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_string(''' 
<CustButton@Button>:
	font_size: 25
	color: 1, 1, 1, 1
<Demo1>:
	numero1: numero1
	numero2: numero2
	resultado: resultado
	cols: 1
	BoxLayout:
		orientation: 'vertical'
		Label:
			id: 11
			text: 'Calculadora Basica'
			font_size: 25
		TextInput:
			id: numero1
			mutiline: False
			font_size: 25
			text: '20'
		TextInput:
			id: numero2
			mutiline: False
			font_size: 25
			text: '10'
		Label:
			id: resultado
			font_size: 25
	BoxLayout:
		spacing: 6
		CustButton:
			size_hint_x: 0.4
			pos_hint: {'x': 0}
			text: '+'
			on_press: root.sumando(*args)
		CustButton:
			size_hint_x:0.4
			pos_hint: {'y': 0}
			text: '-'
			on_press: root.restando(*args)
	BoxLayout:
		spacing: 6
		CustButton:
			size_hint_x:0.4
			pos_hint: {'x':0}
			text: '*'
			on_press: root.multiplicando(*args)
		CustButton:
			size_hint_x: 0.4
			pos_hint: {'y': 0}
			text: '/'
			on_press: root.dividiendo(*args)
''')

class Demo1(GridLayout):
	def sumando (self, instance):
		self.resultado.text = str(int(self.numero1.text) + int(self.numero2.text))
		
	def restando (self, instance):
		self.resultado.text = str(int(self.numero1.text) - int(self.numero2.text))
		
	def multiplicando (self, instance):
		self.resultado.text = str(int(self.numero1.text) * int(self.numero2.text))
	
	def dividiendo (self, instance):
		try:
			self.resutado.text = str(int(numero1.text) / int(self.numero2.text))
		except ZeroDivisionError:
			self.resultado.text = 'division entre zero'
	
	def reset (self, instance):
		self.numero1.text = ""
		self.numero2.text = ""
		self.resultado.text = ""
		
class DemoApp(App):
	def build (self):
		return Demo1()

if __name__ == '__main__':
	DemoApp().run()
		
		
		
		
		
