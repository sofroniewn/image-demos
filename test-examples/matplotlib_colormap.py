import numpy as np
import napari

img = np.array([[1, 0], [0, 1]])

with napari.gui_qt():
    napari.view_image(img, colormap='BuPu')  # KeyError