import numpy as np

def create_mip(np_img, slices_num=15):
    ''' create the mip image from original image, slice_num
    is the number of slices for maximum intensity projection'''
    img_shape = np_img.shape
    np_mip = np.zeros(img_shape)
    for i in range(img_shape[2]):
        start = max(0, i - slices_num)
        np_mip[:, :, i] = np.amax(np_img[:, :, start:i + 1], 2)
    return np_mip[:, :, np_mip.shape[2] // 2]