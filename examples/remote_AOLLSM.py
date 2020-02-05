"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
import dask.array as da
from dask.cache import Cache
import napari

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_name = 's3://sofroniewn/image-data/LLSM/AOLLSM_m4_560nm.zarr'
data = da.from_zarr(file_name)
print(data.shape)

contrast_limits = [0, 150_000]

with napari.gui_qt(startup_logo=True):
    # create an empty viewer
    viewer = napari.view_image(data, name='AOLLSM_m4_560nm', is_pyramid=False, scale=[1, 3, 1, 1],
                contrast_limits=contrast_limits, colormap='magma', axis_labels='tzyx', title='remote')
