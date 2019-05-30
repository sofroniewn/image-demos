"""
Displays a timeseries of a z-stack during mitosis
"""

from skimage.io import imread
from napari import Viewer
from napari.util import app_context
from vispy.color import Colormap

mitosis = imread('data/mitosis/mitosis.tif')


with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the first channel to a red channel
    red = viewer.add_image(mitosis[:, :, 0, :, :], name='red')
    red.colormap = Colormap([(0, 0, 0, 1), (1., 0., 0., 1.)])
    red.clim = (1500.0, 15000.0)
    red.blending = 'additive'

    # add the first channel to a green channel
    red = viewer.add_image(mitosis[:, :, 1, :, :], name='green')
    red.colormap = Colormap([(0, 0, 0, 1), (0., 1., 0., 1.)])
    red.clim = (1500.0, 15000.0)
    red.blending = 'additive'
