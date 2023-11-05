# App foundation
import kivy
kivy.require('2.2.1')
from kivy.app import App
import time
# Widget elements
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('format.kv')

# Window size
Window.size = (800, 480)



    
# class myclock(Label):
#     def update(self, *args):
#         structtime_obtain = time.localtime()
#         strftime_output = time.strftime("%H:%M:%S", structtime_obtain)
#         self.text = strftime_output

# class TimeDisplay(GridLayout):
#     def __init__(self, **kwargs):
#         super(TimeDisplay, self).__init__(**kwargs)
#         self.cols = 2
#         self.clock1 = myclock()
#         Clock.schedule_interval(self.clock1.update, 1)
#         self.add_widget(self.clock1)

# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)
#         self.clock1 = myclock()
#         Clock.schedule_interval(self.clock1.update, 1)
#         self.add_widget(self.clock1)

class MainDisplay(Widget):
    pass
    # time = TimeDisplay()
    # def clock(self):
    #     structtime_obtain = time.localtime()
    #     strftime_output = time.strftime("%H:%M:%S", structtime_obtain)
    #     self.ids.clock_time.text = strftime_output
    #     self.call_time()

    # def call_time(self):
    #     Clock.schedule_interval(self.clock(), 1)

class MyApp(App):
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