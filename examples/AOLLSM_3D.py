"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import Viewer, gui_qt
import dask.array as da

file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
data = da.from_zarr(file_name).transpose((1, 0, 2, 3))[:, ::4, ::4, ::4]
print(data.shape)

clim_range = [0, 150_000]

with gui_qt():
    # create an empty viewer
    viewer = Viewer()
    layer = viewer.add_volume(data, multichannel=False, name='AOLLSM_m4_560nm',
                             clim_range=clim_range, colormap='magma')
