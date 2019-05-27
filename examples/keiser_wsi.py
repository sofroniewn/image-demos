"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
from napari import Viewer
from napari.util import app_context


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base_name = 'data/ndcn/keiser/slides/'
slide_name = 'NA4009-02_AB'
pyramid = [da.from_zarr(base_name + slide_name + '.zarr/' + str(i))
           for i in range(8)]
print([p.shape[:2] for p in pyramid])

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    layer = viewer.add_pyramid(pyramid, name=slide_name, clim_range=[0, 255])
    camera = viewer.window.qt_viewer.view.camera
    base_shape = pyramid[0].shape
    camera.rect = (-0.1 * base_shape[1], -0.1 * base_shape[0],
                   1.2 * base_shape[1], 1.2 * base_shape[0])
