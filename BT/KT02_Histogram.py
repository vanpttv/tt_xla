# Import ImageIO
import  imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

# Load the "tcia-chest-ct" directory
vol = imageio.volread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol', 'DICOM')
im=vol[100, :, :]
print('Min value anh goc:', im.min())
print('Max value anh goc:', im.max())
fig, axes = plt.subplots(2, 2, sharex=True)
axes[0,0].imshow(im, cmap='gray')
axes[0,0].set_title('Ảnh từ tập vol')
im[im>2000]=2000
print('Min value anh bien doi:', im.min())
print('Max value anh bien doi:', im.max())
k=np.zeros(im.shape, dtype='uint8')
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        r = im[i, j]
        if r<=-1000:
            k[i,j]=r*0.005+15
        else:
            k[i,j]=r*49/600+275/3

axes[0,1].imshow(k, cmap='gray')
axes[0,1].set_title('Ảnh từ 0 đến 255')
print("Data Type:", k.dtype)
print('Min value:', k.min())
print('Max value:', k.max())

hist=ndi.histogram(k, min=0, max=255, bins=256)
axes[1,0].plot(hist)
axes[1,0].set_title('Histogram')

cdf = hist.cumsum() / hist.sum()
print(cdf.shape)
im_equalized = cdf[k] * 255
axes[1,1].imshow(im_equalized, cmap='gray')
axes[1,1].set_title('Ảnh cân bằng')

plt.show()