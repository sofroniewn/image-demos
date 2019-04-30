
"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

image = imread('data/mesoscope/anatomical/plane.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the image
    layer = viewer.add_image(image[0], name='plane')
    layer.clim = (-72.0, 1300.0)
    layer.colormap = 'gray'
