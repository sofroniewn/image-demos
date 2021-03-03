"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
import napari


with napari.gui_qt():
    image = np.random.random((10, 10))
    imlayer = napari.layers.Image(image)
    v1 = napari.Viewer()
    v1.add_layer(imlayer)
    v2 = napari.Viewer()
    v2.add_layer(imlayer)