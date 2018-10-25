#/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt



pss   = ['PAN-STARRS_g', 'PAN-STARRS_r', 'PAN-STARRS_i', 'PAN-STARRS_z', 'PAN-STARRS_y']

for i, ps in enumerate(pss):
   w,f = np.loadtxt(ps+'.dat', dtype=None, unpack=True)
   plt.plot(w,f, label=ps)

plt.legend()
plt.show()
