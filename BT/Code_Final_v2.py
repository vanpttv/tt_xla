# Load data
import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
vol = imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
#vol = imageio.volread('D:\\MON HOC\\TT XLA\\Biomedical-Image-Analysis-in-Python-master\\Alzhiemer\\SCD2001_001','DICOM')
#vol = imageio.volread('D:\\MON HOC\\TT XLA\\Biomedical-Image-Analysis-in-Python-master\Alzhiemer\\ID00007637202177411956430','DICOM')
#vol = imageio.volread('D:\MON HOC\TT XLA\Biomedical-Image-Analysis-in-Python-master\Alzhiemer\chess','DICOM')
im = vol[20,:,:]
# def format_and_render_plot():
    # fig = plt.gcf()
    # fig.axes[0].axis('off')
    # plt.tight_layout()
    # plt.show()
# Excercise 1: Translation - Dịch ảnh
# Smooth intensity values
im_filt = ndi.median_filter(im,size=3)
# Select high-intensity pixels
mask_start = np.where(im_filt>150, 1, 0)
# Label the objects in "mask"
labels, nlabels = ndi.label(mask_start)
print('Num. Labels:', nlabels)
# Find image center of mass
com = ndi.center_of_mass(labels, labels, index=20) #label cua tim là label = 7 # label la input, label thu hai la những label được đánh dấu
#
d0 = im.shape[0]/2-com[0]
d1 = im.shape[1]/2-com[1]
print(com[0], com[1], d0, d1)
# Translate the brain towards the center
im_trs = ndi.shift(im, shift=(d0, d1))
# Plot the original and adjusted images

fig,axes = plt.subplots(nrows=3, ncols=4)
axes[0,0].imshow(im, cmap='gray')
axes[0,0].set_title('anh goc')
axes[0,0].axis(False)
axes[0,1].imshow(labels, cmap='rainbow')
axes[0,1].set_title('anh label')
axes[0,1].axis(False)
axes[0,2].imshow(im_trs, cmap='gray')
axes[0,2].set_title('anh trans')
axes[0,2].axis(False)

# Excercise 2: Rotations - Xoay ảnh
im_ro = ndi.rotate(im_trs, angle=-30, reshape=False)
axes[0,3].imshow(im_ro,cmap='gray')
axes[0,3].set_title("anh xoay")
axes[0,3].axis(False)
# Excercise 3: Affine transform - Biến đổi ảnh

mat1 = np.array([[0.8, -0.4, 90],
                 	[0.4, 0.8, -6.0],
                 	[0, 0, 1]])
mat2 = np.array([[1, 0, 0],
                 	[0, 1, 0],
                 	[0, 0, 1]])
mat3 = np.array([[1, -0.3, 60],
                 	[-0.3, 1, 60],
                 	[0, 0, 1]])
mat4 = np.array([[1.5, -0.8, 60],
                 	[0.8, 1.5, -140],
                 	[0, 0, 1]])

img_aft= [ndi.affine_transform(im, mat) for mat in [mat1,mat2,mat3,mat4]]

axes[1,0].imshow(img_aft[0],cmap='gray')
axes[1,0].set_title("anh aft 1")
axes[1,0].axis(False)
axes[1,1].imshow(img_aft[1], cmap='gray')
axes[1,1].set_title("anh aft 2")
axes[1,1].axis(False)
# Excercise 4: Resampling - Lấy mẫu lại
# Xai anh aft2
x=3
print(img_aft[x].shape)
im_dn = ndi.zoom(im, zoom=0.25)
im_up = ndi.zoom(im, zoom=4.00)
axes[1,2].imshow(im_dn,cmap='gray')
axes[1,2].set_title("anh dn")
axes[1,2].axis(False)
axes[1,3].imshow(im_up, cmap='gray')
axes[1,3].set_title("anh up")
axes[1,3].axis(False)

# Excercise 5: Interpolation - Nội suy hình ảnh
up0 = ndi.zoom(img_aft[x], zoom=512/256, order=0)
up5 = ndi.zoom(img_aft[x], zoom=512/256, order=5)
axes[2,0].imshow(up0[128:256,128:256],cmap='gray')
axes[2,0].set_title("anh lv 0")
axes[2,0].axis(False)
axes[2,1].imshow(up5[128:256,128:256], cmap='gray')
axes[2,1].set_title("anh lv 5")
axes[2,1].axis(False)

# Excercise 6: Calculate volume - Tinh luu luong
# Convert binary
def convert_bin(q):
	mask=q>150
	#k=np.where(mask,1,0)
	return mask
im1 = vol[0,:,:]
im_bin1= convert_bin(im1)
im2 = vol[20,:,:]
im_bin2= convert_bin(im2)
print(im_bin1)
print(im_bin2)
# Calculate mean absolute error on all dataFrame

mean_abs_err = np.mean(np.abs(im_bin1.astype('uint8') - im_bin2.astype('uint8')))
print('MAE:', mean_abs_err)
# Calculate absolute image difference
abs_err = np.abs(im_bin1.astype('uint8') - im_bin2.astype('uint8'))
axes[2,2].imshow(abs_err)
axes[2,2].set_title("anh abs")
axes[2,2].axis(False)
plt.show()

def intersection_of_union(im1, im2):
	i = np.logical_and(im1, im2)
	u = np.logical_or(im1, im2)
	return i.sum() / u.sum()
print('Intersection of the union is:',intersection_of_union(im_bin1, im_bin2))