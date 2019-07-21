"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread, imsave
import numpy as np
from napari import Viewer, gui_qt

cells = imread('data-njs/allen_cell/cells.tif')
print(cells.shape)


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    ch1 = viewer.add_volume(cells[:, 1, :, :], name='red spots',
                           clim_range=(300, 700), clim=(400.0, 520.0), colormap='red', blending='additive')

    ch2 = viewer.add_volume(cells[:, 2, :, :], name='cells', colormap='green', clim=(410.0, 700.0), blending='additive')

    ch3 = viewer.add_volume(cells[:, 3, :, :], name='yellow spots',
                           clim_range=(300, 700), clim=(420.0, 500.0), colormap='yellow', blending='additive')

    ch4 = viewer.add_volume(cells[:, 4, :, :], name='DAPI', colormap='blue', clim=(500.0, 1300.0), blending='additive')

    # add brightfield
    brightfield = viewer.add_volume(cells[:, 0, :, :], name='brightfield', colormap='gray')
