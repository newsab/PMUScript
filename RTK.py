import pynmea2
import serial

class RTKStream:

    def __init__(self):
        self.raspiGNNS = serial.Serial('/dev/ttyAMA0', 115200)

    def getPosition(self):
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
        