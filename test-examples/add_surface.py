"""Test converting an image to a pyramid.
"""

import numpy as np
import napari

with napari.gui_qt():
    #viewer = napari.Viewer()

    np.random.seed(0)
    # vertices = np.random.random((10, 3))
    # faces = np.random.randint(10, size=(6, 3))
    # values = np.random.random(10)
    vertices = np.random.random((10, 3))
    faces = np.random.randint(10, size=(6, 3))
    values = np.random.random(10)
    #viewer.add_surface(data)
    # vertices = np.array([[0, 0], [0, 20], [10, 0], [10, 10]])
    # faces = np.array([[0, 1, 2], [1, 2, 3]])
    # values = np.linspace(0, 1, len(vertices))

    data = (vertices, faces, values)

    viewer = napari.view_surface(data)
