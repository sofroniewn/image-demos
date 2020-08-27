import napari
from dask import array as da

img = da.random.randint(0, 100, size=(500, 1500, 1500), chunks=250, dtype=np.uint16)

with napari.gui_qt():
	v = napari.view_image(img, multiscale=False, contrast_limits=(0, 100), ndisplay=3)