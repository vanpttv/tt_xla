# Import ImageIO
import  imageio
import matplotlib.pyplot as plt

# Load the "tcia-chest-ct" directory
vol = imageio.volread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol', 'DICOM')

# Print image attributes
print('Available metadata:', vol.meta.keys())
print('Study Date:', vol.meta['StudyDate'])
n0, n1, n2 = vol.shape
d0, d1, d2 = vol.meta['sampling']
print(n2, d2)
print('Shape of image array:', vol.shape)

for i in range (vol.shape[0]):
    plt.imshow(vol[i,:,:], cmap='gray')
    plt.pause(0.005)
