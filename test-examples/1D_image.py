import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(np.ones(10))
