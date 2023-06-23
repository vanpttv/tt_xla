import imageio
import matplotlib.pyplot as plt
import time
import numpy as np
import scipy.ndimage as ndi

vol=imageio.volread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol', 'DICOM')
im=vol[100, :, :]

start_time=time.time()
k=np.zeros(im.shape, dtype='uint8')
a1=-10/(im.min()+1000)
b1=(10*im.min())/(im.min()+1000)
a2=245/(1000+im.max())
b2=(1000*255+10*im.max())/(1000+im.max())
print("Hệ số:", a1, b1, a2, b2)
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        r=im[i,j]
        if r<=-1000:
            k[i,j]=r*a1+b1
        else:
            k[i,j]=r*a2+b2

hist=ndi.histogram(k, min=0, max=255, bins=256)
cdf=hist.cumsum()/hist.sum()
im_equalized=cdf[k]*255

end_time=time.time()
print("Second:", end_time-start_time)

plt.subplot(2,2,1)
plt.imshow(im, cmap='gray')
plt.title("Ảnh được đọc từ tập vol", size=7)
plt.colorbar()
plt.subplot(2,2,2)
plt.imshow(k, cmap='gray')
plt.title("Ảnh chuyển 0 - 255", size=7)
plt.colorbar()
plt.subplot(2,2,3)
plt.plot(hist)
plt.title("Histogram", size=7)
plt.subplot(2,2,4)
plt.imshow(im_equalized, cmap='gray')
plt.colorbar()
plt.title("Ảnh sau khi cân bằng histogram", size=7)

plt.show()
