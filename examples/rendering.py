# IPython log file


import numpy as np
import toolz as tz
from skimage import data, util


blobs_raw = np.stack([
    data.binary_blobs(length=64, n_dim=3, volume_fraction=f)
    for f in np.linspace(0.05, 0.5, 10)
])

add_noise = tz.curry(util.random_noise)
blobs = tz.pipe(
    blobs_raw,
    add_noise(mode='s&p'),
    add_noise(mode='gaussian'),
    add_noise(mode='poisson')
)

print(blobs.shape)
from scipy import ndimage as ndi

neighbors3d = ndi.generate_binary_structure(3, connectivity=1)
neighbors = neighbors3d[np.newaxis, ...]

opening, closing = map(tz.curry, [ndi.grey_opening, ndi.grey_closing])

denoised = tz.pipe(
    blobs,
    opening(footprint=neighbors),
    closing(footprint=neighbors)
)
from skimage import filters

# label needs a shape `(3,) * ndim` array
neighbors2 = np.concatenate(
    (np.zeros_like(neighbors), neighbors, np.zeros_like(neighbors))
)

binary = filters.threshold_li(denoised) < denoised
labels = ndi.label(binary, structure=neighbors2)[0]


import napari

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(blobs, name='blobs', colormap='magenta')
    viewer.add_image(denoised, name='denoised', colormap='cyan')
    viewer.add_labels(labels, name='labels')
    viewer.dims.ndisplay = 3
