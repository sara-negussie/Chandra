#cross matching sdss and chandra


#import packages
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np
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


#import sdss coordinates
sdssCoords = pd.read_csv('mag_change.txt', delim_whitespace=True)
port_coords = SkyCoord(sdssCoords['SDSS_RA']*u.deg, sdssCoords['SDSS_DEC']*u.deg)


#data release 2.1
cone = vo.dal.SCSService('https://cda.cfa.harvard.edu/csc21_snapshot_scs/coneSearch') 

#query parameters
qry = '''SELECT DISTINCT m.name,m.ra,m.dec
FROM csc21_snapshot.master_source m'''

#new data release 2.1

tap = vo.dal.TAPService('http://cda.cfa.harvard.edu/csc21_snapshot_tap/') 
print('Querying...')

cat = tap.search(qry)

print('Writing...')
import sys
import re
with open('csc21crossmatch.txt','w') as f:
    f.write('name\t\tra\t\tdec\n')
    for i in range(len(cat['ra'])):
        f.write(f'{re.sub(" ","",cat["name"][i])},{cat["ra"][i]},{cat["dec"][i]}\n')

sys.exit()

CSC_21_coords = SkyCoord(ra = cat['ra'] * u.deg, dec = cat['dec']*u.deg)

#can add argument to change to the second, third, etc nearest neighbor
#idx_ is an array of indices into port coords matching the shape of CSC_21_coords
#describing which items in port_coords each item of CSC_21_coords matched to
idx_,sep2d_,_ = CSC_21_coords.match_to_catalog_sky(port_coords)

sep_mask = [True if i <= 10*u.arcsec else False for i in sep2d_]

idx_matches = idx_[sep_mask]
CSC_21_coords_matches = CSC_21_coords[sep_mask]

SDSS_mask = [True if i in idx_matches else False for i in range(len(port_coords))]
port_matches = port_coords[SDSS_mask]

CSC_names_matches = cat['name'][sep_mask]

"""
SDSS_bIDs = sdssCoords['bestObjID']
SDSS_sIDS = sdssCoords['specObjID']
SDSS_zs = sdssCoords['z']

SDSS_bIDs_matches = [SDSS_bIDs[i] for i in idx_matches]

SDSS_sIDS_matches = [SDSS_sIDS[i] for i in idx_matches]

SDSS_zs_matches = [SDSS_zs[i] for i in idx_matches]
"""
CSC_RA_matches = [i.ra.deg for i in CSC_21_coords_matches]
CSC_dec_matches = [i.dec.deg for i in CSC_21_coords_matches]

SDSS_RA_matches = [port_coords[i].ra.deg for i in idx_matches]
SDSS_dec_matches = [port_coords[i].dec.deg for i in idx_matches]

#save the full match CSV
csv_out = np.column_stack((CSC_names_matches,CSC_RA_matches,CSC_dec_matches,SDSS_RA_matches,SDSS_dec_matches))
header = 'CSC NAME,CSC RA,CSC DEC,SDSS RA,SDSS DEC'
np.savetxt('CSC21_SDSS_10arcsec_crossmatch.csv',csv_out,fmt='%s',delimiter=',',header=header)

#save the coords doc which will be used by full process
header_2 = 'name  ra  dec'
coords_out = np.column_stack((CSC_names_matches,CSC_RA_matches,CSC_dec_matches))
np.savetxt('CSC21_coords.txt',coords_out,fmt='%s',delimiter='  ',header=header_2)

