"""Test converting an image to a multiscale.
"""

import numpy as np
import napari

img = np.random.random((20_000, 20_000))
# img = np.random.random((20_000, 200))
# img = np.random.random((10, 100, 2500))
print('shape: ', img.shape)

with napari.gui_qt():
    viewer = napari.view_image(img, ndisplay=2, is_multiscale=False)
