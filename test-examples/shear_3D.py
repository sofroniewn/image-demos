"""Test converting an image to a pyramid.
"""

import numpy as np
import napari


with napari.gui_qt():
    img = np.random.random((50, 50, 50))
    viewer = napari.view_image(img, shear=[2, 0, 0])
