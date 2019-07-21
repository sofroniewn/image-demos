"""
Displays the allen brain reference atlas at 10 um resolution
"""

from skimage.io import imread
from napari import Viewer, gui_qt

brain = imread('data/allen_brain/average_template_25.tif')
annotation = imread('data/allen_brain/annotation_25.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the brain
    brain_layer = viewer.add_image(brain, name='brain')

    # add the annotations
    annotation_layer = viewer.add_labels(annotation, name='annotation')
