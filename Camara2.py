import kivy
from kivy.uix.camera import Camera
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class MiCamara(App):
	
	def build (self):
		rl = RelativeLayout()
		cam = Camera(resolution=(640, 360), size=(1000, 600), pos=(0,0), play=True)
		rl.add_widget(cam)
		
		return rl
		
if __name__ == '__main__':
	MiCamara().run()
