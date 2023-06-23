import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", 'DICOM')

# Create an empty time series
ts = np.zeros(vol.shape[0])

# Calculate volume at each voxel
d1, d2, d3 = vol.meta['sampling']
dvoxel = d2*d3

# Loop over the labeled arrays
for t in range(30):
    im = vol[t, :, :]
    # Smooth intensity values
    im_filt = ndi.median_filter(im, size=3)
    # Select high-intensity pixels
    mask_start = np.where(im_filt > 250, 1, 0)
    mask = ndi.binary_closing(mask_start)
    labels, nlabels = ndi.label(mask)
    nvoxels = ndi.sum(1,labels, index=labels[128,128])
    ts[t] = nvoxels*dvoxel
    # plt.imshow(labels, cmap='rainbow')
    # plt.pause(0.005)

# Plot the data
print(ts)
plt.plot(ts)
plt.show()