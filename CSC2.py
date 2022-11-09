"""import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import astropy
import pyvo as vo
#import scipy
from astropy.coordinates import SkyCoord
from astropy import units as u
from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs
import numpy as np
import pandas as pd
import time

m33 = SkyCoord.from_name('M33')
maxrad = 0.166667 * u.deg #this is 10 arcmin

#cone = vo.dal.SCSService('https://cda.cfa.harvard.edu/csc21_snapshot_scs/coneSearch')

#results = cone.search(pos=m33, radius=maxrad, verbosity=3)
#len(results)
#print(results)
print(help(search_chandra_archive))"""



#import sherpa
from ciao_contrib.cda.search import search_chandra_archive, get_chandra_obs
import numpy as np
import pandas as pd
import time

start = time.time() #start a time to see how long it takes


galaxiesFull = pd.read_csv("mag_change.txt", delim_whitespace=True)  
raGalaxies = galaxiesFull["SDSS_RA"] #right ascention
decGalaxies = galaxiesFull["SDSS_DEC"] #decllination

print("Writing file")
with open(r'csc3degcat21.txt', 'w') as fp:
        fp.write("Num\tObsID\t\t\t\t\t\tTarget_Name\t\t\t\t\tMy_RA\t\t\t\tCSC_RA\t\t\tMy_DEC\t\t\tCSC_DEC\t\tInstrument\t\tObs_Date\n")
        for j in range(np.size(raGalaxies)):
            ra = raGalaxies[j]
            dec = decGalaxies[j]
            sr = search_chandra_archive(ra, dec, size=3.0) #size is how many degrees away in arcsec
            if sr is None:
                continue
            else:
                obs = get_chandra_obs(sr)
                count = np.size(obs['obsid'])
                for i in range(count):
                    fp.write("%5d\t%8s\t%29s\t%12.6f\t%12.6f\t%12.6f\t%12.6f\t%9s\t%21s\n" %( (j+1) ,(obs['obsid'][i]), (obs['target'][i]).replace(" ", "") , (raGalaxies[j]), (obs['ra'][i]), (decGalaxies[j]), (obs['dec'][i]), (obs['instrument'][i]), (obs['obsdate'][i]) ) )
                    
print("finished")
print(f'Numpy: {time.time() - start} seconds')
