"""
Display raw and sheared
"""
import numpy as np
from skimage.io import imread
import napari
from napari.utils.transforms import shear_matrix_from_angle


raw = imread('data/affine/AIUTSW_raw_data.tif')
sheared = imread('data/affine/AIUTSW_30_degree_shear.tif')

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer(ndisplay=3)
    viewer.add_image(raw, colormap='blue', blending='additive', shear=shear_matrix_from_angle(30))
    viewer.add_image(sheared, colormap='red', blending='additive')
