#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from astropy.convolution import convolve, Box1DKernel
from astLib import astSED

# converting APASS mag into fluxes
filters   = ['APASS_B', 'APASS_V', 'APASS_g', 'APASS_r', 'APASS_i']

for i, filter in enumerate(filters):
   wnew, tnew = np.loadtxt(filter+'.dat',  unpack=True, dtype=None)
   wold, told = np.loadtxt('APASS.old/'+filter+'.dat',  unpack=True, dtype=None)
   plt.plot(wnew, tnew, ls='dashed', label=filter+'svo')
   plt.plot(wold, told, ls='dotted', label=filter+'old')
plt.legend()
plt.show()

