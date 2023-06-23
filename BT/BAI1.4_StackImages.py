import imageio
import numpy as np
im1=imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')
im2=imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-002.dcm')
im3=imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-003.dcm')
print(im1.shape)
vol = np.stack([im1, im2, im3])
print('Volume dimensions:', vol.shape)

