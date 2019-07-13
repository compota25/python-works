from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
	
	def __init__ (self, **kwargs):
		""" Function doc """
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='Nombre de usuario'))
		self.usuario = TextInput(multiline=False)
		self.add_widget(self.usuario)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

class MyApp(App):
	
	def build (self):
		""" Function doc """
		return LoginScreen()

if __name__ == '__main__':
	MyApp().run()
		
