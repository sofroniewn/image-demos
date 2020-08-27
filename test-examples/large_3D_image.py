import napari
import numpy as np
from dask import array as da

img = np.asarray(da.random.randint(0, 100, size=(500, 1500, 1500), chunks=250, dtype=np.uint16))
print(img.shape)

with napari.gui_qt():
	v = napari.view_image(img, multiscale=False, contrast_limits=(0, 100), ndisplay=3)