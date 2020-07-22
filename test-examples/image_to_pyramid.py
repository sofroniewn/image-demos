"""Test converting an image to a pyramid.
"""

import numpy as np
import napari
from skimage.transform import pyramid_gaussian

image = np.random.random((2000, 2000))
pyramid = list(pyramid_gaussian(image, downscale=2, multichannel=False))[:-4]

print(image.shape)
print(len(pyramid))
print([p.shape for p in pyramid])

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(pyramid, contrast_limits=[0, 1])
