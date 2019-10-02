import numpy as np
from glob import glob
from skimage.io import imread
import zarr
from scipy.ndimage import zoom


file_name = 'data/mesospim/ExpA_VIP_ASLM_on.tif'
print('loading tif')
data = imread(file_name)
print('tif loaded')
print(data.shape)

file_name_2 = 'data/mesospim/ExpA_VIP_ASLM_on.zarr'

root = zarr.open_group(file_name_2, mode='a')
print('init')

for i in range(0, 6):
    print(i, 6, data.shape)
    z1 = root.create_dataset(str(i), shape=data.shape, chunks=(64, 64, 64),
                             dtype=np.uint16)
    z1[:] = data
    print('shrinking')
    data = zoom(data, 0.5)
