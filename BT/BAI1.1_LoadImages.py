# Import ImageIO
import imageio

# Load "chest-220.dcm"
im = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)
