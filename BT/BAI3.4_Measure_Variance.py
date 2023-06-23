import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")

# Smooth intensity values
vol_filt=ndi.median_filter(vol,size=3)

# Select high-intensity pixels
mask_start = np.where(vol_filt>350, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Select left ventricle pixels
lv_val = labels[120,120]
print(lv_val)
lv_mask = np.where(labels==lv_val,1,np.nan)

# Variance for all pixels
var_all = ndi.variance(vol)
print('All pixels:', var_all)

# Variance for labeled pixels
var_labels = ndi.variance(vol, labels)
print('Labeled pixels:', var_labels)

# Variance for each object
var_objects = ndi.variance(vol, labels=lv_mask)
print('Left ventricle:', var_objects[0])
# print('Other tissue:', var_objects[1])

# Plot the image
# for i in range (vol.shape[0]):
#     plt.imshow(labels[i,:,:], cmap='rainbow')
#     plt.pause(0.005)


