import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im=vol[20,:,:]
print(im.shape)

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
xfm1 = ndi.affine_transform(im, mat1)
xfm2 = ndi.affine_transform(im, mat2)
xfm3 = ndi.affine_transform(im, mat3)
xfm4 = ndi.affine_transform(im, mat4)

plt.imshow(im, cmap='gray')
fig, axes = plt.subplots(1, 4)
axes[0].imshow(xfm1, cmap='gray')
axes[1].imshow(xfm2, cmap='gray')
axes[2].imshow(xfm3, cmap='gray')
axes[3].imshow(xfm4, cmap='gray')
plt.show()
