"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
import dask.array as da

# file_name = 'data/LLSM/AOLLSM_m4_560nm-3D.zarr'
# file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
# data = da.from_zarr(file_name).transpose((1, 0, 2, 3))

data = np.random.random((2, 200, 200, 200))

# Downsample data
# data = data[:, ::2, ::6, ::8]
# data = data[:, ::2, ::2, ::2]
print(data.shape)

contrast_limits = [0, 200_000]

# create an empty viewer
viewer = napari.Viewer()
layer = viewer.add_image(data, name='AOLLSM_m4_560nm',
                            contrast_limits=contrast_limits, colormap='magma')
napari.run()
