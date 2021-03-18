import pynmea2
import serial
import datetime


def getLon():
    ser = serial.Serial('/dev/ttyAMA0', 115200)
    
    while 1:
        rawData = ser.readline()
        try:
            msg = pynmea2.parse(rawData)           
            lo = pynmea2.dm_to_sd(msg.lon)
            lon = "{:.9f}".format(lo)
            print lon
            la = pynmea2.dm_to_sd(msg.lat)
            lat = "{:.9f}".format(la)
            print lat
            alt = msg.altitude         
            print alt
            print rawData
        except:
           pass
        

getLon()

