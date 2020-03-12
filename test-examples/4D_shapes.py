"""
Display one shapes layer ontop of one image layer using the add_shapes and
add_image APIs. When the window is closed it will print the coordinates of
your shapes.
"""

import numpy as np
import napari


# create some random 4D data
data = np.random.rand(10, 20, 256, 256)

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(data)

    # generate ellipse in centre of data for all data slices (radius=20)
    # bbox = [[108, 108], [108, 148], [148, 148], [148, 108]]
    # viewer.add_shapes(bbox, shape_type='ellipse') # <--- works fine, shape is persistent throughout all layers

#    bbox = [[3, 108, 108], [3, 108, 148], [3, 148, 148], [3, 148, 108]]
    bbox = [[3, 5, 108, 108], [3, 5, 108, 148], [3, 5, 148, 148], [3, 5, 148, 108]]
    viewer.add_shapes(bbox, shape_type='ellipse') # <--- does not work, produces AxisError
