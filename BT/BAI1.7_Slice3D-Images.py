import imageio
import matplotlib.pyplot as plt

vol=imageio.volread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol', 'DICOM')

# Plot the images on a subplots array
fig, axes= plt.subplots(nrows=1, ncols=4)

# Loop through subplots and draw image
for i in range(4):
    im=vol[i, :, :]
    axes[i].imshow(im, cmap='gray')
    axes[i].axis('off')
plt.show()