"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import napari
from numcodecs import Blosc
import zarr
compressor = Blosc(cname = 'zstd', clevel = 3, shuffle = Blosc.BITSHUFFLE)
data = zarr.ones((102_0, 200, 210), chunks = (100, 200, 210), compressor = compressor)


with napari.gui_qt():
    viewer = napari.view_image(data, is_pyramid=False, contrast_limits=[0, 1])
