import numpy as np
from skimage import data, filters
import napari


blobs_raw = np.stack([
    data.binary_blobs(length=256, n_dim=3, volume_fraction=f)
    for f in np.linspace(0.05, 0.5, 10)
])
blobs = filters.gaussian(blobs_raw, sigma=(0, 2, 2, 2))
with napari.gui_qt():
    # create a Viewer and add an image here
    viewer = napari.view_image(blobs)
