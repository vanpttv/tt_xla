# Import ImageIO and load image
import imageio
im = imageio.imread('../TAI LIEU LY THUYET/dataset/dataset/Check_Vol/1-001.dcm')

# Print the available metadata fields
print('Du lieu anh dau vao', im.meta)
print('Ngay sinh banh nhan', im.meta['PatientBirthDate'])
print('Tu khoa trong kho du lieu', im.meta.keys())
