"""
Display one shapes layer ontop of one image layer using the add_shapes and
add_image APIs. When the window is closed it will print the coordinates of
your shapes.
"""

import numpy as np
import napari


with napari.gui_qt():
    path = [[505, 60], [402, 71], [383, 42], [251, 95], [212, 59],
            [131, 137], [126, 187], [191, 204], [171, 248], [211, 260],
            [273, 243], [264, 225], [430, 173], [512, 160]]
    polygons = [path] + [[list(c), [10, 10]] for c in path]
    shape_type  = ['path'] + ['ellipse'] * len(path)
    edge_colors = np.random.random((len(polygons), 4))
    napari.view_shapes(polygons, shape_type=shape_type, edge_width=5, opacity=1,
                              edge_color=edge_colors, face_color='royalblue')
