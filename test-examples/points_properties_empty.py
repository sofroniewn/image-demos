"""
Displays empty points with properties
"""

import napari
import numpy as np


with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((5, 400, 400)))

    # create properties for each point
    properties = {
        'class': np.array([]),
    }

    # define the color cycle for the face_color annotation
    face_color_cycle = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']

    points_layer = viewer.add_points(
        properties=properties,
        size=10,
        edge_width=1,
        edge_color='white',
        face_color='class',
        face_color_cycle=face_color_cycle,
        name='points'
    )
