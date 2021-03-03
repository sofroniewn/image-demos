import napari
import numpy as np
import xarray as xr

img = xr.DataArray(np.random.rand(2, 5, 1024, 1024))
mask = xr.DataArray(np.zeros_like(img,dtype=np.int))

# uncomment these to use numpy and all is fine
# img = np.random.rand(2, 5, 1024, 1024)
# mask = np.zeros_like(img, dtype=np.int)

with napari.gui_qt():
    viewer = napari.view_image(img, name='img')
    labels = viewer.add_labels(mask, name='mask')
    labels.mode = 'paint'