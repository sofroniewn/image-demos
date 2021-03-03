"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():

    viewer = napari.view_image(np.random.random((5, 6, 5, 30, 40)), channel_axis=0)
    #viewer.window._qt_window.showNormal()
    viewer.window._qt_window.showFullScreen()