import numpy as np
import pandas as pd
import time
from astropy.io import fits

fits_image_filename = '9548/primary/acisf09548_000N003_bpix1.fits.gz'
with fits.open(fits_image_filename) as hdul:
    hdul.info()