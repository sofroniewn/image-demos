import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((2048, 2048)))
    viewer.add_labels(np.zeros((2048, 2048)))
