import serial
import datetime
import threading
import Pyro4
from RTK import RTKStream
import os
from HackRF import PMUHackRF
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
        self.frequency = 0.0
        
		
    def measure(self):
        global HackData 
        HackData =  PMUHackRF(self.frequency) 
        print"Ok jag kor"
        while True:
            with self.quitlock:
                if self.quitflag:
                    print"I'm done!"
                    return
            lon, lat, alt = self.rtk.getPosition()
            RFLvl = HackData.GetDataFromHackRF()
            time = str(datetime.datetime.now())
            print time, lon, lat, alt, RFLvl
            line = time, lon, lat, alt, RFLvl
            self.listToSend.append(line)
            
            
        
            
    def starta(self, frequency):
        self.frequency = frequency
        print"hej"
        self.quitflag = False
        if self.t.is_alive():
           return self.measure(fre)
            
        else:
            self.t.start()
            


    def stopMeasure(self):
        with self.quitlock:
            self.quitflag = True
        self.t.join()
        print "HEEEEJ!!!!!!! Nu javlar funkar det fint! "
        self.wtf.createFile(self.listToSend, self.frequency)
        print "sucess"
        HackData.killHackRF()
        return self.listToSend

        
        #self.t._stop()

    def getStartPosition(self):
        print"Vart ar jag?"      
        lon, lat, alt = self.rtk.getPosition()
        time = str(datetime.datetime.now())
        startposition = time, lon, lat, alt
        print"Nu vet jag vart jag ar" + time, lon, lat, alt
        return startposition
    
    def getListToSend(self):
        return self.listToSend
   

    
      

Pyro4.Daemon.serveSimple(
    {
        PmuApp: "PMUApp"
         
    },
    ns=True, verbose=True, host="172.16.0.3") 


    	
