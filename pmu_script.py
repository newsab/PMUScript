
# init vehicle
# 2 stall klocka
# Read Pos
# 2 angen frekvens
# Read RF level
# skriv i fil

from libhackrf import *
import math
from pylab import *     # for plotting
from scipy import signal
import numpy as np
import datetime
import serial
import RTK

global vehicle
global FileName
global SERIAL_PORT





def Measure():
	global FileName


	while True:
	
		#if keyboard.is_pressed('q'):
		#	break
		
		#print('Stoppa med q')
	
	
		#lat, lon, alt = GetDataFromPosition()
		
		
	
		#lat = str(59.3885) # DEMO
		#lon = str(15.9185) # DEMO
		#alt = str(5.00)    # DEMO
		
		lon, lat, alt = RTK.getPosition()

		time.sleep(0.2)
		
		RFLvl = GetDataFromHackRF()
		#RFLvl = -50.0 # DEMO
	
		f_print=(str(datetime.datetime.now()), lat, lon, alt, RFLvl)
			
		f = open(FileName, "at")		
		f.write(str(f_print))
		f.write("\n")
		f.close()
		
		with serial.Serial('/dev/ttyAMA0', baudrate=115200, timeout=1) as ser:
			print(str(ser))
			# read 10 lines from the serial output
   		# for i in range(10):
       # line = ser.readline().decode('ascii', errors='replace')
        
		
		
		print(f_print)
		
		#print(str(pos))
#def Init_Position():
    ##print(pos)
	#print "Wait to Connect"
	
	
	#position = str(pos)
	
	#vehicle = dronekit.connect('/dev/serial/by-id/usb-ArduPilot_CUAVv5_3A0031001351383135373935-if00',baud=57600)
	#vehicle = dronekit.connect('/dev/ttyUSB0')	
	#vehicle = dronekit.connect('/dev/ttyUSB0',baud=57600) # USB Remas Vid simulering !!!!
	#vehicle = dronekit.connect('/dev/ttyAMA0',baud=57600) # Remas Vid simulering !!!!
	#vehicle = dronekit.connect('/dev/ttyAMA0',baud=57600, wait_ready=True)
	
	#time.sleep(3)
	
	#print "Connected" 
	
#def GetDataFromPosition():
    #gpsStr = str(position.)
    #gpsStr = str(vehicle.location.global_relative_frame)
    
    #print gpsStr
#   position = gpsStr[15:].split(',')
    #print gpsData
   # lat = gpsData[0].split('=')[1]
   # lon = gpsData[1].split('=')[1]
   # alt = gpsData[2].split('=')[1]
    #print lat, lon, alt
   # return lat, lon, alt


def GetDataFromHackRF():
	
	samples = hackrf.read_samples(20000)
	
	x = samples.real # real del av samples i volt
	fs = int(10e6)
	N = 2000
	S=20000
	L=22000
	x=x[18000:20000]
	
	f, Pxx_den = signal.welch(x-mean(x), fs, 'blackmanharris', nperseg=400)
	#f, Pxx_den = signal.spectrogram(x-mean(x), fs, 'blackmanharris', nperseg=400)
	#f, Pxx_spec = signal.welch(x-mean(x), fs, 'flattop', 1024)
	
	f=hackrf_center_freq-f
	
	pxx=10*log10(Pxx_den)+30
	
	RFLvl=max(pxx)
	
	#time.sleep(1)
	
	#print 'Pxx_den dBm Max: %s' % str(max(pxx))
	
	return RFLvl


hackrf = HackRF()

hackrf.sample_rate = 10e6
hackrf_center_freq=228e6  #    FREKVENS
hackrf.center_freq = hackrf_center_freq

hackrf.lna_gain = 0
hackrf.vga_gain = 36
#hackrf.vga_gain = 26


FileName = str(datetime.datetime.now())

print(FileName)


f = open(FileName, "wt")
f.write('Drone Measurement, Frq: ' + str(hackrf_center_freq/1000000) + ' MHz')
f.write("\n")
f.write("\n")
f.write("\n")
f.write(FileName)
f.write("\n")
f.write("\n")
f.close()




Measure()