"""Test converting an image to a pyramid.
"""

import numpy as np
import napari

points = np.random.randint(100, size=(1000, 2))

with napari.gui_qt():
    viewer = napari.view_points(points, face_color='red')
