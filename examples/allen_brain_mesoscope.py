"""
Displays the allen brain reference atlas at 10 um resolution
"""

from skimage.io import imread
import numpy as np
from glob import glob
from napari import ViewerApp
from napari.util import app_context

base_name = '/Users/nicholassofroniew/Documents/DATA-imaging/allen_brain/natalia/0620_Slc_2x4'
files = glob(base_name + '/*.tif')

slices = [imread(f) for f in files]

print(slices[0].shape)
shape = slices[0].shape[1:]

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the layers
    for i, im in enumerate(slices):
        name = files[i][-10:]
        viewer.add_image(im.transpose(1, 2, 0), name=name)
        viewer.layers[i].colormap = 'gray'
        viewer.layers[i].clim = [0.0, 50.0]
        viewer.layers[i].clim_range = [0.0, 150.0]
        offset = np.array([i%4, i//4])
        viewer.layers[i].translate = offset*shape
