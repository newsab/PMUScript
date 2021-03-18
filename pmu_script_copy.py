from libhackrf import *
import math
from pylab import *     # for plotting
from scipy import signal
import numpy as np
import datetime
from serial import Serial
import RTK
import os
import json
import test4

global FileName
global fullPath

def Measure():
	global FileName
	global fullPath
	
	while True:
    		
		#lon= RTK.getLon()
		#lat = RTK.getLat()
		#alt = RTK.getAlt()
		lon, lat, alt, alt2 = test4.getPosition()
		RFLvl = GetDataFromHackRF()	
		f_print=(str(datetime.datetime.now()), lat, lon, alt, alt2, RFLvl)
		#time.sleep(0.2)
		
		#f = open(FileName, "at")		
		f = open(fullPath, "at")
		f.write(str(f_print))
		f.write("\n")
		f.close()
        		
		print(f_print)		

def GetDataFromHackRF():
	
	samples = hackrf.read_samples(20000)	
	
	x = samples.real # real del av samples i volt
	fs = int(10e6)
	N = 2000
	S=20000
	L=22000
	x=x[18000:20000]
	f, Pxx_den = signal.welch(x-mean(x), fs, 'blackmanharris', nperseg=400)
	f=hackrf_center_freq-f	
	pxx=10*log10(Pxx_den)+30
	RFLvl=max(pxx)	
	
	return RFLvl

hackrf = HackRF()

hackrf.sample_rate = 10e6
hackrf_center_freq=228e6  #    FREKVENS
hackrf.center_freq = hackrf_center_freq
hackrf.lna_gain = 0
hackrf.vga_gain = 36

FileName = str(datetime.datetime.now())

#print(FileName)
#f = open(FileName, "wt")

path = "/home/pi/pmuScript/Measurement/"
fullPath = os.path.join(path, FileName)
f = open(fullPath, "wt")

f.write('Drone Measurement, Frq: ' + str(hackrf_center_freq/1000000) + ' MHz')
f.write("\n \n \n")
#f.write(FileName)
f.write(fullPath)
f.write("\n \n")
f.close()

Measure()