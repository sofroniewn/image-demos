"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""


import napari
import numpy as np


with napari.gui_qt():
    scale = (1, 209.9999999999999, 77.52248561765859, 77.52248561765859)
    viewer = napari.Viewer()
    image = np.random.random((1, 2, 100, 100))
    viewer.add_image(image, scale=(1, 100, 1, 1))

