from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.app import App
import kivy
kivy.require('2.0.0')  # replace with your current kivy version !


class AppWidget(Widget):
    def build(self):
        pass


class HelloWorldApp(App):
    def build(self):
        return AppWidget()


if __name__ == '__main__':
    HelloWorldApp().run()
