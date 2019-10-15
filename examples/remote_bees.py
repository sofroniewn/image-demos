"""
Dynamically load irregularly shapes images of bees from s3
"""

import numpy as np
from dask_image.imread import imread
from dask.cache import Cache
from napari import Viewer, gui_qt

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

dir_bees = 's3://sofroniewn/image-data/bees/'
bees = imread(dir_bees + '*.jpg')
print(bees.shape)


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    viewer.add_image(ants, name='ants', contrast_limits=[0, 255])
