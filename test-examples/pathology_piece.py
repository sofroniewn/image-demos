"""
Image pyramid of pathology slide
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
import xml.etree.ElementTree as ET
from napari import Viewer, gui_qt

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

print('getting slice')
pyr = np.asarray(pyramid[0][:20_000, :2_000])
#pyr = np.random.random((20_000, 20_000))
print(pyr.shape[:2])

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the pyramid
    layer = viewer.add_image(pyr, name='slide')
