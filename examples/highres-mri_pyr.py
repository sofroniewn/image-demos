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

mri = [da.from_zarr(file_name + '/' + str(i))
           for i in range(6)]
print([p.shape for p in mri])

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_pyramid(mri, name='mri', colormap='gray', contrast_limits=[0, 50])
    viewer.dims.order = [0, 2, 1]

    @viewer.bind_key('s')
    def swap(viewer):
        """Swaps dims
        """
        viewer.dims.order = np.roll(viewer.dims.order, 1)
