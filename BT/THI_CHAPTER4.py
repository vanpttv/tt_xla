import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage import color
from skimage import io

im1_goc = imageio.imread('../CUOI KY/image1.jpg')
im2_goc = imageio.imread('../CUOI KY/image2.jpg')
im1 = color.rgb2gray(io.imread('../CUOI KY/image1.jpg'))
im2 = color.rgb2gray(io.imread('../CUOI KY/image2.jpg'))
img = io.imread('../CUOI KY/image1.jpg', as_gray=True)
plt.figure()
plt.subplot(2,2,1)
plt.imshow(im1_goc)
plt.title("Ảnh REF màu")
plt.subplot(2,2,2)
plt.imshow(im2_goc, cmap='gray')
plt.title("Ảnh test màu")

plt.subplot(2,2,3)
plt.imshow(im1, cmap='gray')
plt.colorbar()
plt.title("Ảnh REF chuyển sang ảnh xám")
plt.subplot(2,2,4)
plt.imshow(im2, cmap='gray')
plt.colorbar()
plt.title("Ảnh test chuyển sang ảnh xám")


image1=np.zeros(im1.shape, dtype='uint8')
image2=np.zeros(im1.shape, dtype='uint8')
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
plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(image1,cmap='gray')
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(image2,cmap='gray')
plt.colorbar()

# a: Tinh ERR RAW
# Convert binary
def convert_bin(q):
    mask=q>100
    return mask
im_bin1= convert_bin(image1)
im_bin2= convert_bin(image2)

# Calculate absolute image difference
abs_err = np.absolute(im_bin1.astype('int') - im_bin2.astype('int'))

# Calculate mean absolute error
mean_abs_err = np.mean(np.abs(im_bin1.astype('int') - im_bin2.astype('int')))
print('MAE:', mean_abs_err)

# plt.figure(3)
# plt.subplot(1,3,1)
# plt.imshow(im_bin1, cmap="gray")
# plt.colorbar()
# plt.subplot(1,3,2)
# plt.imshow(im_bin2, cmap='gray')
# plt.colorbar()
# plt.subplot(1,3,3)
# plt.imshow(abs_err, cmap='gray')
# plt.colorbar()

# b: Tim tam va dich
mask1 = np.where(image1>100, 1, 0)
# Label the objects in "mask"
labels1, nlabels1 = ndi.label(mask1)
print('Num. Labels:', nlabels1)
# Find image center of mass
com1 = ndi.center_of_mass(labels1, labels1, index=1)
print(com1[0], com1[1])

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

im_trans = ndi.shift(image2, shift=(d02, d12))
mask = np.where(im_trans>100, 1, 0)
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)
com = ndi.center_of_mass(labels, labels, index=1)

print(com[0], com[1])

# plt.figure(4)
# plt.imshow(labels2, cmap='rainbow')
# plt.colorbar()
# plt.title("Ảnh Label")
# plt.figure(5)
# plt.imshow(im_trans, cmap='gray')
# plt.colorbar()
# plt.title("Ảnh dịch tâm")

im_bin2_l2= convert_bin(im_trans)

# Calculate absolute image difference
abs_err_l2 = np.absolute(im_bin1.astype('int') - im_bin2_l2.astype('int'))

# Calculate mean absolute error
mean_abs_err_l2 = np.mean(np.abs(im_bin1.astype('int') - im_bin2_l2.astype('int')))
print('MAE:', mean_abs_err_l2)

# plt.figure(5)
# plt.subplot(1,3,1)
# plt.imshow(im_bin1, cmap="gray")
# plt.colorbar()
# plt.subplot(1,3,2)
# plt.imshow(im_bin2_l2, cmap='gray')
# plt.colorbar()
# plt.subplot(1,3,3)
# plt.imshow(abs_err_l2, cmap='gray')
# plt.colorbar()

# c. Chay for de xoay theo chieu kim dong ho moi lan 1 do
# mae=[]
# for i in range(360):
#     im_ro = ndi.rotate(im_trans, angle=-i, reshape=False)
#     im_bin2_new = convert_bin(im_ro)
#     mean_abs_err_l2 = np.mean(np.abs(im_bin1.astype('int') - im_bin2_new.astype('int')))
#     mae.append(mean_abs_err_l2)
#     print('MAE:',[i, mean_abs_err_l2])
# print([min(mae),mae.index(min(mae))])
plt.show()