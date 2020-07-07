"""
Slow "timeseries" of big labels
"""

from skimage import data
import numpy as np
import napari

with napari.gui_qt():
    #viewer = napari.view_image(np.random.random((6, 16384, 16384)), name='big 2D timeseries')
    # viewer = napari.view_image(np.random.random((6, 256, 512, 512)), ndisplay=3, name='big 3D timeseries')
    # viewer = napari.view_labels(np.random.randint(10, size=(20, 2048, 2048)),  name='big labels timeseries')
    blobs = np.stack(
        [
            data.binary_blobs(
                length=8092, blob_size_fraction=0.05, n_dim=2, volume_fraction=f
            )
            for f in np.linspace(0.05, 0.5, 10)
        ],
        axis=0,
    )
    print('data ready')
    viewer = napari.view_image(blobs.astype(float))
