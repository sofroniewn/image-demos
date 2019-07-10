"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from dask_image.imread import imread
from dask.cache import Cache
from napari import Viewer, gui_qt

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'

images = imread(base_name + '/images/image_gray.tif')
labels = imread(base_name + '/labels/label.tif')

print(images.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    image_layer = viewer.add_image(images, name='nuceli', clim_range=(0, 255), colormap='gray')
    labels_layer = viewer.add_labels(labels, name='labels', opacity=0.5)
