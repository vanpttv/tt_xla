import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im=vol[20,:,:]

# Smooth intensity values
im_filt=ndi.median_filter(im,size=3)

# Select high-intensity pixels
mask_start = np.where(im_filt>350, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)
# print(labels)

# Select left ventricle pixels
# lv_val = labels[128,114]
lv_val=6
print(lv_val)
lv_mask = np.where(labels==lv_val,1,0)

# Find bounding box of left ventricle
bboxes = ndi.find_objects(lv_mask)
print('Number of objects:', len(bboxes))
print('Indices for first box:', bboxes[0])


# Crop to the left ventricle (index 0)
im_lv = im[bboxes[0]]

# Plot the cropped image
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.figure(2)
plt.imshow(im_filt, cmap='gray')
plt.colorbar()
plt.figure(3)
plt.imshow(labels, cmap='rainbow')
plt.colorbar()
plt.figure(4)
plt.imshow(lv_mask, cmap='rainbow')
plt.colorbar()
plt.figure(5)
plt.imshow(im_lv, cmap='gray')
plt.colorbar()
plt.show()