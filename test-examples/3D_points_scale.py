import napari
import numpy as np


with napari.gui_qt():
    v = napari.view_image(np.random.random((10, 20, 20)), scale=(5, 3, 1))
    points = np.array([[10, 10, 0], [8, 12, 5], [4, 11, 2]])
    v.add_points(points, scale=(5, 3, 1))