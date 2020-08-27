"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import scipy.ndimage as ndi
import napari


with np.load('data/vispy_volumes/stent.npz') as array:
    stent = array["data"]


print(stent.shape)
with napari.gui_qt():
    viewer = napari.Viewer()

    # add the volume
    viewer.add_image(stent, name='stent')
    viewer.add_image(np.expand_dims(stent[55], axis=0), name='2D_slice', translate=[55, 0, 0], colormap='blue')