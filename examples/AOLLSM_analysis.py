"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
import dask.array as da
from skimage import filters

file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
data = da.from_zarr(file_name)


with napari.gui_qt():
    viewer = napari.Viewer(axis_labels='tzyx')
    viewer.add_image(data, name='AOLLSM_m4_560nm', multiscale=False, scale=[1, 3, 1, 1],
                contrast_limits=[0, 150_000], colormap='magma')
    viewer.add_image(data.map_blocks(filters.sobel), name='sobel', scale=[1, 3, 1, 1],
                contrast_limits=[0, 10_000], visible=False)