from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

# haha... ignore the 2 classes below...
class loginScreen(App):

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
        if len(username) != 0 & len(room) != 0 & len(hall) != 0:
            print(username, room, hall) #TODO transfer this data to alert screen
        self.username.text = ""
        self.room.text = ""
        self.res_hall.text = ""

class alertScreen(App):

    def build(self):
        main_layout = GridLayout(rows=3)

        button_layout = AnchorLayout(anchor_x='center',anchor_y='center')
        button = Button(text='Send Alert',size_hint=(.25,.15))
        button.bind(on_press=self.buttonClicked)
        button_layout.add_widget(button)

        text_layout = GridLayout(cols=2)
        text_layout.add_widget(Label(text='Alert Description'))
        self.alert = TextInput(multiline=True)
        text_layout.add_widget(self.alert)
        
        floor_layout = GridLayout(cols=5)
        button1 = ToggleButton(text="Basement", group="floors")
        button2 = ToggleButton(text="1st Floor", group="floors", state="down")
        button3 = ToggleButton(text="2nd Floor", group="floors")
        button4 = ToggleButton(text="3rd Floor", group="floors")
        button5 = ToggleButton(text="All Floors", group="floors")
        floor_layout.add_widget(button1)
        floor_layout.add_widget(button2)
        floor_layout.add_widget(button3)
        floor_layout.add_widget(button4)
        floor_layout.add_widget(button5)

        main_layout.add_widget(button_layout)
        main_layout.add_widget(text_layout)
        main_layout.add_widget(floor_layout)

        return main_layout

    def buttonClicked(self,btn):
        alert = self.alert.text
        if len(alert) != 0:
            print(alert)
        self.alert.text = ""

# kv file for screens
Builder.load_string("""
<LoginScreen>:
    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "coderev.png"
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'bottom'
            Button:
                text: 'Login'
                size_hint: (.25,.15)
                on_press: root.login(name.text, room.text, hall.text)
        GridLayout:
            cols: 2
            Label:
                text: 'Name'
                color: 80, 0, 0, 1
            TextInput:
                id: name
                multiline: False
            Label:
                text: 'Room #'
                color: 80, 0, 0, 1
            TextInput:
                id: room
                multiline: False
            Label:
                text: 'Residence Hall'
                color: 80, 0, 0, 1
            TextInput:
                id: hall
                multiline: False
            Label:
                text: ''
            Label:
                text: ''

<AlertScreen>:
    GridLayout:
        rows: 3
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "ruhrohshaggy.jpg"
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            Button:
                text: 'Send Alert'
                size_hint: (.25,.15)
                on_press: root.sendAlert(alert.text)
        GridLayout:
            cols: 2
            Label:
                text: 'Alert Description'
            TextInput:
                id: alert
                multiline: True
            Label:
                text: ''
            Label:
                text: ''
        GridLayout:
            cols: 5
            ToggleButton:
                text: 'Basement'
                group: 'floor'
            ToggleButton:
                text: '1st Floor'
                group: 'floor'
                state: 'down'
            ToggleButton:
                text: '2nd Floor'
                group: 'floor'
            ToggleButton:
                text: '3rd Floor'
                group: 'floor'
            ToggleButton:
                text: 'All Floors'
                group: 'floor'
""")

# login validation
BuildingDict = {
        "mosher":{"spider man": "066",
        "doctor strange": "123",
        "peter quill": "234",
        "iron man": "066",
        "incredible hulk": "456",
        "black widow": "090",
        "hawk eye": "270"
}
}

# Declare both screens
class LoginScreen(Screen):
    def login(self, name, room, hall):
        if len(name) != 0 and len(room) != 0 and len(hall) != 0:
            if hall in BuildingDict:
                if name in BuildingDict["mosher"]:
                    if room == BuildingDict["mosher"][name]:
                        sm.current = 'alert'
                    else:
                        print("Try again...")
            # print(name, room, hall)

class AlertScreen(Screen):
    def sendAlert(self, alert):
        if len(alert) != 0:
            print(alert) # TODO connect this with dropbox and replace print statement
            sm.current = 'login'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(AlertScreen(name='alert'))

class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()

#loginScreen().run()
#alertScreen().run()