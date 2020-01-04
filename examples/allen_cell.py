"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread, imsave
import numpy as np
from napari import Viewer, gui_qt

cells = imread('data-njs/allen_cell/cells.tif')
labels = imread('data-njs/allen_cell/labels.tif')

print(cells.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    ch1 = viewer.add_image(cells[:, 1, :, :], name='red spots',
                           contrast_limits=(400.0, 520.0), colormap='red', blending='additive', scale=[3, 1, 1])

    ch2 = viewer.add_image(cells[:, 2, :, :], name='cells', colormap='green', contrast_limits=(410.0, 700.0), blending='additive',  scale=[3, 1, 1])

    ch3 = viewer.add_image(cells[:, 3, :, :], name='yellow spots',
                           contrast_limits=(420.0, 500.0), colormap='yellow', blending='additive',  scale=[3, 1, 1])

    ch4 = viewer.add_image(cells[:, 4, :, :], name='DAPI', colormap='blue', contrast_limits=(500.0, 1300.0), blending='additive',  scale=[3, 1, 1])

    # add brightfield
    brightfield = viewer.add_image(-cells[:, 0, :, :], name='brightfield', colormap='gray',  scale=[3, 1, 1])

    #labels = np.zeros([cells.shape[i] for i in [0, 2, 3]])
    labels_layer = viewer.add_labels(labels, name='annotations', scale=[3, 1, 1])

# labels = labels_layer.data
# imsave('data/allen_cell/labels.tif', labels.astype('uint32'), plugin='tifffile',
#        photometric='minisblack')
