import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


def intersection_of_union(im1, im2):
    i = np.logical_and(im1, im2)
    u = np.logical_or(im1, im2)
    return i.sum() / u.sum()


vol = imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")
im1 = vol[19, :, :]
# xfm = ndi.shift(im1, (-10, -10))
# im2 = ndi.rotate(xfm, angle=15, reshape=False)
im2 = vol[1, :, :]

iou = intersection_of_union(im1, im2)
print("Intersection of the union: ", iou)

plt.subplot(1, 2, 1)
plt.imshow(im1, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(im2, cmap='gray')
plt.show()