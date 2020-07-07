"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
from skimage import data
import napari
import logging
import sys


logger = logging.getLogger('napari.layers.base.layer_event_handler')
logger.setLevel(logging.DEBUG)


camera = data.camera()
moon = data.moon()

with napari.gui_qt():
    # add the image
    viewer = napari.Viewer()
    #sys.setrecursionlimit(100)
    viewer.add_image(camera)
    viewer.add_image(camera)
