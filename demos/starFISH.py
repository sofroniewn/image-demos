"""
Displays FISH data, raw and deconvolved, with spots detected using starFISH
"""

from skimage.io import imread
import numpy as np
from napari import ViewerApp
from napari.util import app_context

raw = imread('data/FISH_raw.tif')
deconvolved = imread('data/FISH_deconvolved.tif')
spots = np.loadtxt('data/FISH_spots.csv', delimiter=',')

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the raw images
    raw_layer = viewer.add_image(raw.transpose(2, 1, 0), name='raw')
    raw_layer.colormap = 'gray'
    raw_layer.clim = (140.0, 1300.0)

    # decon_layer = viewer.add_image(deconvolved.transpose(2, 1, 0),
    #                                name='deconvolved')
    # decon_layer.colormap = 'gray'
    # decon_layer.clim = (0.0, 0.2)

    spots_layer = viewer.add_markers(spots[:, [1, 2, 0]], face_color='red',
                                     edge_color='red', symbol='ring', size=8,
                                     n_dimensional=True, name='spots')
    spots_layer.opacity = 0.5
