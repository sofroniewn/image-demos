"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

import numpy as np
from napari import ViewerApp
from napari.util import app_context
from vispy.color import Colormap
#from dask_image.imread import imread
import dask.array as da


file_name = '/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm-5.zarr'

data = da.from_zarr(file_name) #.transpose(3, 2, 1, 0)
print(data.shape)

#
# # data = da.stack([imread(f, nframes=-1) for f in image_files], axis=-1)
# # print(data.shape)
#

# data = np.random.rand(16000, 16000)
#
clim_range_default = [0, 150_000]

with app_context():
    # create an empty viewer
    viewer = ViewerApp()
    layer = viewer.add_image(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range_default=clim_range_default)
