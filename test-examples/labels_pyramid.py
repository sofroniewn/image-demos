"""Test converting an image to a pyramid.
"""

import numpy as np
from napari import Viewer, gui_qt
from skimage.transform import pyramid_gaussian
from skimage import data
from scipy import ndimage as ndi

blobs = data.binary_blobs(length=9_000, volume_fraction=0.1, n_dim=2)
labeled = ndi.label(blobs)[0]

print(labeled.shape)

with gui_qt():
    viewer = Viewer()
    viewer.add_labels(labeled)
