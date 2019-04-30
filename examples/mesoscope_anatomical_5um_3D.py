"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

stack = imread('data/mesoscope/anatomical/volume_5um.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the image
    layer = viewer.add_image(stack, name='stack')
    layer.clim = (0.0, 8000.0)
    layer.colormap = 'gray'
