"""Test converting an image to a pyramid.
"""

import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.view_image(np.random.random((200, 50)))
