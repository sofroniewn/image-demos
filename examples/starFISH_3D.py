"""
Displays FISH data, raw and deconvolved, with spots detected using starFISH
"""

from skimage.io import imread
import numpy as np
from napari import Viewer, gui_qt

raw = imread('data-njs/smFISH/raw.tif')
deconvolved = imread('data-njs/smFISH/deconvolved.tif')
spots = np.loadtxt('data-njs/smFISH/spots.csv', delimiter=',')

print(raw.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the raw images
    raw_layer = viewer.add_volume(raw, name='images', colormap='red', clim=(140.0, 1300.0), blending='additive')

    decon_layer = viewer.add_volume(deconvolved, name='deconvolved', colormap='green', clim=(0.0, 0.2), blending='additive')

    spots_layer = viewer.add_points(spots, face_color='blue',
                                     edge_color='blue', symbol='ring', size=8,
                                     n_dimensional=True, name='spots')
    spots_layer.opacity = 0.5

    @viewer.bind_key('s')
    def swap(viewer):
        """Swaps dims
        """
        dims = np.array(viewer.dims.order[-3:])
        dims = (dims + 1) % 3
        print('swapping', dims)
        viewer.dims.swap(dims[0], dims[1])
