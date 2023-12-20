# App foundation
import kivy
kivy.require('2.2.1')
from kivy.config import Config
# Config.set('graphics', 'fullscreen', 1)

from kivy.app import App
# from kivymd.app import MDApp
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
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('format.kv')

# Window size
Window.size = (800, 480)
# Window.fullscreen = True


class MainDisplay(Widget):
    start = ''
    tot = float(0)
    elapsed = ''
    event = ''

    def change_gif(self, file, color):
        self.ids.gif.source = file
        self.ids.clock_time.color = color

    def act1(self):
        if self.ids.act1.state == 'down':
            self.start = time.time()
            print(f'Down {self.convert_time(self.start)}')
            self.event = Clock.schedule_interval(self.timer1, 1)
        elif self.ids.act1.state == 'normal':
            self.event.cancel()
            self.tot = self.tot + self.elapsed
            print(self.tot)
            self.elapsed = float(0)
    
    def stop1(self):
        self.ids.act1.state = 'normal'

    def timer1(self, *args):
        if self.ids.act1.state == 'normal':
            print('up')
            self.event.cancel()
            self.tot = self.tot + self.elapsed
            print(self.tot)
            self.elapsed = float(0)
        else:
            self.elapsed = time.time() - self.start
            print(self.tot, self.elapsed)
            # self.tot += self.elapsed
            self.ids.act1.text = str(self.convert_time(self.tot + self.elapsed))

    def convert_time(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        string_time = f'{int(hours)}:{int(mins)}:{int(sec)}'
        return string_time
        


class MyApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        structtime_obtain = time.localtime()
        strftime_output = time.strftime("%I:%M:%S %p", structtime_obtain)
        self.root.ids.clock_time.text = strftime_output

    def build(self):
        # return LoginScreen()
        return MainDisplay()
    
if __name__ == '__main__':
    MyApp().run()