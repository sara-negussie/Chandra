import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import astropy
import pyvo as vo
#import scipy
from astropy.coordinates import SkyCoord
from astropy import units as u

m33 = SkyCoord.from_name('M33')
maxrad = 1.0 * u.deg

cone = vo.dal.SCSService('https://cda.cfa.harvard.edu/csc21_snapshot_scs/coneSearch')

results = cone.search(pos=m33, radius=maxrad, verbosity=3)
len(results)
print(results)