"""Test converting an image to a multiscale.
"""

import dask as da
import napari

img = da.random.random((200_000, 200_000))
# img = np.random.random((20_000, 200))
# img = np.random.random((10, 100, 2500))
print('shape: ', img.shape)

with napari.gui_qt():
    viewer = napari.view_image(img, visible=False)
