"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():

    viewer = napari.view_labels(np.random.randint(10, size=(1024, 1024)))
