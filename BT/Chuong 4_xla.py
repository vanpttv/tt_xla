import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("D:\HK2_2021\TT_XLA\TAI LIEU LY THUYET\SDC4201", "DICOM")

im=vol[20,:,:]
plt.figure(1)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title("Ảnh gốc")

# Excercise 1: Translation - Dịch ảnh
mask = np.where(im>400, 1, 0)
# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)
# Find image center of mass
com = ndi.center_of_mass(labels, labels, index=11)

# Calculate amount of shift needed
d0 = 128-com[0]
d1 = 128-com[1]
print(com[0], com[1], d0, d1)

# Translate the brain towards the center
im_trans = ndi.shift(im, shift=(d0, d1))

plt.figure(2)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title("Ảnh gốc")
plt.figure(3)
plt.imshow(im_trans, cmap='gray')
plt.colorbar()
plt.title("Ảnh dịch tâm")
plt.figure(4)
plt.imshow(labels, cmap='rainbow')
plt.colorbar()
plt.title("Ảnh Label")

# Excercise 2: Rotations - Xoay ảnh
# Rotate the shifted image
im_ro = ndi.rotate(im_trans, angle=-30, reshape=False)

# Plot the original and rotated images
plt.figure(5)
plt.imshow(im, cmap='gray')
plt.colorbar()
plt.title("Ảnh gốc")
plt.figure(6)
plt.imshow(im_ro, cmap='gray')
plt.colorbar()
plt.title("Ảnh xoay")

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
plt.figure(7)
plt.imshow(img_aft[0], cmap='gray')
plt.figure(8)
plt.imshow(img_aft[1], cmap='gray')
plt.figure(9)
plt.imshow(img_aft[2], cmap='gray')
plt.figure(10)
plt.imshow(img_aft[3], cmap='gray')

# Excercise 4: Resampling - Lấy mẫu lại
# Resample image
im_dn = ndi.zoom(im_trans, zoom=0.25)
im_up = ndi.zoom(im_trans,zoom=4)
plt.figure(11)
plt.imshow(im_dn, cmap='gray')
plt.figure(12)
plt.imshow(im_up, cmap='gray')

# Excercise 5: Interpolation - Nội suy hình ảnh
up0 = ndi.zoom(im, zoom=2, order=0)
up5 = ndi.zoom(im, zoom=2, order=5)
# Print original and new shape
print('Original shape:', im.shape)
print('Upsampled shape:', up0.shape, up5.shape)
print('Upsampled shape:', up0.min(), up0.max(), up5.min(), up5.max())

# Plot close-ups of the new images
plt.figure(13)
plt.imshow(im, cmap='gray')
plt.figure(14)
plt.imshow(up0[128:256, 128:256], cmap='gray')
plt.figure(15)
plt.imshow(up5[128:256, 128:256], cmap='gray')

# Exercise 6
im1=vol[13,:,:]
im2=vol[20,:,:]

# Convert binary
def convert_bin(q):
    mask=q>100
    return mask
im_bin1= convert_bin(im1)
im_bin2= convert_bin(im2)

# Calculate image difference
err = im1-im2

# Calculate absolute image difference
abs_err = np.absolute(im_bin1.astype('uint8') - im_bin2.astype('uint8'))

# Calculate mean absolute error
mean_abs_err = np.mean(np.abs(im_bin1.astype('uint8') - im_bin2.astype('uint8')))
print(err)
print('MAE:', mean_abs_err)

plt.figure(16)
plt.imshow(err, cmap="seismic")
plt.colorbar()
plt.figure(17)
plt.imshow(abs_err, cmap='gray')
plt.colorbar()

#Exercise 7: Intersection of the union - Tính IOU
def intersection_of_union(im1, im2):
    i = np.logical_and(im1, im2)
    u = np.logical_or(im1, im2)
    return i.sum() / u.sum()
iou = intersection_of_union(im1, im2)
print("Intersection of the union: ", iou)
plt.figure(18)
plt.subplot(1, 2, 1)
plt.imshow(im1, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(im2, cmap='gray')
plt.show()