# App foundation
import kivy
kivy.require('2.2.1')
from kivy.config import Config
# Config.set('graphics', 'fullscreen', 1)

from kivy.app import App
import time
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget

# General Imports
import json

Builder.load_file('format.kv')

# Window size
Window.size = (800, 480)
# Window.fullscreen = True

act_totals = {
    "act1" : {"laps": []},
    "act2" : {"laps": []},
    "act3" : {"laps": []},
    "act4" : {"laps": []}
}

class MainDisplay(Widget):
    lap = {
        "lapnum" : 1,
        "lapact" : None,
        "start" : None,
        "stop" : None,
        "total" : None
    }

    event = ''

    def act(self, act):
        if self.lap['lapact'] != None:
            self.log_lap(self.lap['lapact'])
        self.lap.update({"start" : time.time()})
        self.lap.update({"lapact" : act})
        self.event = Clock.schedule_interval(self.timer, 1)

    def log_lap(self, act):
        self.event.cancel()
        self.lap.update({"stop" : time.time()})
        self.lap.update({"total" : self.lap["stop"] - self.lap["start"]})
        lap = {
            "lapnum" : self.lap['lapnum'],
            "lapact" : self.lap['lapact'],
            "start" : self.lap['start'],
            "stop" : self.lap['stop'],
            "total" : self.lap['total']
        }
        act_totals[f'act{self.lap["lapact"]}']["laps"].append(lap)
        self.lap.update({"lapnum" : self.lap["lapnum"] + 1,
                         "lapact" : None,
                         "start" : None,
                         "stop" : None,
                         "total" : None})
        print(self.lap["lapact"], lap)
        print(self.lap)
        return

    def timer(self, *args):
        if getattr(self.ids, "but" + self.lap["lapact"]).state == 'down':
            self.lap.update({"total" : time.time() - self.lap["start"]})
            getattr(self.ids, "act" + self.lap["lapact"]).text = str(self.convert_time(self.lap["total"]))

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
        return MainDisplay()
    
if __name__ == '__main__':
    MyApp().run()