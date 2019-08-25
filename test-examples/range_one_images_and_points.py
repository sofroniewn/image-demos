"""
Test adding images with range one dimensions and points

Intially no sliders should be present as the images have range one
dimensions. On adding the points the sliders should be displayed.
"""

import numpy as np
from skimage import data
from skimage.color import rgb2gray
import napari


with napari.gui_qt():
    # create the viewer window
    viewer = napari.Viewer()

    data = np.random.random((1, 1, 1, 100, 200))
    viewer.add_image(data)

    points = np.floor(5 * np.random.random((1000, 5))).astype(int)
    points[:, -2:] = 20 * points[:, -2:]
    viewer.add_points(points)
