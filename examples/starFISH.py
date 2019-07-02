"""
Displays FISH data, raw and deconvolved, with spots detected using starFISH
"""

from skimage.io import imread
import numpy as np
from napari import Viewer
from napari.util import app_context

raw = imread('data/smFISH/raw.tif')
deconvolved = imread('data/smFISH/deconvolved.tif')
spots = np.loadtxt('data/smFISH/spots.csv', delimiter=',')

print(raw.shape)

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the raw images
    raw_layer = viewer.add_image(raw, name='images')
    raw_layer.colormap = 'gray'
    raw_layer.clim = (140.0, 1300.0)

    decon_layer = viewer.add_image(deconvolved, name='deconvolved')
    decon_layer.colormap = 'gray'
    decon_layer.clim = (0.0, 0.2)
    decon_layer.visible = False

    spots_layer = viewer.add_points(spots, face_color='red',
                                     edge_color='red', symbol='ring', size=8,
                                     n_dimensional=True, name='spots')
    spots_layer.opacity = 0.5
