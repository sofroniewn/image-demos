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
images = np.array([np.flipud(imread(f)) for f in file_names])

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    clims = [[np.percentile(img, 1), np.percentile(img, 99)] for img in images]
    layer = viewer.add_multichannel(images, axis=0, name=names, contrast_limits=clims, blending='additive')
