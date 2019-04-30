"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread
import numpy as np
from napari import ViewerApp
from napari.util import app_context
from vispy.color import Colormap

cells = imread('data/cells/cells.tif')
cells[470:, 320:, :] = cells[470, 320, :]
centers = np.loadtxt('data/cells/cells_centers.csv', delimiter=',')
shapes = np.load('data/cells/cells_boundaries.npy')
face_colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'white']

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add and color the membrane
    membrane = viewer.add_image(cells[:, :, 0], name='membrane')
    membrane.colormap = Colormap([(0, 0, 0, 1), (1., 0., 1., 1.)])
    membrane.clim = [0.0, 255.0]
    membrane.blending = 'additive'

    # add and color the cytoplasm
    cytoplasm = viewer.add_image(cells[:, :, 1], name='cytoplasm')
    cytoplasm.colormap = Colormap([(0, 0, 0, 1), (1., 1., 0., 1.)])
    cytoplasm.clim = [0.0, 255.0]
    cytoplasm.blending = 'additive'

    # add and color the nucleus
    nucleus = viewer.add_image(cells[:, :, 2], name='nucleus')
    nucleus.colormap = Colormap([(0, 0, 0, 1), (0., 1., 1., 1.)])
    nucleus.clim = [0.0, 255.0]
    nucleus.blending = 'additive'

    boundaries_layer = viewer.add_shapes(shapes, shape_type='polygon',
                                         face_color=face_colors,
                                         name='boundaries')
    boundaries_layer.visible = False


    centers_layer = viewer.add_markers(centers, name='centers')
    centers_layer.size = 20
    centers_layer.edge_width = 0
    centers_layer.face_color = 'blue'
    centers_layer.opacity = 0.75
    centers_layer.visible = False

# centers = centers_layer.data
# np.savetxt('data/cells/cells_centers.csv', centers, delimiter=',')
#
# shapes = boundaries_layer.data.to_list()
# np.save('data/cells/cells_boundaries.npy', shapes)
