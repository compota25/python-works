from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Test(BoxLayout):
                              	
	def llenar (self):
		self.rv.data = [{'value' : ''.join(sample(ascii_lowercase, 6) )} for x in range(10)]
	
	def ordenar (self):
		self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])
	
	def limpiar(self):
		self.rv.data = []

	def insertar (self, value):
		self.rv.data.insert(0, {'value': value or 'default value'})
	
	def actualizar(self, value):
		if self.rv.data:
			self.rv.data[0]['value'] = value or 'default new value'
			self.rv.refresh_from_data()
	
	def remover(self):
		if self.rv.data:
			self.rv.data.pop(0)
	
class recycleview1(App):
	def build(self):
		return Test()

if __name__ == "__main__":
	recycleview1().run()