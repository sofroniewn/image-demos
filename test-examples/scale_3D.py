"""Test converting an image to a pyramid.
"""

import numpy as np
import napari


with napari.gui_qt():
    img = np.random.random((50, 128, 128))
    viewer = napari.view_image(img, scale=[1.25, 1, 1])
    print('shape: ', img.shape)
    print(viewer.dims.range)
    print(viewer.layers[0].shape)
    print(viewer.layers[0].data.shape)
