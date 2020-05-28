import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("outcomes.log").T

fig,ax = plt.subplots(nrows=len(data),ncols=1,sharex='col',sharey='all',
							figsize=(5,10))

rw = 0.9
rnge = (0,1500)
nbins = 50

ax[0].hist(data[0],bins=nbins,rwidth=rw,range=rnge)
ax[1].hist(data[1],bins=nbins,rwidth=rw,range=rnge)
ax[2].hist(data[2],bins=nbins,rwidth=rw,range=rnge)



ax[0].set_title('Inside Only - 1 unit')
ax[1].set_title('Triple Lux')
ax[2].set_title('Double Single')
plt.show()