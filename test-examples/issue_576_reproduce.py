"""
Issue 576
"""

import napari
import numpy as np


vol = np.random.random((68, 296, 393)).astype(np.float64)

with napari.gui_qt():
    viewer = napari.view_image(vol, ndisplay=3)
