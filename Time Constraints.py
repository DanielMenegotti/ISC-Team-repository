from time import sleep
import threading

class myThread(threading.Thread):
    def __init__(self, speed):
        threading.Thread.__init__(self)
        self.time = speed
    
    def run(self):
        sleep(self.time)
        
        
#Add to   = myThread(speed)
hohoho.start()