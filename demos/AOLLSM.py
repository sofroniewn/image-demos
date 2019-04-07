"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import ViewerApp
from napari.util import app_context
# from dask_image.imread import imread
import dask.array as da


file_name = '/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm-6.zarr'

data = da.from_zarr(file_name)
print(data.shape)


# data = da.stack([imread(f, nframes=-1) for f in image_files], axis=-1)
# print(data.shape)
# data = np.random.rand(2**14, 2**14)

clim_range = [0, 150_000]
# clim_range = [0, 1.0]

with app_context():
    # create an empty viewer
    viewer = ViewerApp()
    layer = viewer.add_image(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range=clim_range)
