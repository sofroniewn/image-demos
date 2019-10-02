"""Test converting an image to a pyramid.
"""

import numpy as np
from skimage.transform import pyramid_gaussian
import napari

img = np.random.random((1000, 1000))
pyramid = list(pyramid_gaussian(img, multichannel=False))

print(img.shape, img.min(), img.max())
print(len(pyramid))
print([p.shape for p in pyramid])

with napari.gui_qt():
    viewer = napari.view_image(pyramid)
