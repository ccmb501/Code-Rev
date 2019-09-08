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
from dropbox_file_util import Tracker, Alert_Sender
import alert_json
import time
from plyer import notification
import json
import threading

# ======================================== DEBUG STUFF =============================================
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
# ==================================================================================================

# kv file for screens
Builder.load_string("""
<LoginScreen>:
    on_leave:
        name.text = ''
        room.text = ''
        hall.text = ''
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
    on_leave: alert.text = ''
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

# login validation (in the future, this would be populated by the names, rooms, and halls of all students)
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
    n = ""
    r = ""
    h = ""
    def login(self, name, room, hall):
        if len(name) != 0 and len(room) != 0 and len(hall) != 0:
            if hall in BuildingDict:
                if name in BuildingDict["mosher"]:
                    if room == BuildingDict["mosher"][name]:
                        n = name
                        r = room
                        h = hall
                        sm.current = 'alert'
                    else:
                        print("Try again...")
            # print(name, room, hall); TODO these values need to be carried over

class AlertScreen(Screen):
    send_period = 10
    def sendAlert(self, alert):
        if len(alert) != 0:
            os = Alert_Sender()
            alert_time = alert_json.current_time()
            alert = alert_json.format_alert(0, LoginScreen.r, alert, LoginScreen.n, alert_time)
            os.send_alert(alert, alert_time, LoginScreen.n)
            sm.current = 'login'

# check for alerts
def alert_tracker():
    iter = 0
    while True:
        iter += 1
        print('Tracking Alerts #' + str(iter) + ":\n")
        tracker = Tracker()
        #Check x times
        checks = 30
        update_period = 1
        for i in range(0, checks):
            #print('Polling')
            is_alert = tracker.poll()
            if(is_alert):
                alert = tracker.pull_last_file()
                print('There is an alert: ', alert) #create notification
                send_notification(alert)
            time.sleep(update_period)

# create notifications
def send_notification(alert: str):
    data = json.loads(alert)
    notification.notify(title='Code Rev : Room '+ data[1], message=data[2] + '- '+data[3], app_name='coderev',timeout=20)

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(AlertScreen(name='alert'))

# main class
class MainApp(App):
    def build(self):
        return sm

# run file
if __name__ == '__main__':
    #MainApp().run()
    main = MainApp()
    a = threading.Thread(target=main.run, name="one")
    b = threading.Thread(target=alert_tracker, name="two")

    a.start()
    #b.start()
    

#loginScreen().run()
#alertScreen().run()