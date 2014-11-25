import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
import time


kivy.config.Config.set ( 'input', 'mouse', 'mouse,disable_multitouch' )

class StopWatch(Widget):
    startBtntxt = "Start"
    stopBtntxt = "Stop"

    startBtn = ObjectProperty(None)
    stopBtn = ObjectProperty(None)
    timelbl = ObjectProperty(None)

    seconds = 0
    minuets = 0

    time = StringProperty("")

    if(seconds < 10 and minuets < 10):
        time = str(minuets) + "0:0" + str(seconds) 

    
    
    def startTime(self):
        print("TIME STARTED!")
        start = time.time()
        time.clock()    
        elapsed = 0
        while elapsed >= 0:
            elapsed = time.time() - start
            print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)
            if elapsed < 60:
                self.seconds +=1
            else:
                self.minuets+= 1
                self.seconds = 0
            self.timelbl.text =self.time
            time.sleep(1)  

            
    def stopTime(self):
        print("TIME STOPED!")


class StopWatchApp(App):
    
        
    def build(self):
        watch = StopWatch()
       
        return watch

StopWatchApp().run()