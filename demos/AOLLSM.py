"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import ViewerApp
from napari.util import app_context
import zarr

file = 'data/LLSM/AOLLSM_m4_560nm.zarr'
data = zarr.open(file, mode='r')
print(data.shape)

clim_range = [0, 150_000]

with app_context():
    # create an empty viewer
    viewer = ViewerApp()
    layer = viewer.add_image(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range=clim_range)
