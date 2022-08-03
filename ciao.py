import ciao_contrib.runtool as rt
from ciao_contrib.runtool import dmlist
from ciao_contrib.runtool import *
from ciao_contrib.runtool import acis_process_events, dmstat, dmmerge

import ciao_contrib.proptools as proptools #go between coordinates

from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs

import astropy 
import pyvo as vo

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sherpa

ra =  8.815
dec = -43.566
sr = search_chandra_archive(ra, dec, size=0.1, instrument=None, grating=None)

print(sr)
print(sr.dtype.names[0:5])
print(sr[0])

print("hello world")
#dmlist('ngc133.fits', 'blocks')
#dmlist('csc2.fits') #, 'blocks')
#help(rt.new_pfiles_environment)

#dmstat("img.fits")
# make data
"""
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
plt.plot(x, y)
plt.show()
"""
from astropy.coordinates import SkyCoord
from astropy import units as u
ngc1333 = SkyCoord.from_name('NGC 1333')
maxrad = 2.0 * u.arcmin


ngc1333 = SkyCoord.from_name('NGC 1333')
maxrad = 2.0 * u.arcmin

ngc1333

cone = vo.dal.SCSService('http://cda.cfa.harvard.edu/csc2scs/coneSearch')

results = cone.search(pos=ngc1333, radius=maxrad)
  
print(results)

#plt.plot(results['ra'], results['dec'], 'o')

#plt.show()

galaxiesFull = pd.read_csv("galaxies_full.csv", sep = ',')  
raGalaxies = galaxiesFull["RA(deg)"] #right ascention
decGalaxies = galaxiesFull["DEC(deg)"] #decllination

for i in range(np.size(raGalaxies)):
    ra = raGalaxies[i]
    dec = decGalaxies[i]

#help(rt)

#help(get_source())

#dmlist('ngc1333.fits', 'blocks')