"""
Displays an MRI volume
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

clean = imread('data/mnist/clean.tif')
noisy = imread('data/mnist/noisy.tif')


def view_overlaid(offset):
    noisy_layer.translate = [0, 0]
    viewer.camera.set_range((0, offset), (0, offset))


def view_side_by_side(offset):
    noisy_layer.translate = [offset, 0]
    viewer.camera.set_range((0, 2*offset), (0, offset))


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the images
    clean_layer = viewer.add_image(clean, name='clean')
    clean_layer.colormap = 'gray'

    noisy_layer = viewer.add_image(noisy, name='noisy')
    noisy_layer.colormap = 'gray'

    view_side_by_side(clean.shape[1])
