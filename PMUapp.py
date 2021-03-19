import Pyro4
import pynmea2
import serial
import datetime
from MeasureLoop import Measure
import threading

@Pyro4.expose
class PmuApp:
    
    def __init__ (self):
        self.measure = Measure()
        self.quitflag = False
        self.quitlock = threading.Lock()

        

    def startMeasure(self):
        while True:
            with self.quitlock:
                if self.quitflag:
                    return
            self.measure.startMeasure()
            

    def stopMeasure(self):
        with self.quitlock:
            self.quitflag = True
        self.t.join()
        print "HEEEEJ!!!!!!!"
        self.measure.stopMeasure()


    t = threading.Thread(target=startMeasure)
    t.start()    

Pyro4.Daemon.serveSimple(
    {
        PmuApp: "PMUApp"
         
    },
    ns=True, verbose=True, host="172.16.0.3") 


    	
