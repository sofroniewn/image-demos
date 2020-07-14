import napari
import numpy as np

with napari.gui_qt():
    viewer = napari.Viewer()
    # Add images
    data = np.ones((6, 15, 15))
    viewer.add_image(data, channel_axis=0, blending='translucent')