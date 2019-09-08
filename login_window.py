import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class login(App):

    def build(self):
        main_layout = FloatLayout()

        button_layout = AnchorLayout(anchor_x='center',anchor_y='bottom')
        button = Button(text='Login',size_hint=(.25,.15))
        button.bind(on_press=self.buttonClicked)
        button_layout.add_widget(button)

        text_layout = GridLayout(cols=2)
        text_layout.add_widget(Label(text='Name'))
        self.username = TextInput(multiline=False)
        text_layout.add_widget(self.username)
        text_layout.add_widget(Label(text='Room #'))
        self.room = TextInput(multiline=False)
        text_layout.add_widget(self.room)
        text_layout.add_widget(Label(text='Residence Hall'))
        self.res_hall = TextInput(multiline=False)
        text_layout.add_widget(self.res_hall)
        text_layout.add_widget(Label(text=''))
        text_layout.add_widget(Label(text=''))

        main_layout.add_widget(button_layout)
        main_layout.add_widget(text_layout)

        return main_layout

    def buttonClicked(self,btn):
        username = self.username.text
        room = self.room.text
        hall = self.res_hall.text
        print(username, room, hall)
        self.username.text = ""
        self.room.text = ""
        self.res_hall.text = ""

login().run()