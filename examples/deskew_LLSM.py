"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
from tifffile import imread
from napari.utils.transforms import shear_matrix_from_angle


ch0 = imread('./data-njs/tjl/ch0.tif')
ch1 = imread('./data-njs/tjl/ch1.tif')

with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    shear = 1.73
    viewer.add_image(ch0, blending='additive', colormap='green', scale=[3, 1, 1], shear=shear_matrix_from_angle(30))
    viewer.add_image(ch1, blending='additive', colormap='magenta', scale=[3, 1, 1], shear=shear_matrix_from_angle(30))
