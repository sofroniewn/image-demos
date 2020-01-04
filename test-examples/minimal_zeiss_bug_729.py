"""
Minmal czi file example
"""
import numpy as np
import napari

data = np.random.random((10, 2, 15, 256, 256)) # works
data = np.random.random((256, 256, 1)) # works
data = np.random.random((1, 10, 2, 15, 256, 256, 1)) # crash
data = np.random.random((1, 10, 2, 15, 256, 256, 6)) # crash
data = np.random.random((6, 10, 2, 15, 256, 256, 1)) # crash

with napari.gui_qt():
    napari.view_image(data, ndisplay=3)
