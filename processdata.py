from astropy.io import fits

from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
import numpy as np

hdulist = fits.open('catwithdis.fit')
data = hdulist[1].data
c = SkyCoord(data['ra'] * u.deg, data['dec'] * u.deg, frame='icrs')
l = c.galactic.l.degree
b = c.galactic.b.degree
col_l = fits.Column(name='l', format='D', array=l)
col_b = fits.Column(name='b', format='D', array=b)
new_cols = fits.ColDefs([col_l, col_b])
orig_cols = data.columns
hdu = fits.BinTableHDU.from_columns(orig_cols + new_cols)
hdu.writeto('newtable.fits')