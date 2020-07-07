"""Test converting an image to a pyramid.
"""

import os 
import numpy as np
os.environ["NAPARI_PERFMON"] = "1"

import napari



points = np.random.randint(100, size=(1000, 2))

with napari.gui_qt():
    viewer = napari.view_points(points, face_color='red')
