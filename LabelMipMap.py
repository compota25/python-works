import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.label import Label

class LabelMipmapTest(App):
	def build (self):
		""" Function doc """
		s = ScatterPlane(scale=.5)
		l1 = Label(text='Python', font_size=200, pos=(750, 500), mipmap=True)
		l2 = Label(text='kivy', font_size=200, pos=(750,728))
		s.add_widget(l1)
		s.add_widget(l2)
		return s
		
if __name__ == '__main__':
	LabelMipmapTest().run()
	
