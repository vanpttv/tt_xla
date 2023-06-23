import imageio
import matplotlib.pyplot as plt
import numpy

im=imageio.imread('../TAI LIEU LY THUYET/MedNIST/MedNIST/Hand/000000.jpeg')
print("Data Type:", im.dtype)
print('Min value:', im.min())
print('Max value:', im.max())
plt.subplot(2,1,1)
plt.imshow(im, cmap='gray', vmin=0, vmax=255)
plt.subplot(2,1,2)
plt.imshow(im, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()