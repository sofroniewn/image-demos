import numpy as np
from skimage import data
from vispy.color import Colormap
import napari

blobs = data.binary_blobs(length=64, n_dim=2, volume_fraction=0.1)
rand = np.random.random((64, 64))

with napari.gui_qt():
    label_red = Colormap([[0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 1.0]])
    viewer = napari.view_image(rand)
    viewer.add_image(blobs, contrast_limits=[0, 1], colormap=('label_red', label_red))
