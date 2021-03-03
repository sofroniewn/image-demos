"""
Display raw and sheared
"""
import napari
import numpy as np


class MyPoints(napari.layers.Points):
    def random_function():
        return 42


with napari.gui_qt():
    viewer = napari.view_image(np.random.random((10, 10)))

    points = MyPoints()
    viewer.layers.append(points)
