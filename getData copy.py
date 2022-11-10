#import sherpa
from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs
import numpy as np
import pandas as pd
import time

start = time.time() #start a time to see how long it takes


galaxiesFull = pd.read_csv("mag_change.txt", delim_whitespace=True)  
raGalaxies = galaxiesFull["My_RA"] #right ascention
decGalaxies = galaxiesFull["My_DEC"] #decllination

print("Writing file")
with open(r'csc10arcminp2.txt', 'w') as fp:
        fp.write("This is using the original coordinate. and finding everything within 10arcmin.\n")
        fp.write("Num\tObsID\t\t\t\t\t\tTarget_Name\t\t\t\t\tMy_RA\t\t\t\tCSC_RA\t\t\tMy_DEC\t\t\tCSC_DEC\t\tInstrument\t\tObs_Date\n")
        for j in range(np.size(raGalaxies)):
            ra = raGalaxies[j]
            dec = decGalaxies[j]
            sr = search_chandra_archive(ra, dec, size=0.166667) #size is how many degrees away
            if sr is None:
                continue
            else:
                obs = get_chandra_obs(sr)
                count = np.size(obs['obsid'])
                for i in range(count):
                    fp.write("%4d\t%7s\t%27s\t%12.6f\t%12.6f\t%12.6f\t%12.6f\t%9s\t%21s\n" %( (j+1) ,(obs['obsid'][i]), (obs['target'][i]).replace(" ", "") , (raGalaxies[j]), (obs['ra'][i]), (decGalaxies[j]), (obs['dec'][i]), (obs['instrument'][i]), (obs['obsdate'][i]) ) )
                    
print("finished")
print(f'Numpy: {time.time() - start} seconds')
