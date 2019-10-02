"""
Display some dipy bundles
"""

import numpy as np
from skimage import data
import napari
import dipy.data as dpd

bundles = dpd.read_bundles_2_subjects()
cst = bundles['cst.right']

with napari.gui_qt():
    blobs = data.binary_blobs(
                length=128, blob_size_fraction=0.05, n_dim=3, volume_fraction=0.05
            )
    viewer = napari.view(blobs.astype(float))

    print('Path', len(cst))
    layer = viewer.add_shapes(
        cst, shape_type='path', edge_width=4, edge_color=['red', 'blue']
    )

    #viewer.dims.ndisplay = 3
