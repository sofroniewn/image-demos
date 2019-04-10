"""
Image pyramid of pathology slide
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
from napari import ViewerApp
from napari.util import app_context

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_name = 'data/camelyon16/normal_001.zarr'

pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

print([p.shape[:2] for p in pyramid])

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the pyramid
    layer = viewer.add_pyramid(pyramid, name='slide')
    #shape = np.array(pyramid[0].shape[:2])
    #viewer.camera.zoom(.1, center=-shape/2)
