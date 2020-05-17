"""
Display 48-bit rgb
"""
import numpy as np
from skimage.io import imread
import napari


hela = imread('data/cells/hela-cells.tif')
h_f = hela.astype('float')
h_s = h_f / h_f.max()
scaled = np.round(255 * h_s).astype('int')

print(hela.shape, hela.max(), h_f.max(), h_s.max(), scaled.max(), scaled.dtype.kind)

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the helao
    viewer.add_image(scaled, name='hela')
