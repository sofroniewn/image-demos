"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread, imsave
import numpy as np
from napari import Viewer, gui_qt

cells = imread('data/allen_workshop/AICS-12_1070.ome.tif')

print(cells.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    ch1 = viewer.add_image(cells[:, :4], channel_axis=1, scale=[3, 1, 1])
