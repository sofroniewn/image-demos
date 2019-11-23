import numpy as np
from skimage import data
from skimage.util import random_noise
import napari

blobs_raw = data.binary_blobs(length=64, n_dim=3, volume_fraction=0.1)

with napari.gui_qt():
    viewer = napari.view_image(blobs_raw, scale = [0.25, 2, 1])
    viewer.dims.ndisplay = 3
