import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
import time
from threading import Thread

kivy.config.Config.set ( 'input', 'mouse', 'mouse,disable_multitouch' )



    

class StopWatch(Widget):
    seconds = 0
    minuets = 0
    time_track = StringProperty("00:00")

    


    startBtntxt = "Start"
    stopBtntxt = "Stop"

    startBtn = ObjectProperty(None)
    stopBtn = ObjectProperty(None)
    timelbl = ObjectProperty(None)
    
    

    def update(self,dt):
        if(self.seconds < 10 and self.minuets < 10):
            self.time_track = "0" + str(self.minuets) + ":0" + str(self.seconds)
        elif(self.seconds >= 10 and self.minuets < 10):
            self.time_track = "0" + str(self.minuets) + ":" + str(self.seconds)
        elif(self.seconds >= 10 and self.minuets >= 10):
            self.time_track = str(self.minuets) + ":" + str(self.seconds)

        if(self.seconds == 60):

            self.minuets += 1
            self.seconds = 0
        
        self.timelbl.text = str(self.time_track)

        self.seconds+=1

    def start_time(self):
        print("START TIME!")
        
        

    def stopTime(self):
        print("STOP TIME!")

    

class StopWatchApp(App):     
    def build(self):
        watch = StopWatch()
        Clock.schedule_interval(watch.update, 1/1000)
        return watch

StopWatchApp().run()
