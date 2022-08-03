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

#for i in range(1): #(np.size(raGalaxies)):
i = 12
ra = raGalaxies[i]
dec = decGalaxies[i]
sr = search_chandra_archive(ra, dec, size=0.3) #size is how many degrees away

search.append(sr)
print("size of search = ", np.size(search))
print(search)

obs = get_chandra_obs(sr)
print(obs.keys())
from ciao_contrib.cda.data import download_chandra_obsids
download_chandra_obsids([1843])

9548