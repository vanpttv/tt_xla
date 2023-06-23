import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im=vol[20,:,:]
print(im.shape)

# Center and level image
xfm = ndi.shift(im, shift=(-20,-20))
xfm = ndi.rotate(xfm, angle=-35, reshape=False)

# Resample image
im_dn = ndi.zoom(xfm, zoom=0.25)
im_up = ndi.zoom(xfm,zoom=4)

# Plot the images
fig, axes = plt.subplots(1, 4)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(xfm, cmap='gray')
axes[2].imshow(im_dn, cmap='gray')
axes[3].imshow(im_up, cmap='gray')
plt.show()