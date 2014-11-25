import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty

kivy.config.Config.set ( 'input', 'mouse', 'mouse,disable_multitouch' )

#contains the whole interface
class StopWatch(Widget):

    #gloabl variables
    seconds = 0
    minuets = 0
    time_track = StringProperty("00:00")
    running = False
    resetting = True
    timelbl = ObjectProperty(None)    

    def update(self,dt):
        self.timelbl.text = str(self.time_track)
        if(self.running):

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

        if(self.resetting == True):
            self.minuets = 0
            self.seconds = 0
            self.time_track = str(self.minuets) + "0:0" + str(self.seconds)
            self.resetting = False
            self.running = False

    #Starts the timer
    def start_time(self):
        print("START TIME!")
        self.running = True
        
    #Stops the timer
    def stopTime(self):
        print("STOP TIME!")
        self.running = False

    #Reset the timer
    def resetTime(self):
        print("RESET TIME!")
        self.running = False
        self.resetting = True

class StopWatchApp(App):     
    def build(self):
        watch = StopWatch()
        Clock.schedule_interval(watch.update, 1)
        return watch

StopWatchApp().run()
