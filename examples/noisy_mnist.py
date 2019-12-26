"""
Displays an MRI volume
"""

from skimage.io import imread
from napari import Viewer, gui_qt

clean = imread('data/mnist/clean.tif')
noisy = imread('data/mnist/noisy.tif')


def view_overlaid(offset):
    noisy_layer.translate = [0, 0]
    viewer.camera.set_range((0, offset), (0, offset))


def view_side_by_side(offset):
    noisy_layer.translate = [offset, 0]
    viewer.camera.set_range((0, 2*offset), (0, offset))


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    clean_layer = viewer.add_image(clean, name='clean', colormap='gray')

    noisy_layer = viewer.add_image(noisy, name='noisy', colormap='gray')
    
    view_side_by_side(clean.shape[1])
