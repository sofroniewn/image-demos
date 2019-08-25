"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import Viewer, gui_qt
import zarr

file_name = '/Volumes/Samsung_T5/data/LLSM/AOLLSM_m4_560nm.zarr'
data = zarr.open(file_name, mode='r')
print(data.shape)

clim_range = [0, 150_000]

with gui_qt():
    # create an empty viewer
    viewer = Viewer()
    layer = viewer.add_image(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range=clim_range, colormap='magma')
