"""
Display multiplexed brain data from Salvatore and Seeley.
"""

from skimage.io import imread
import numpy as np
from napari import Viewer
from napari.util import app_context
from vispy.color import Colormap
from glob import glob
from os.path import basename

file_names = glob('data/ndcn/seeley/*.tif')
names = [basename(f)[:-18] for f in file_names]
images = [imread(f) for f in file_names]
colors = [(1., 0., 0., 1.),
          (0., 1., 0., 1.),
          (1., 1., 0., 1.),
          (1., 0., 1., 1.),
          (0., 1., 1., 1.)]

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    for i in range(len(images)):
        image = images[i]
        if names[i] == 'DAPI':
            col = (0., 0., 1., 1.)
        else:
            col = colors[i % len(colors)]
        layer = viewer.add_image(np.flipud(image), name=names[i])
        layer.colormap = Colormap([(0., 0., 0., 1.), col])
        layer.clim = [np.percentile(image, 1), np.percentile(image, 99)]
        layer.blending = 'additive'
