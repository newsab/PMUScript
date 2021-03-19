from libhackrf import *
import math
from pylab import *     # for plotting
from scipy import signal
import numpy as np

hackrf = HackRF()

hackrf.sample_rate = 10e6
hackrf_center_freq=228e6  #    FREKVENS
hackrf.center_freq = hackrf_center_freq
hackrf.lna_gain = 0
hackrf.vga_gain = 36

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

def getFrequency():
    return hackrf_center_freq
