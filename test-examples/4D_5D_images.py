"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():

    viewer = napari.view(np.random.random((2, 6, 30, 40)))

    viewer.add_image(np.random.random((4, 4, 5, 30, 40)))
