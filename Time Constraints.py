from time import sleep
import threading

class myThread(threading.Thread):
    def __init__(self, time):
        threading.Thread.__init__(self)
        self.time = time
    
    def run(self):
        sleep(self.time)
        print("Kablam!!")
        
hohoho = myThread(5)
hohoho.start()