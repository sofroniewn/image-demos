"""
Display multiplexed brain data from Salvatore and Seeley.
"""

from skimage.io import imread
import numpy as np
from napari import Viewer, gui_qt
from vispy.color import Colormap
from glob import glob
from os.path import basename

file_names = glob('data-njs/ndcn/seeley/*.tif')
names = [basename(f)[:-18] for f in file_names]
images = [imread(f) for f in file_names]
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan']

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    for i in range(len(images)):
        image = images[i]
        if names[i] == 'DAPI':
            col = 'blue'
        else:
            col = colors[i % len(colors)]
        clim = [np.percentile(image, 1), np.percentile(image, 99)]
        layer = viewer.add_image(np.flipud(image), name=names[i], colormap=col, clim=clim)
        layer.blending = 'additive'
