"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread
import numpy as np
from napari import ViewerApp
from napari.util import app_context
from vispy.color import Colormap

cells = imread('data/starFISH.png')

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add and color the membrane
    cell_layer = viewer.add_image(cells[:, :, 0], name='cells')
    cell_layer.colormap = 'gray'

    boundaries_layer = viewer.add_shapes([], shape_type='polygon',
                                         name='nuclei')
    boundaries_layer.visible = False

shapes, types = boundaries_layer.data.to_list()
np.save('data/starFISH_boundaries.npy', shapes)
