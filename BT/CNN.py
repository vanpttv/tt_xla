import numpy as np
import os
import time
# %matplotlib inline
import matplotlib.pyplot as mp
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as om
import torchvision as tv
import torch.utils.data as dat


if torch.cuda.is_available():     # Lựa chọn phần cứng huấn luyện là GPU nếu có thể
    dev = torch.device("cuda:0")
    kwar = {'num_workers': 8, 'pin_memory': True}
    cpu = torch.device("cpu")
else:
    print("Warning: CUDA not found, CPU only.")
    dev = torch.device("cpu")
    kwar = {}
    cpu = torch.device("cpu")

np.random.seed(551)


dataDir = 'MedNist '               # The main data directory
classNames = os.listdir(dataDir)  # Each type of image can be found in its own subdirectory
classNames= [ x for x in classNames if x!= '.DS_Store']
numClass = len(classNames)        # Số lượng class = số lượng của của thư mục con
imageFiles = [[os.path.join(dataDir,classNames[i],x) for x in os.listdir(os.path.join(dataDir,classNames[i]))]
              for i in range(numClass)]                     # Danh sách tên của các file trong dữ liệu
numEach = [len(imageFiles[i]) for i in range(numClass)]     # Số lượng mẫu cho từng class
imageFilesList = []               # Tạo một danh sách rỗng dùng để chứa tên các file ảnh
imageClass = []                   # Tạo một danh sách rỗng dùng để chứa tên các class
for i in range(numClass):
    imageFilesList.extend(imageFiles[i])
    imageClass.extend([i]*numEach[i])
numTotal = len(imageClass)        # Tổng số ảnh trong dữ liệu
imageWidth, imageHeight = Image.open(imageFilesList[0]).size         # Kích thước mỗi ảnh
print("There are",numTotal,"images in",numClass,"distinct categories")
print("Label names:",classNames)
print("Label counts:",numEach)
print("Image dimensions:",imageWidth,"x",imageHeight)

mp.subplots(3,3,figsize=(8,8))
for i,k in enumerate(np.random.randint(numTotal, size=9)):  # Lấy ngẫu nhiên 9 ảnh
    im = Image.open(imageFilesList[k])                      #      và hiển thị chúng cùng với nhãn
    arr = np.array(im)
    mp.subplot(3,3,i+1)
    mp.xlabel(classNames[imageClass[k]])
    mp.imshow(arr,cmap='gray',vmin=0,vmax=255)
mp.tight_layout()
mp.show()

toTensor = tv.transforms.ToTensor()
def scaleImage(x):          # đưa vào một ảnh đoc từ thư viện PIL, trả về một tensor
    y = toTensor(x)
    if(y.min() < y.max()):  # Giả sử ảnh không rỗng, chuẩn hoá dữ liệu vào khoảng [0 - 1]
        y = (y - y.min())/(y.max() - y.min())
    z = y - y.mean()        # Đảm bảo dữ liệu mới có trị trung bình bằng 0
    return z


