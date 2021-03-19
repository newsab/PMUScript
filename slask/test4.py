import pynmea2
import serial

def getPosition():
  stream = serial.Serial('/dev/ttyAMA0', 115200)

  for sentence in stream:
    try:
      pNMEA = pynmea2.parse(sentence)

      if isinstance(pNMEA, pynmea2.types.talker.GGA):       
        lo = pynmea2.dm_to_sd(pNMEA.lon)
        lon = "{:.9f}".format(lo)  

        la = pynmea2.dm_to_sd(pNMEA.lat)
        lat = "{:.9f}".format(la)  

        alt = pNMEA.altitude
        alt2 = pNMEA.altitude_units

        return lon, lat, alt, alt2

      #if isinstance(pNMEA, pynmea2.types.talker.GSA):
          #print "GSA"
          #print '\tMode:', pNMEA.mode
          #print '\tMode fix type:', pNMEA.mode_fix_type  
  
    except:
      pass

