"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
import napari
import logging



logger = logging.getLogger('napari.layers.base.layer_event_handler')
logger.setLevel(logging.DEBUG)


with napari.gui_qt():
    # add the image
    viewer = napari.Viewer()
    data = np.random.random((10, 30, 40))
    viewer.add_image(data)
    viewer.layers[0].data = data[0]
 
    # assert len(viewer.layers) == 1
    # assert viewer.dims.ndim == 2
    # assert view.dims.nsliders == viewer.dims.ndim
    # assert np.sum(view.dims._displayed_sliders) == 0
