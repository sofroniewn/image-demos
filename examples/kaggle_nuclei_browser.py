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

base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'

images = imread(base_name + '/images/image_gray.tif')
labels = imread(base_name + '/labels/label.tif')

print(images.shape)

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the images
    image_layer = viewer.add_image(images, name='nuceli', clim_range=(0, 255))
    image_layer.colormap = 'gray'
    labels_layer = viewer.add_labels(labels, name='labels', opacity=0.5)
