"""
Displays an MRI volume
"""

from napari import Viewer, gui_qt
import numpy as np
import dask.array as da
from dask.cache import Cache

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_name = 'data/MRI/synthesized_FLASH25_pyr.zarr'

mri = np.asarray(da.from_zarr(file_name + '/' + str(3)))
mri[mri < 10] = 10
mri = mri - 10

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_volume(mri, name='mri', colormap='gray')
