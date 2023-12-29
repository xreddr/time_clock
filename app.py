# App foundation
import kivy
kivy.require('2.2.1')
from kivy.config import Config
# Config.set('graphics', 'fullscreen', 1)
from kivy.app import App

# Additional kivy imports
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Data Viz imports
import matplotlib.pyplot as plt 
import numpy as np

# General Imports
import time
from datetime import date, datetime, timedelta, time as dtime
import json

Builder.load_file('format.kv')

# Window size
Window.size = (800, 480)
# Window.fullscreen = True

act_totals = {
    "act1" : {"laps": [],
              "total": float(0)},
    "act2" : {"laps": [],
              "total": float(0)},
    "act3" : {"laps": [],
              "total": float(0)},
    "act4" : {"laps": [],
              "total": float(0)}
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
        if getattr(self.ids, 'but' + act).state == 'normal':
            pass
        else:
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
        tot = float(0)
        for lap in act_totals[f'act{self.lap["lapact"]}']['laps']:
            tot += float(lap['total'])
            print(tot)
            print(lap['total'])
            act_totals[f'act{self.lap["lapact"]}'].update({"total" : tot})
        # self.ids.pie.source = "fig.png"
        print(act_totals[f'act{self.lap["lapact"]}']['total'])
        self.lap.update({"lapnum" : self.lap["lapnum"] + 1,
                         "lapact" : None,
                         "start" : None,
                         "stop" : None,
                         "total" : None})
        return

    def timer(self, *args):
        if getattr(self.ids, "but" + self.lap["lapact"]).state == 'down':
            self.lap.update({"total" : time.time() - self.lap["start"]})
            getattr(self.ids, "act" + self.lap["lapact"]).text = str(self.convert_time(float(act_totals[f'act{self.lap["lapact"]}']["total"]) + self.lap["total"]))

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
        Clock.schedule_interval(self.update_pie, 1)

    def update_clock(self, *args):
        structtime_obtain = time.localtime()
        strftime_output = time.strftime("%I:%M:%S %p", structtime_obtain)
        self.root.ids.clock_time.text = strftime_output
        # self.update_pie()

    def update_pie(self, *args):
        today = date.today()
        time_pass = time.time() - time.mktime(today.timetuple())

        now = datetime.now()
        midnight = datetime.combine(now + timedelta(days=1), dtime())
        time_left = (midnight - now).seconds

        y = np.array([time_left, time_pass])
        mylabels = [f'{time_left}', f'{time_pass}']
        print(mylabels)
        plt.pie(y, startangle=90, labels=mylabels)
        plt.savefig("fig.png", transparent=True)
        plt.show()
        self.root.ids.pie.source = "fig.png"


    def build(self):
        return MainDisplay()
    
if __name__ == '__main__':
    MyApp().run()