"""Test converting an image to a pyramid.
"""

import numpy as np
from napari import Viewer, gui_qt
from skimage.transform import pyramid_gaussian

image = np.random.random((2000, 2000))
pyramid = list(pyramid_gaussian(image, downscale=2, multichannel=False))

print(image.shape)
print(len(pyramid))
print([p.shape for p in pyramid])

with gui_qt():
    viewer = Viewer()
    viewer.add_image(pyramid, contrast_limits=[0, 1])
