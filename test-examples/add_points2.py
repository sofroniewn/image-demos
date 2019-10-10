"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():
    # add the image
    viewer = napari.view_image(data.astronaut(), rgb=True)
    # add the points
    points = np.array([[100, 100], [200, 200], [300, 100]])
    viewer.add_points(points, size=30)
