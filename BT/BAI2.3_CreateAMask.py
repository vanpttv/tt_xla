import scipy.ndimage as ndi
import imageio
import matplotlib.pyplot as plt

im=imageio.imread('../TAI LIEU LY THUYET/MedNIST/MedNIST/Hand/000000.jpeg')

# Create skin and bone masks
mask_bone=im>=145
mask_skin=(im>=45) & (im<145)

# Plot the skin (0) and bone (1) masks

fig, axes = plt.subplots(1,3)
axes[0].imshow(im, cmap='gray')
axes[1].imshow(mask_bone, cmap='gray')
axes[2].imshow(mask_skin, cmap='gray')

plt.show()

