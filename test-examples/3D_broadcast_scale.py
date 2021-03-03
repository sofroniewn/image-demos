import napari
import numpy as np


with napari.gui_qt():
	v = napari.view_image(np.random.random((10, 20, 20)), scale=(2, 2))