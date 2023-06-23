import imageio
import matplotlib.pyplot as plt
# Import SciPy's "ndimage" module
import scipy.ndimage as ndi

im=imageio.imread('../TAI LIEU LY THUYET/MedNIST/MedNIST/Hand/000000.jpeg')
# Create a histogram, binned at each possible value
hist=ndi.histogram(im, min=0, max=255, bins=256)

print(hist.shape)

cdf=hist.cumsum()/hist.sum()
print(cdf.shape)

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(hist, label='Histogram')
axes[0].set_title('Histogram')
axes[1].plot(cdf, label='CDF')
axes[1].set_title('CDF')
plt.show()

