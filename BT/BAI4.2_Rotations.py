import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im=vol[20,:,:]

# Smooth intensity values
im_filt=ndi.median_filter(im,size=3)

# Select high-intensity pixels
mask_start = np.where(im_filt>400, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Find image center of mass
com = ndi.center_of_mass(labels, labels, index=7) #label cua tim là label = 7

# Calculate amount of shift needed
d0 = 128-com[0]
d1 = 128-com[1]
print(com[0], com[1], d0, d1)

# Translate the brain towards the center
xfm = ndi.shift(im, shift=(d0, d1))

# Rotate the shifted image
xfm = ndi.rotate(xfm, angle=-30, reshape=False)

# Plot the original and rotated images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(xfm, cmap='gray')
plt.show()
