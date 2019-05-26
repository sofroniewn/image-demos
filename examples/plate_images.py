"""
Display multiplexed brain data from Salvatore and Seeley.
"""

from skimage.io import imread
import numpy as np
from napari import Viewer
from napari.util import app_context
from vispy.color import Colormap


file_name = 'data/ndcn/kampmann/plate.tif'
images = imread(file_name).transpose(2, 0, 1)
colors = {'blue': (0., 0., 1., 1.),
          'red': (1., 0., 0., 1.),
          'green': (0., 1., 0., 1.),
          'magenta': (1., 1., 0., 1.),
          'cyan': (1., 0., 1., 1.),
          'yellow': (0., 1., 1., 1.)}
color_names = ['red', 'blue', 'green',]

print(images.shape)

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    for i, im in enumerate(images):
        layer = viewer.add_image(im, name='plate ' + color_names[i])
        layer.colormap = Colormap([(0., 0., 0., 1.), colors[color_names[i]]])
        layer.clim = [np.percentile(im, 1), np.percentile(im, 99)]
        layer.blending = 'additive'
