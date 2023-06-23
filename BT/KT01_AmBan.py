import imageio
import matplotlib.pyplot as plt
import numpy as np
import time

im=imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')
print('Type:',type(im))
print('Shape:',im.shape)
print(im.shape[0], im.shape[1])
fig, axes= plt.subplots(nrows=3, ncols=1)
axes[0].imshow(im, cmap='gray')

start_time=time.time()
anh_bd=np.zeros(im.shape, dtype='uint8')
k=np.zeros(im.shape, dtype='uint8')
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        r = im[i, j]
        if r<=-1000:
            k[i,j]=r*0.005+15
        else:
            k[i,j]=r*49/600+275/3
axes[1].imshow(k, cmap='gray')

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        anh_bd[i,j]=255-k[i,j]
end_time=time.time()
print('Seconds:', end_time-start_time)
axes[2].imshow(anh_bd, cmap='gray')
plt.show()