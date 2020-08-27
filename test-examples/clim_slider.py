"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.view_image(np.random.random((200, 200)), contrast_limits=[0, 10])
