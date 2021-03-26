import serial
import datetime
import threading
import Pyro4
from RTK import RTKStream
import os
import HackRF
from FileWriter import WriteToFile

@Pyro4.expose
class PmuApp:
    
    def __init__ (self):
        self.rtk = RTKStream()
        self.wtf = WriteToFile()
        self.quitlock = threading.Lock()
        self.t = threading.Thread(target=self.measure)
        self.listToSend = []
        self.quitflag = False
		
    def measure(self):
        print"Ok jag kor"
        while True:
            with self.quitlock:
                if self.quitflag:
                    print"I'm done!"
                    return
            lon, lat, alt = self.rtk.getPosition()
            RFLvl = HackRF.GetDataFromHackRF()
            time = str(datetime.datetime.now())
            print time, lon, lat, alt, RFLvl
            line = time, lon, lat, alt, RFLvl
            self.listToSend.append(line)

            
        
            
    def starta(self):
        print"hej"
        self.quitflag = False
        if self.t.is_alive():
            self.measure()
            
        else:
            self.t.start()
            


    def stopMeasure(self):
        with self.quitlock:
            self.quitflag = True
        self.t.join()
        print "HEEEEJ!!!!!!! Nu javlar funkar det fint! "
        self.wtf.createFile(self.listToSend)
        print "sucess"
        return self.listToSend
        
        #self.t._stop()

    
        
   

    
      

Pyro4.Daemon.serveSimple(
    {
        PmuApp: "PMUApp"
         
    },
    ns=True, verbose=True, host="172.16.0.3") 


    	
