import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    image = np.random.random((20, 100, 100))
    viewer.add_image(image)

