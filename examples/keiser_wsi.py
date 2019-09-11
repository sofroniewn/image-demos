"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
from napari import Viewer, gui_qt


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base_name = 'data-njs/ndcn/keiser/slides/'
slide_name = 'NA4009-02_AB'
pyramid = [da.from_zarr(base_name + slide_name + '.zarr/' + str(i))
           for i in range(8)]
print([p.shape[:2] for p in pyramid])

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    layer = viewer.add_pyramid(pyramid, name=slide_name, contrast_limits=[0, 255])
