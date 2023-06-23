import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

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

# Create a `labels` overlay
overlay = np.where(labels>0, labels, np.nan)

plt.figure(1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.figure(2)
plt.imshow(im_filt, cmap='gray')
plt.colorbar()
plt.figure(3)
plt.imshow(overlay, cmap='rainbow', alpha=0.75)
plt.colorbar()
plt.figure(4)
plt.imshow(labels, cmap='rainbow')
plt.colorbar()
plt.figure(5)
plt.imshow(mask_start, cmap='rainbow')
plt.colorbar()
plt.show()
