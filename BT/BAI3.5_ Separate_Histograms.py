import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

vol=imageio.volread("../TAI LIEU LY THUYET/SDC4201", "DICOM")

# # Smooth intensity values
# vol_filt=ndi.median_filter(vol,size=3)
#
# # Select high-intensity pixels
# mask_start = np.where(vol_filt>450, 1, 0)
# mask = ndi.binary_closing(mask_start)
#
# # Label the objects in "mask"
# labels, nlabels = ndi.label(mask)
# print('Num. Labels:', nlabels)
#
# # Create histograms for selected pixels
# hist1 = ndi.histogram(vol, min=0, max=255, bins=256)
# hist2 = ndi.histogram(vol, 0, 255, 256, labels=labels)
# hist3 = ndi.histogram(vol, 0, 255, 256, labels=labels, index=1)

# Plot the histogram density
# plt.figure(1)
# plt.plot(hist1.cumsum()/hist1.sum(), label='All pixels')
# plt.figure(2)
# plt.plot(hist2.cumsum()/hist2.sum(), label='All labeled pixels')
# plt.figure(3)
# plt.plot(hist3.cumsum()/hist3.sum(), label='Left ventricle')
# plt.show()


for j in range( vol.shape[0]):
    img = vol[j,:,:]
    labels,nlabels = ndi.label(img)
    # Tạo biểu đồ cho các pixel đã chọn
    hist1 = ndi.histogram(img, min=1, max=1049, bins=256)
    hist2 = ndi.histogram(img, 1, 255, 256, labels=labels)
    hist3 = ndi.histogram(img, 1, 255, 256, labels=labels, index=1)
    plt.figure(1)
    # Vẽ biểu đồ mật độ
    plt.plot(hist1 / hist1.sum(), label='All pixels')
    plt.plot(hist2 / hist2.sum(), label='All labeled pixels')
    plt.plot(hist3 / hist3.sum(), label='Left ventricle')
    plt.title('Number' + str(j))
    plt.pause(0.005)
    plt.clf()


