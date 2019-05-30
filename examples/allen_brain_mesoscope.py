"""
Displays the allen brain reference atlas at 10 um resolution
"""

from skimage.io import imread
import numpy as np
from glob import glob
from napari import Viewer
from napari.util import app_context

base_name = 'data/allen_brain/natalia'

experiment = '/0620_Slc_2x4'
# experiment = '/0622_Vip_4x2'
files = glob(base_name + experiment + '/*.tif')

slices = [imread(f) for f in files]

print(slices[0].shape)
shape = slices[0].shape[1:]

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the layers
    for i, im in enumerate(slices):
        name = files[i][-10:-4]
        viewer.add_image(im, name=name)
        viewer.layers[i].colormap = 'gray'
        viewer.layers[i].clim = [0.0, 40.0]
        viewer.layers[i].clim_range = [0.0, 100.0]
        offset = np.array([i%4, i//4])
        viewer.layers[i].translate = offset*shape
