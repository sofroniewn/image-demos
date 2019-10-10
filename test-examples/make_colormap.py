import numpy as np
from vispy.color import Colormap
import napari


cmap = Colormap([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
image = np.random.random((100, 100))

with napari.gui_qt():
    viewer = napari.view_image(image, colormap=('diverging', cmap))
