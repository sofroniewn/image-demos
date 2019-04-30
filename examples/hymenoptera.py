"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from dask_image.imread import imread
from dask.cache import Cache
from napari import ViewerApp
from napari.util import app_context

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

dir_ants = 'data/hymenoptera/train/ants/'
dir_bees = 'data/hymenoptera/train/bees/'

ants = imread(dir_ants + '*.jpg')
bees = imread(dir_bees + '*.jpg')

print(ants.shape)
print(bees.shape)

offset = max(ants.shape[2], bees.shape[2]) + 20

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the images
    ant_layer = viewer.add_image(ants, name='ants')
    bee_layer = viewer.add_image(bees, name='bees')

    bee_layer.translate = [offset, 0]
    viewer.camera.set_range((0, 2*offset), (0, offset))
