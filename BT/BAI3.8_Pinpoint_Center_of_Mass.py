import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", 'DICOM')

# Smooth intensity values
vol_filt=ndi.median_filter(vol,size=3)

# Select high-intensity pixels
mask_start = np.where(vol_filt>450, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Extract centers of mass for objects 1 and 2
coms = ndi.center_of_mass(vol, labels, index=6)
# print('Label 1 center:', coms[0])
# print('Label 2 center:', coms[1])

# Add marks to plot
plt.imshow(vol[20,:,:], cmap='gray')
# for c0, c1, c2 in coms:
#     plt.scatter(c1, c2, s=100, marker='o')
plt.scatter(coms[2], coms[1], s=100, marker='o')
plt.show()