"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():
    axis_labels= ['t', 'z', 'y', 'x']
    viewer = napari.view_image(np.random.random((10, 6, 30, 40)), axis_labels=axis_labels)
