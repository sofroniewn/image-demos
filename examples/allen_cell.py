"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread, imsave
import numpy as np
from napari import Viewer
from napari.util import app_context
from vispy.color import Colormap

cells = imread('data/allen_cell/cells.tif')
labels = imread('data/allen_cell/labels.tif')

print(cells.shape)

with app_context():
    # create an empty viewer
    viewer = Viewer()

    ch1 = viewer.add_image(cells[:, 1, :, :], name='red spots',
                           clim_range=(300, 700))
    ch1.colormap = Colormap([(0, 0, 0, 1), (1., 0., 0., 1.)])
    ch1.clim = (400.0, 520.0)
    ch1.blending = 'additive'

    ch2 = viewer.add_image(cells[:, 2, :, :], name='cells')
    ch2.colormap = Colormap([(0, 0, 0, 1), (0., 1., 0., 1.)])
    ch2.clim = (410.0, 700.0)
    ch2.blending = 'additive'

    ch3 = viewer.add_image(cells[:, 3, :, :], name='yellow spots',
                           clim_range=(300, 700))
    ch3.colormap = Colormap([(0, 0, 0, 1), (1., 1., 0., 1.)])
    ch3.clim = (420.0, 500.0)
    ch3.blending = 'additive'

    ch4 = viewer.add_image(cells[:, 4, :, :], name='DAPI')
    ch4.clim = (500.0, 1300.0)
    ch4.colormap = Colormap([(0, 0, 0, 1), (0., 0., 1., 1.)])
    ch4.blending = 'additive'

    # add brightfield
    brightfield = viewer.add_image(cells[:, 0, :, :], name='brightfield')
    brightfield.colormap = 'gray'


    #labels = np.zeros([cells.shape[i] for i in [0, 2, 3]])
    labels_layer = viewer.add_labels(labels, name='annotations')
    labels_layer.n_dimensional = False

labels = labels_layer.image
imsave('data/allen_cell/labels.tif', labels.astype('uint32'), plugin='tifffile',
       photometric='minisblack')
