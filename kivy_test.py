# https://kivy.org/doc/stable/guide/basic.html#quickstart explains what everything means
import kivy

from kivy.app import App
from kivy.uix.label import Label


class kivy_test(App):

    def build(self):
        return Label(text='Hello World')


kivy_test().run()