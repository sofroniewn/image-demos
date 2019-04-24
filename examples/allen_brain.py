"""
Displays the allen brain reference atlas at 10 um resolution
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

brain = imread('data/allen_brain/average_template_25.tif')
annotation = imread('data/allen_brain/annotation_25.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the brain
    brain_layer = viewer.add_image(brain.transpose(1, 0, 2), name='brain')
    brain_layer.colormap = 'gray'

    # add the annotations
    annotation_layer = viewer.add_labels(annotation.transpose(1, 0, 2),
                                        name='annotation')
