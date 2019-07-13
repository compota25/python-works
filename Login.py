import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

Builder.load_string(''' 
<CustomPopup1>:
	size_hint: .3, .3
	auto_dismiss: False
	title: 'Mensaje'
	Button:
		text: 'Bienvenido Al Sistema'.
		on_press: root.dismiss()
<CustomPopup2>:
	size_hint: .3, .3
	auto_dismiss: False
	title: 'Mensaje'
	Button:
		text: 'Credenciales incorrectos'
		on_press: root.dismiss()
<Login>:
	BoxLayout
		id: login_layout
		orientation: 'vertical'
		padding: [10, 50, 10, 50]
		spacing: 50
		Label:
			text: 'Acceso al sistema'
			font_size: 40
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: 'Usuario'
				font_size: 22
				halign: 'left'
				text_size: root.width-30, 30
			TextInput:
				id:usuario
				multiline: False
				font_size: 22
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: 'Password'
				halign: 'left'
				font_size: 22
				text_size: root.width-30, 30
			TextInput:
				id:password
				multiline: False
				password: True
				font_size: 22
		Button:
			text: 'Acceder'
			font_size: 22
			on_press: root.loguear(usuario.text, password.text)
''')

class CustomPopup1(Popup):
	pass
	
class CustomPopup2(Popup):
	pass
	
class Login(FloatLayout):
	
	def show_popup1 (self, b):
		p = CustomPopup1()
		p.open()

	def show_popup2 (self, b):
		p = CustomPopup2()
		p.open()

	def loguear (self, loginText, passwordText):
		app = App.get_running_app()
		app.username = loginText
		app.password = passwordText
		if(app.username=="demo" and app.password=="12345678"):
			p = CustomPopup1()
			p.open()
		else:
			p = CustomPopup2()
			p.open()

class MyApp(App):
	
	def build (self):
		return Login()
	
if __name__ == "__main__":
	MyApp().run()
	
		



