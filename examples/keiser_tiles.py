"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from dask_image.imread import imread
from dask.cache import Cache
from napari import Viewer
from napari.util import app_context


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base_dir = 'data/ndcn/keiser/tiles/'
slide_name = 'NA4009-02_AB'

tiles = imread(base_dir + slide_name + '/*.jpg')
print(tiles.shape)

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    layer = viewer.add_image(tiles, name=slide_name, clim_range=[0, 255])
