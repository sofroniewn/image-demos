"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

import numpy as np
from napari import ViewerApp
from napari.util import app_context
from vispy.color import Colormap
from skimage.io import imread
#from dask_image.imread import imread
import dask.array as da
from glob import glob
import zarr


# image_path = '/Volumes/GoogleDrive/My Drive/d/'
# image_file = 'ex6-2_CamA_ch1_CAM1_stack*_560nm_*Abs_000x_000y_000z_0000t_decon.tif'
# image_files = glob(image_path + image_file)
#
# shape = (len(image_files), 201, 1024, 768)
#
#
# z1 = zarr.open('/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm.zarr',
#                mode='w', shape=shape, chunks=(1, 201, 1024, 768), dtype='f4')
#
# for i, f in enumerate(image_files):
#     print(i)
#     z1[i] = imread(f)

data = da.from_zarr('/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm.zarr').transpose(3, 2, 1, 0)
print(data.shape)

# data = da.stack([imread(f, nframes=-1) for f in image_files], axis=-1)
# print(data.shape)

with app_context():
    # create an empty viewer
    viewer = ViewerApp()
    #viewer.add_image(np.asarray(data[:, :, :, 0]))
    viewer.add_image(data)
