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

# Calculate left ventricle distances
lv = np.where(labels==6, 1, 0)
dists = ndi.distance_transform_edt(lv, sampling=vol.meta['sampling'])

# Report on distances
print('Max distance (mm):', ndi.maximum(dists))
print('Max location:', ndi.maximum_position(dists))

# Plot overlay of distances
overlay = np.where(dists[5] > 0, dists[5], np.nan)
plt.imshow(overlay, cmap='hot')
plt.show()