"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread
import numpy as np
from napari import Viewer, gui_qt

cells = imread('data/cells/cells.tif')
cells[470:, 320:, :] = cells[470, 320, :]
centers = np.loadtxt('data/cells/cells_centers.csv', delimiter=',')
shapes = np.load('data/cells/cells_boundaries.npy')
face_colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'white']

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add and color the membrane
    membrane = viewer.add_image(cells[:, :, 0], name='membrane', colormap='magenta', clim = [0.0, 255.0], blending='additive')

    # add and color the cytoplasm
    cytoplasm = viewer.add_image(cells[:, :, 1], name='cytoplasm', clim=[0.0, 255.0], colormap='yellow', blending='additive')

    # add and color the nucleus
    nucleus = viewer.add_image(cells[:, :, 2], name='nucleus', clim=[0.0, 255.0], colormap='cyan', blending='additive')

    boundaries_layer = viewer.add_shapes(shapes, shape_type='polygon',
                                         face_color=face_colors,
                                         name='boundaries', visible=False)


    centers_layer = viewer.add_points(centers, name='nuclei centers', size=20, edge_width=0, face_color='blue', opacity=0.75, visible=False)

# centers = centers_layer.data
# np.savetxt('data/cells/cells_centers.csv', centers, delimiter=',')
#
# shapes = boundaries_layer.data
# np.save('data/cells/cells_boundaries.npy', shapes)
