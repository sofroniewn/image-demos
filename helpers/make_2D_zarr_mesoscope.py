import numpy as np
from glob import glob
from skimage.io import imread
import zarr


image = imread('data/mesoscope/anatomical/plane.tif')[0]


file_name = 'data/mesoscope/anatomical/plane.zarr'
### For one file
# shape = (768, 1024, 201)
# z1 = zarr.open(file_name, mode='w', shape=shape, chunks=(None, None, 10), dtype='f4')
# z1[:] = imread(image_files[0]).transpose(2, 1, 0)

### For many files
shape = image.shape
print(shape)
z1 = zarr.open(file_name, mode='w', shape=shape, chunks=(512, 512), dtype='f4')
z1[:] = image
