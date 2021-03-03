"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
import napari


with napari.gui_qt():
    # add the image
    viewer = napari.Viewer()
    
    layer = viewer.add_points([0,0])
    viewer.layers.remove(layer)
    viewer.layers.append(layer)
