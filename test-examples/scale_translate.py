"""Test converting an image to a pyramid.
"""

import numpy as np
import napari


with napari.gui_qt():
    img = np.random.random((28, 28))
    viewer = napari.view_image(img, scale=[2, 1], translate=[30, 0])
    print('shape: ', img.shape)
    print(viewer.dims.range)
    print(viewer.layers[0].shape)
    print(viewer.layers[0].data.shape)
