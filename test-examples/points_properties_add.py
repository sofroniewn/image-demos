"""
Displays points with properties
"""

import napari
import numpy as np


with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((5, 400, 400)))

    points = np.array([[100, 100], [200, 200], [333, 111]])

    # create properties for each point
    properties = {
        'class': np.array([1, 2, 3]),
    }

    # define the color cycle for the face_color annotation
    face_color_cycle = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']

    points_layer = viewer.add_points(
        points,
        properties=properties,
        size=10,
        edge_width=1,
        edge_color='white',
        face_color='class',
        face_color_cycle=face_color_cycle,
        name='points'
    )
