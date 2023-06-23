import scipy.ndimage as ndi
import imageio
import matplotlib.pyplot as plt
import numpy as np

im=imageio.imread('../TAI LIEU LY THUYET/MedNIST/MedNIST/Hand/000000.jpeg')
hist=ndi.histogram(im, min=1, max=255, bins=255)
mask_bone=im>=145
mask_skin=(im>=45) & (im<145)

im_bone = np.where(mask_bone, im, 0)
im_skin = np.where(mask_skin, im, 0)

fig, axes=plt.subplots(nrows=3, ncols=2)
axes[0,0].imshow(im, cmap='gray')
axes[0,1].plot(hist)
axes[1,0].imshow(mask_bone, cmap='gray')
axes[1,1].imshow(mask_skin, cmap='gray')
axes[2,0].imshow(im_bone, cmap='gray')
axes[2,1].imshow(im_skin, cmap='gray')
plt.show()


