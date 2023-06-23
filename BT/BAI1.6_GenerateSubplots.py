# Import PyPlot
import imageio
import matplotlib.pyplot as plt

# Initialize figure and axes grid
fig, axes  = plt.subplots(nrows=2, ncols=1)

# Draw an image on each subplot
im1 = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')
axes[0].imshow(im1, cmap='gray')

im2 = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-002.dcm')
axes[1].imshow(im2, cmap='gray')

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()

