import numpy as np
import napari

data = np.random.random((10, 10, 10))
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(data, scale=[2, 1, 1], translate=[10, 15, 20], shear=[[1, 0, 0], [0, 1, 0], [10, 0, 1]])
