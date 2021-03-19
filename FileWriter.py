import os
import HackRF
import datetime

class WriteToFile:

    def __init__(self):
        self.fileName = str(datetime.datetime.now())
        self.path = "/home/pi/pmuScript/Measurement/"
        self.fullPath = os.path.join(self.path, self.fileName)       
      
        
    def createFile(self, listToRead):
        listToLoop = listToRead
        f = open(self.fullPath, "wt")
        f.write('Drone Measurement, Frq: ' + str(HackRF.getFrequency()/1000000) + ' MHz')
        f.write("\n \n \n")
        f.write(self.fullPath)
        f.write("\n \n")
        f.close()
        
        for line in listToLoop:
            #f_print=(str(datetime.datetime.now()), lat, lon, alt, RFLvl)
            f = open(self.fullPath, "at")
            f.write(str(line))
            f.write("\n")
            f.close()
