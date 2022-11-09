#import sherpa
from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs
import numpy as np
import pandas as pd
import time

start = time.time() #start a time to see how long it takes


galaxiesFull = pd.read_csv("galaxies_full.csv", sep = ',')  
raGalaxies = galaxiesFull["RA(deg)"] #right ascention
decGalaxies = galaxiesFull["DEC(deg)"] #decllination

print("Writing file")
with open(r'csc1degcat21.txt', 'w') as fp:
        fp.write("Num\tObsID\t\t\t\t\t\tTarget_Name\t\t\t\t\tMy_RA\t\t\t\tCSC_RA\t\t\tMy_DEC\t\t\tCSC_DEC\t\tInstrument\t\tObs_Date\n")
        for j in range(np.size(raGalaxies)):
            ra = raGalaxies[j]
            dec = decGalaxies[j]
            sr = search_chandra_archive(ra, dec, size=1.0) #size is how many degrees away in arcsec
            if sr is None:
                continue
            else:
                obs = get_chandra_obs(sr)
                count = np.size(obs['obsid'])
                for i in range(count):
                    fp.write("%4d\t%7s\t%27s\t%12.6f\t%12.6f\t%12.6f\t%12.6f\t%9s\t%21s\n" %( (j+1) ,(obs['obsid'][i]), (obs['target'][i]).replace(" ", "") , (raGalaxies[j]), (obs['ra'][i]), (decGalaxies[j]), (obs['dec'][i]), (obs['instrument'][i]), (obs['obsdate'][i]) ) )
                    
print("finished")
print(f'Numpy: {time.time() - start} seconds')
