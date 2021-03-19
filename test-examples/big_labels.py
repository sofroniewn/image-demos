import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_labels(np.ones((2048, 2048)).astype(int))
