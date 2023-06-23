#!/usr/bin/env python
# coding: utf-8

# In[79]:


import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage import color
from skimage import io


# In[80]:


im1_goc = imageio.imread('D:\HK2_2021\TT_XLA\CUOI KY\image1.jpg')
im2_goc = imageio.imread('D:\HK2_2021\TT_XLA\CUOI KY\image2.jpg')
im1 = color.rgb2gray(io.imread('D:\HK2_2021\TT_XLA\CUOI KY\image1.jpg'))
im2 = color.rgb2gray(io.imread('D:\HK2_2021\TT_XLA\CUOI KY\image2.jpg'))


# In[81]:


plt.figure()
plt.subplot(2,2,1)
plt.imshow(im1_goc)
plt.title("Ảnh REF")
plt.subplot(2,2,2)
plt.imshow(im2_goc)
plt.title("Ảnh test")

plt.subplot(2,2,3)
plt.imshow(im1, cmap='gray')
plt.colorbar()
plt.title("Ảnh REF")
plt.subplot(2,2,4)
plt.imshow(im2, cmap='gray')
plt.colorbar()
plt.title("Ảnh test")


# In[82]:


image1=np.zeros(im1.shape, dtype='uint8')
image2=np.zeros(im2.shape, dtype='uint8')
print(image1.shape, image2.shape)
min1=im1.min()
max1=im1.max()
min2=im2.min()
max2=im2.max()
print("Hệ số:", min1, max1, min2, max2)
for i in range(im1.shape[0]):
    for j in range(im1.shape[1]):
        r=im1[i,j]
        image1[i,j]=r*(255/(1-min1))+((255*min1)/(min1-1))
for i in range(im2.shape[0]):
    for j in range(im2.shape[1]):
        r=im2[i,j]
        image2[i,j]=r*(255/(1-min2))+((255*min2)/(min2-1))
plt.figure()
plt.subplot(1,2,1)
plt.imshow(image1,cmap='gray')
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(image2,cmap='gray')
plt.colorbar()


# In[83]:


# a: Tinh ERR RAW
# Convert binary
def convert_bin(q):
    mask=q>100
    return mask
im_bin1= convert_bin(image1)
im_bin2= convert_bin(image2)

# Calculate absolute image difference
abs_err = np.abs(im_bin1.astype('int') - im_bin2.astype('int'))


# Calculate mean absolute error
mean_abs_err = np.mean(abs_err)
print('MAE:', mean_abs_err)

plt.figure()
plt.imshow(im_bin1, cmap="gray")
plt.colorbar()
plt.figure()
plt.imshow(im_bin2, cmap='gray')
plt.colorbar()
plt.figure()
plt.imshow(abs_err, cmap='gray')
plt.colorbar()


# In[84]:


# b: Tim tam va dich
mask1 = np.where(image1>100, 1, 0)
# Label the objects in "mask"
labels1, nlabels1 = ndi.label(mask1)
print('Num. Labels:', nlabels1)
# Find image center of mass
com1 = ndi.center_of_mass(labels1, labels1, index=1)
print(com1[0], com1[1])


# In[85]:


mask2 = np.where(image2>100, 1, 0)
# Label the objects in "mask"
labels2, nlabels2 = ndi.label(mask2)
print('Num. Labels:', nlabels2)
# Find image center of mass
com2 = ndi.center_of_mass(labels2, labels2, index=1)

# Calculate amount of shift needed
d02 = com1[0]-com2[0]
d12 = com1[1]-com2[1]
print(com2[0], com2[1], d02, d12)


# In[86]:


im_trans = ndi.shift(image2, shift=(d02, d12))
mask = np.where(im_trans>100, 1, 0)
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)
com = ndi.center_of_mass(labels, labels, index=1)

# Calculate amount of shift needed
d0 = 128-com[0]
d1 = 128-com[1]
print(com[0], com[1], d0, d1)


# In[87]:


plt.figure()
plt.imshow(labels2, cmap='rainbow')
plt.colorbar()
plt.title("Ảnh Label")
plt.figure()
plt.imshow(im_trans, cmap='gray')
plt.colorbar()
plt.title("Ảnh dịch tâm")


# In[88]:


im_bin2_l2= convert_bin(im_trans)

# Calculate absolute image difference
abs_err_l2 = np.absolute(im_bin1.astype('int')- im_bin2_l2.astype('int'))

# Calculate mean absolute error
mean_abs_err_l2 = np.mean(np.abs(im_bin1.astype('int') - im_bin2_l2.astype('int')))
print('MAE:', mean_abs_err_l2)


# In[89]:


plt.figure()
plt.subplot(1,2,1)
plt.imshow(im_bin1, cmap="gray")
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(im_bin2_l2, cmap='gray')
plt.colorbar()
plt.figure()
plt.imshow(abs_err_l2, cmap='gray')
plt.colorbar()


# In[90]:


mae=[]
for i in range(360):
    im_ro = ndi.rotate(im_trans, angle=-i, reshape=False)
    im_bin2_new = convert_bin(im_ro)
    mean_abs_err_l2 = np.mean(np.abs(im_bin1.astype('int') - im_bin2_new.astype('int')))
    mae.append(mean_abs_err_l2)
    print('MAE:',[i, mean_abs_err_l2])


# In[91]:


print([min(mae),mae.index(min(mae))])


# In[92]:


im_ro = ndi.rotate(im_trans, angle=-321, reshape=False)
plt.figure()
plt.imshow(image1, cmap='gray')
plt.colorbar()
plt.title("Ảnh gốc")
plt.figure()
plt.imshow(im_ro, cmap='gray')
plt.colorbar()
plt.title("Ảnh xoay")

