import numpy as np
import napari


r0 = np.random.random((1, 2, 236, 275, 271))
r1 = np.random.random((1, 2, 236, 137, 135))

with napari.gui_qt():
    v = napari.view_image([r0, r1])