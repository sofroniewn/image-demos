import numpy as np
from skimage import data
from skimage.util import random_noise
import napari

blobs_raw = np.stack([data.binary_blobs(length=64, n_dim=3, volume_fraction=f)
                      for f in np.linspace(0.05, 0.5, 10)])
blobs_sp = random_noise(blobs_raw, mode='s&p')
blobs_g = random_noise(blobs_sp, mode='gaussian')
blobs = random_noise(blobs_g, mode='poisson')
with napari.gui_qt():
    viewer = napari.view_image(blobs.astype(np.float32))
    viewer.dims.ndisplay = 3
