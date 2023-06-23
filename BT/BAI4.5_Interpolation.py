import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im=vol[20,:,:]
print(im.shape)

# Upsample "im" by a factor of 4
up0 = ndi.zoom(im, zoom=2, order=0)
up5 = ndi.zoom(im, zoom=2, order=5, mode='wrap') #4.693737030029297

# Print original and new shape
print('Original shape:', im.shape)
print('Upsampled shape:', up0.shape, up5.shape)
print('Upsampled shape:', up0.min(), up0.max(), up5.min(), up5.max())

# Plot close-ups of the new images
fig, axes = plt.subplots(1, 3)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(up0[128:256, 128:256], cmap='gray')
axes[2].imshow(up5[128:256, 128:256], cmap='gray')

im1=up0
im2=up5
# Calculate image difference
err = im1-im2

# Plot the difference
plt.figure(2)
plt.imshow(err, cmap="seismic")
plt.colorbar()

# Calculate absolute image difference
abs_err = np.absolute(im1 - im2)

# Plot the difference
plt.figure(3)
plt.imshow(abs_err, cmap='seismic')
plt.colorbar()

# Calculate mean absolute error
mean_abs_err = np.mean(np.abs(im1 - im2))
print('MAE:', mean_abs_err)
plt.show()