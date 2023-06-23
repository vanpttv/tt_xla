import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im1=vol[13,:,:]
im2=vol[20,:,:]
print(im1.shape, im2.shape)
plt.figure(1)
plt.subplot(1, 2,1)
plt.imshow(im1, cmap='gray')
plt.colorbar()
plt.subplot(1, 2,2)
plt.imshow(im2, cmap='gray')
plt.colorbar()

# Convert binary
def convert_bin(q):
	mask=q>150
	#k=np.where(mask,1,0)
	return mask
im1 = vol[13,:,:]
im_bin1= convert_bin(im1)
im2 = vol[20,:,:]
im_bin2= convert_bin(im2)

# Calculate image difference
err = im1-im2

# Plot the difference
plt.figure(2)
plt.imshow(err, cmap="seismic")
plt.colorbar()

# Calculate absolute image difference
abs_err = np.absolute(im1 - im2)
mean_abs_err = np.mean(np.abs(im_bin1.astype('uint8') - im_bin2.astype('uint8')))
print('MAE:', mean_abs_err)
# Calculate absolute image difference
abs_err = np.abs(im_bin1.astype('uint8') - im_bin2.astype('uint8'))

# Plot the difference
plt.figure(3)
plt.imshow(abs_err, cmap='seismic')
plt.colorbar()
plt.show()