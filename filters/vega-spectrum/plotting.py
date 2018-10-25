#/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

w,f = np.loadtxt('alpha_lyr_004.ascii', unpack=True)
#plt.plot(w,f, label='alpha_lyr_004')
w,f = np.loadtxt('alpha_lyr_mod_002.txt', unpack=True)
plt.plot(w,f, label='alpha_lyr_mod_002')
w,f = np.loadtxt('bohlin2006_Vega.sed', unpack=True)
plt.plot(w,f, label='bohlin2006_Vega')
plt.legend()
plt.show()
