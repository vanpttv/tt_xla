# Import ImageIO and PyPlot
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')

# Draw the image in grayscale
plt.subplot(2, 1, 1)
plt.imshow(im, cmap='gray')

# Draw the image with greater contrast
plt.subplot(2, 1, 2)
plt.imshow(im, cmap='gray', vmin=-200, vmax=200)
plt.axis('off')
plt.show()
