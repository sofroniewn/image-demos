import numpy as np
import napari


img = np.random.randint(0, 100, size=(6898, 9946))

with napari.gui_qt():
    v = napari.view_image(img)
