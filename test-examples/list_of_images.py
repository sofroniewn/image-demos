"""
Test adding list of images
"""

import numpy as np
from skimage import data
import napari
list_of_images = [data.astronaut(), data.clock(), data.coins(), data.binary_blobs(length=50,n_dim=3)]


with napari.gui_qt():
    axis_labels= ['t', 'z', 'y', 'x']
    viewer = napari.view_image(np.random.random((10, 6, 30, 40)), axis_labels=axis_labels)
