"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import Viewer
from napari.util import app_context

stack = imread('data/mesoscope/anatomical/volume_highres.tif')


with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    layer = viewer.add_image(stack,
    name='stack')
    layer.clim = (0.0, 2500.0)
    layer.colormap = 'gray'
