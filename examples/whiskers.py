"""
Displays an MRI volume
"""

from imageio import imread
from napari import Viewer, gui_qt
import numpy as np

mov = imread('data-njs/whiskers/IMG_7988.tif')

print(mov.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mov, name='whiskers')
