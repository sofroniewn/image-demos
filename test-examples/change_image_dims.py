"""Test changing the dims and shape of an image layer in place and checking the
numbers of sliders and their ranges changes appropriately.
"""

import numpy as np
from skimage import data
from napari import Viewer, gui_qt


with gui_qt():
    viewer = Viewer()

    # add data
    blobs = data.binary_blobs(
        length=128, blob_size_fraction=0.05, n_dim=3, volume_fraction=0.25
    ).astype(float)

    layer = viewer.add_image(blobs[:64])

    # switch number of displayed dimensions
    layer.data = blobs[0]

    # switch number of displayed dimensions
    layer.data = blobs[:64]

    # switch the shape of the displayed data
    layer.data = blobs[:3]
