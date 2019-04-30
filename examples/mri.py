"""
Displays an MRI volume
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

mri = imread('data/MRI/mri.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the mri
    layer = viewer.add_image(mri, name='mri')
    layer.colormap = 'gray'
