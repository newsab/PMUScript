from libhackrf import *
import math
from pylab import *     # for plotting
from scipy import signal
import numpy as np

class PMUHackRF:
    	
	def __init__(self, frequency):
		self.fredag = (float(frequency)*1000000.0)
		self.hackrf = HackRF()
		self.hackrf.sample_rate = 10e6	
		self.hackrf_center_freq= self.fredag  #    FREKVENS
		self.hackrf.center_freq = self.hackrf_center_freq
		self.hackrf.lna_gain = 0
		self.hackrf.vga_gain = 36	

	def GetDataFromHackRF(self):
		samples = self.hackrf.read_samples(20000)		
		x = samples.real # real del av samples i volt
		fs = int(10e6)
		N = 2000
		S=20000
		L=22000
		x=x[18000:20000]
		f, Pxx_den = signal.welch(x-mean(x), fs, 'blackmanharris', nperseg=400)
		f=self.hackrf_center_freq-f	
		pxx=10*log10(Pxx_den)+30
		RFLvl=max(pxx)
			
		
		return RFLvl

	def killHackRF(self):
		self.hackrf.__del__()

	
