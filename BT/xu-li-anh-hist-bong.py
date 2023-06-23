# Import SciPy's "ndimage" module
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import imageio
import cv2
import numpy as np
# Create a histogram, binned at each possible value
image = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')
image[image>2000]=2000
goc=np.zeros(image.shape, dtype='uint8')
anh=np.zeros(image.shape, dtype='uint8')
k=np.zeros(image.shape, dtype='uint8')
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        r=image[i,j]
        if r<=-1000:
            k[i,j]=r*0.005+15
        else:
            k[i,j]=r*49/600+275/3

# img_equal_hist = cv2.equalizeHist(anh)
hist = ndi.histogram(k, min=0,max=255,  bins=256)
cdf = hist.cumsum() / hist.sum()
cdf.shape
img_equal_hist=cdf[k]*255
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(hist, label='Histogram')
axes[0].set_title('Histogram')
axes[1].imshow (img_equal_hist, cmap='gray')
plt.show()
