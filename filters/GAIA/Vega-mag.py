#/usr/bin/env python
from astLib import astSED
import numpy as np
import matplotlib.pyplot as plt
c =2.99792458 
from WDmodels  import photometry

info = {'gaiaDR2_g'  : 13.0385,
        'gaiaDR2_b'  : 12.9688,
        'gaiaDR2_r'  : 13.1308,
        'egaiaDR2_g' : 0.0005,
        'egaiaDR2_b' : 0.0023,
        'egaiaDR2_r' : 0.0012}

sed = astSED.AB
#sed = astSED.VEGA
path = '/home/astro/phrnbk/python_modules/WDmodels/filters/'
gaia = ['gaiaDR2_g', 'gaiaDR2_b', 'gaiaDR2_r']
for band in gaia:
   if band in info.keys():   
      flux0 = sed.calcFlux(astSED.Passband(path+'GAIA/'+band+'.dat'))
      print flux0, 2.5*np.log10(flux0)
#      print astSED.flux2Mag(flux0, 0.1*flux0, astSED.Passband(path+'GAIA/'+band+'.dat'))
      mag   = sed.calcMag(astSED.Passband(path+'GAIA/'+band+'.dat'), addDistanceModulus=False, magType='AB')
#      print mag
      mag   = mag - 2.5*np.log10(3.) +2.5*np.log10(c)
#      print mag



