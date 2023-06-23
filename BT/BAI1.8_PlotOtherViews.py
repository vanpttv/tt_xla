import imageio
import matplotlib.pyplot as plt

vol=imageio.volread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol', 'DICOM')

# Select frame from "vol"
im1=vol[:, 256, :]
im2=vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2=vol.meta['sampling']
print(d0, d1, d2)
asp1=d0/d2
asp2=d0/d1

# Plot the images on a subplots array
fig, axes=plt.subplots(nrows=4, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=asp1)
axes[1].imshow(im2, cmap='gray', aspect=asp2)

axes[2].imshow(im1, cmap='gray')
axes[3].imshow(im2, cmap='gray')

plt.show()