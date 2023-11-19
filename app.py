# App foundation
import kivy
kivy.require('2.2.1')
from kivy.config import Config
# Config.set('graphics', 'fullscreen', 1)

# from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRoundFlatIconButton
import time
# Widget elements
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('format.kv')

# Window size
# Window.size = (800, 480)
Window.fullscreen = True


class MainDisplay(Widget):
    def change_gif(self, file, color):
        self.ids.gif.source = file
        self.ids.clock_time.color = color

    def act1(self):
        Clock.schedule_interval(self.timer1, 0.1)

    def timer1(self, *args):
        start = time.time()
        elapsed = time.time() - start
        print(elapsed)
        self.ids.act1.text = str(elapsed)
        


class MyApp(MDApp):
    def on_start(self):
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        structtime_obtain = time.localtime()
        strftime_output = time.strftime("%I:%M %p", structtime_obtain)
        self.root.ids.clock_time.text = strftime_output

    def build(self):
        # return LoginScreen()
        return MainDisplay()
    
if __name__ == '__main__':
    MyApp().run()