"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import Viewer, gui_qt
import zarr

file_name = 'data/LLSM/AOLLSM_m4_560nm-3D.zarr'
data = zarr.open(file_name, mode='r')
print(data.shape)

clim_range = [0, 200_000]

with gui_qt():
    # create an empty viewer
    viewer = Viewer()
    layer = viewer.add_volume(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range=clim_range, colormap='magma')
