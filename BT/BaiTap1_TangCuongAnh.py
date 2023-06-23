from __future__ import print_function
import imageio
import matplotlib.pyplot as plt
import time
import numpy as np
import argparse
import cv2


im=imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')
print('Tyoe',type(im))
print('Shape',im.shape)

fig, axes= plt.subplots(nrows=3, ncols=1)
axes[0].imshow(im, cmap='gray')
axes[0].axis("off")
axes[0].set_title('Ảnh DICOM gốc', size=10)

##CHUYỂN ẢNH DICOM CÓ PIXEL CÓ GIÁ TRỊ -3000 -> TỚI 0->255
## -----------CACH VAN

# a=[]
# start_time=time.time()
# for i in range(im.shape[0]):
#     for j in range(im.shape[1]):
#         im[i,j]=im[i,j]*255/2000
#         if(im[i,j])<0:
#             im[i,j]=0
#         elif(im[i,j])>=255:
#             im[i,j]=255
#         a.append(im[i,j])
# k=0
# for i in range(im.shape[0]):
#     for j in range(im.shape[1]):
#         im[i,j]=a[k]
#         k=k+1
# end_time=time.time()
# print('Seconds', end_time-start_time)
# axes[1].imshow(im, cmap='gray')
# plt.show()

## -------------CACH DUNG

start_time=time.time()
k=np.zeros(im.shape, dtype='uint8')
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        r=im[i,j]
        if r<=-1000:
            k[i,j]=r*0.005+15
        else:
            k[i,j]=r*49/600+275/3
end_time=time.time()
print('Seconds', end_time-start_time)
axes[1].imshow(k, cmap='gray')
axes[1].axis("off")
axes[1].set_title('Ảnh chuyển sang thang pixel 0-255', size=10)


# TĂNG CƯỜNG ẢNH BẰNG BIẾN ĐỔI GAMMA

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

gamma_im=adjust_gamma(k, 0.5)
axes[2].imshow(gamma_im,cmap='gray')
axes[2].axis("off")
axes[2].set_title("Ảnh được biến đổi GAMMA", size=10)
plt.show()
cv2.imwrite('output_gamma.jpg', gamma_im)



# # loop over various values of gamma
# for gamma in np.arange(0.0, 3.5, 0.5):
#     # ignore when gamma is 1 (there will be no change to the image)
#     if gamma == 1:
#         continue
#     # apply gamma correction and show the images
#     gamma = gamma if gamma > 0 else 0.1
#     adjusted = adjust_gamma(original, gamma=gamma)
#     cv2.putText(adjusted, "g={}".format(gamma), (10, 30),
#         cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
#     cv2.imshow("Images", np.hstack([original, adjusted]))
#     cv2.waitKey(0)

