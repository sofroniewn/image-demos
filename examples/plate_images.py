"""
Display multiplexed brain data from Salvatore and Seeley.
"""

from skimage.io import imread
import numpy as np
from napari import Viewer, gui_qt


file_name = 'data-njs/ndcn/kampmann/plate.tif'
images = imread(file_name).transpose(2, 0, 1)
color_names = ['red', 'blue', 'green',]

print(images.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    for i, im in enumerate(images):
        clim = [np.percentile(im, 1), np.percentile(im, 99)]
        layer = viewer.add_image(im, name='plate ' + color_names[i], clim=clim, colormap=color_names[i])
        layer.blending = 'additive'
