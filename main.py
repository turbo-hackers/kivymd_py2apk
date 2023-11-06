from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton

class TestApp(MDApp):

	def build(self):
		global name,l
		screen = Screen()
		
		# defining Text field with all the parameters
		name = MDTextField(text="Enter name",
					pos_hint={'center_x': 0.4, 'center_y': 0.5},
					size_hint_x=None, width=100)

		# defining label with all the parameters
		l = MDLabel(text="HI !",halign="center",
					pos_hint={'center_y': 0.8},
					theme_text_color="Custom",
					text_color=(0.5, 0, 0.5, 1),
					font_style='Subtitle1')

		# defining Button with all the parameters
		btn = MDRectangleFlatButton(text="Submit",
					size_hint_x=None,
					pos_hint={'center_x': 0.55, 'center_y': 0.5},
					on_release=self.btnfunc)
		# adding widgets to screen
		screen.add_widget(name)
		screen.add_widget(btn)
		screen.add_widget(l)
		# returning the screen
		return screen

	def btnfunc(self, obj):
		if name.text != "Enter name":
			l.text = ("HI "+name.text.upper()+" !")
		else:
			l.text = ("HI !")

if __name__ == "__main__":
	TestApp().run()
