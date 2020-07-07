import numpy as np
from vispy.color import Colormap
import napari


data = np.random.randint(4, size=(10, 10))
custom = Colormap([
        [0., 0., 0., 0.],  # label 0 is fully transparent
        [1., 0., 0., 1.],  # label 1 is red
        [0., 1., 1., 1.],  # label 2 is cyan
        [1., 1., 0., 1.],  # label 3 is yellow
    ]
)

with napari.gui_qt():
    viewer = napari.view_image(data, colormap=custom, contrast_limits=[0, 3])
