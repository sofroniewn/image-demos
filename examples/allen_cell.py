"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread, imsave
import numpy as np
from napari import ViewerApp
from napari.util import app_context
from vispy.color import Colormap

cells = imread('data/allen_cell/cells.tif')
labels = imread('data/allen_cell/labels.tif')

print(cells.shape)

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    ch1 = viewer.add_image(cells[:, 1, :, :].transpose(1, 2, 0),
                                   name='ch1 - red', clim_range=(300, 700))
    ch1.colormap = Colormap([(0, 0, 0, 1), (1., 0., 0., 1.)])
    ch1.clim = (400.0, 520.0)
    ch1.blending = 'additive'

    ch2 = viewer.add_image(cells[:, 2, :, :].transpose(1, 2, 0),
                                   name='ch2 - green')
    ch2.colormap = Colormap([(0, 0, 0, 1), (0., 1., 0., 1.)])
    ch2.clim = (410.0, 700.0)
    ch2.blending = 'additive'

    ch3 = viewer.add_image(cells[:, 3, :, :].transpose(1, 2, 0),
                                   name='ch3 - yellow', clim_range=(300, 700))
    ch3.colormap = Colormap([(0, 0, 0, 1), (1., 1., 0., 1.)])
    ch3.clim = (420.0, 500.0)
    ch3.blending = 'additive'

    ch4 = viewer.add_image(cells[:, 4, :, :].transpose(1, 2, 0),
                                   name='ch4 - blue')
    ch4.clim = (500.0, 1300.0)
    ch4.colormap = Colormap([(0, 0, 0, 1), (0., 0., 1., 1.)])
    ch4.blending = 'additive'

    # add brightfield
    brightfield = viewer.add_image(cells[:, 0, :, :].transpose(1, 2, 0),
                                   name='brightfield')
    brightfield.colormap = 'gray'


    #labels = np.zeros([cells.shape[i] for i in [2, 3, 0]])
    labels_layer = viewer.add_labels(labels, name='annotations')
    labels_layer.n_dimensional = False

labels = labels_layer.image
imsave('data/allen_cell/labels.tif', labels.astype('uint32'), plugin='tifffile',
       photometric='minisblack')
