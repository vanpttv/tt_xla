import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", 'DICOM')

# Smooth intensity values
vol_filt=ndi.median_filter(vol,size=3)

# Select high-intensity pixels
mask_start = np.where(vol_filt>350, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

d0,d1,d2=vol.meta['sampling']
dvoxels=d1*d2
nvoxels=ndi.sum(1, labels,index=6)
volumn=nvoxels*dvoxels
print('Dữ liệu ', vol.meta)
print('doxel: ', dvoxels)
print('nvoxel: ', nvoxels)
print('Thể tích là: ', volumn)