import Pyro4
import pynmea2
import serial
import datetime

@Pyro4.expose
class Rtk:
    
    def __init__ (self):
        self.raspiGNNS = serial.Serial('/dev/ttyAMA0', 115200)

    def getPosition(self):
        #stream = raspiGNNS

        for sentence in self.raspiGNNS:
            try:
                pNMEA = pynmea2.parse(sentence)

                if isinstance(pNMEA, pynmea2.types.talker.GGA):       
                    lo = pynmea2.dm_to_sd(pNMEA.lon)
                    lon = "{:.9f}".format(lo)  

                    la = pynmea2.dm_to_sd(pNMEA.lat)
                    lat = "{:.9f}".format(la)  

                    alt = pNMEA.altitude
                    

                    return lon, lat, alt
            except:
                pass


Pyro4.Daemon.serveSimple(
    {
        Rtk: "myrtk"
    },
    ns=True, verbose=True, host="172.16.0.3") 