"""
Test adding an image with a range one dimensions.

There should be no slider shown for the axis corresponding to the range
one dimension.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():

    viewer = napari.view_image(np.random.random((20, 100, 200)), axis_labels=['a very long label', 'y', 'x'])
