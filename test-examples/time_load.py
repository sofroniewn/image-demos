"""Test converting an image to a pyramid.
"""
import time
import numpy as np
a = time.time()
import vispy
print('vispy', time.time()-a)
b = time.time()
import zarr
print('zarr', time.time()-b)
d = time.time()
import dask
print('dask', time.time()-d)
e = time.time()
import skimage
print('skimage', time.time()-e)
c = time.time()
import napari
print('napari', time.time()-c)

img = np.random.random((512, 512))
print('shape: ', img.shape)

with napari.gui_qt():
    viewer = napari.view_image(img)
