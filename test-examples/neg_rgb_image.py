"""
Test adding an image with a range one dimensions.

There should be no slider shown for the axis corresponding to the range
one dimension.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():
    np.random.seed(0)
    # image = 2 * np.random.random((20, 20, 3)) - 1.0
    image = 20 * np.random.random((20, 20, 3)) - 10
    print(image.min(), image.max())
    image = np.clip(image, 0, 1)
    viewer = napari.view(image)
