"""Test converting an image to a pyramid.
"""

import numpy as np
import napari


with napari.gui_qt():
    image = np.random.random((5, 128, 128))
    labels = np.zeros((5, 128, 128))
    scale = [1, 0.16, 0.16]
    #scale = [10, 1000, 1000]
    viewer = napari.view_image(image, name='Raw', rgb=False, scale=scale) 
    label_layer = viewer.add_labels(labels, name='Label', scale=scale)