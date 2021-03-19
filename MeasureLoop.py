import datetime
from RTK import RTKStream
import os
import HackRF
from FileWriter import WriteToFile

class Measure:
    	
	def __init__(self):
		self.listToSend = []
		self.wtf = WriteToFile()
		self.rtk = RTKStream()
		self.on = True

	def startMeasure(self):
    
		while self.on:
    		
			lon, lat, alt = self.rtk.getPosition()
			RFLvl = HackRF.GetDataFromHackRF()
			time = str(datetime.datetime.now())
			print time, lon, lat, alt, RFLvl
			line = time, lon, lat, alt, RFLvl
			self.listToSend.append(line)
			


	def	stopMeasure(self):
    	
		self.on = False
		self.wtf.createFile(self.listToSend)
		





	
