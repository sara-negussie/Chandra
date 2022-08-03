import sherpa
from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs
import numpy as np
import pandas as pd

galaxiesFull = pd.read_csv("galaxies_full.csv", sep = ',')  
raGalaxies = galaxiesFull["RA(deg)"] #right ascention
decGalaxies = galaxiesFull["DEC(deg)"] #decllination
#PosErr_Galaxies = galaxiesFull.iloc[:, 4] #position error
#PosErr_Galaxies

search = []

#for i in range(5): #(np.size(raGalaxies)):
i = 12
ra = raGalaxies[i]
dec = decGalaxies[i]
sr = search_chandra_archive(ra, dec, size=0.3) #size is how many degrees away

"""if len(sr) == 0:
    continue  170.06291667, 12.98933333
else:
    search.append(sr)
"""
#print("size of sr = ", np.size(sr))
#print("sr=", sr)
#print(search)

#search.append(sr)

obs = get_chandra_obs(sr)
#np.size(obs)
#obsid = obs['obsid']
#target = obs['target']
#print(obsid)
#print(target)

#help(get_chandra_obs)
#obsid = obs['obsid']
#target = obs['target']
#count = np.size(sr)
#print(obsid)
#print(target[0])

#print(target)

print("Writing file")
#j = 12

with open(r'csc.txt', 'w') as fp:
        fp.write("ObsID\tTarget\tMy RA\tCSC RA\tMy DEC\tCSC DEC\n")
        for j in range(12): #(np.size(raGalaxies)):
            ra = raGalaxies[j]
            dec = decGalaxies[j]
            sr = search_chandra_archive(ra, dec, size=0.3) #size is how many degrees away
            if sr is None:
                continue
            else:
                obs = get_chandra_obs(sr)
                count = np.size(sr)
                for i in range(count):
                        #fp.write("%s\t%s\t%f\t%f\t%f\t%f\n" %( (obs['obsid'][i]), (obs['target'][i]), (raGalaxies[j]), (obs['ra'][i]), (decGalaxies[j]), (obs['ra'][i]) ) )
                    print(i)
                    print(obs['obsid'][i])
                    #print(i, (obs['obsid'][i]), (obs['target'][i]), (raGalaxies[j]), (obs['ra'][i]), (decGalaxies[j]), (obs['ra'][i]) )
#print("size of search = ", np.size(search))
#print(search)
#print(obs.keys())
#from ciao_contrib.cda.data import download_chandra_obsids
#download_chandra_obsids([1843])

"""
      obsid
      instrument
      grating
      exposure       in ks
      ra             aim point ra in degrees
      dec            aim point dec in degrees
      target         target name
      obsdate
      piname         last name of PI
      separation     separation of aim point from ra,dec in arcminute
from astropy.io import fits

fits_image_filename = '9548/primary/acisf09548_000N003_bpix1.fits.gz'
with fits.open(fits_image_filename) as hdul:
    hdul.info()
"""