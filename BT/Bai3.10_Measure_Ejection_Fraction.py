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

ts = np.zeros(30)

# Calculate volume at each voxel
d1, d2, d3 = vol.meta['sampling']
dvoxel = d2*d3

for t in range(30):
    nvoxels = ndi.sum(1,labels, index=[128,128])
    ts[t] = nvoxels*dvoxel

# Get index of max and min volumes
tmax = np.argmax(ts)
tmin = np.argmin(ts)

# Plot the largest and smallest volumes
fig, axes = plt.subplots(2, 1)
# axes[0].imshow(____, vmax=160)
# axes[1].imshow(____, vmax=160)
# format_and_render_plots()

# Calculate ejection fraction
ej_vol = ts.max() - ts.min()
ej_frac = ej_vol/ts.max()
print('Est. ejection volume (mm^3):', ej_vol)
print('Est. ejection fraction:', ej_frac)