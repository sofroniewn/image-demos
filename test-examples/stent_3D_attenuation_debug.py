"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import napari


with np.load('data/vispy_volumes/stent.npz') as array:
    stent = array["data"]

with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)

    viewer.add_image(stent, name='stent')
    viewer.layers['stent'].rendering = 'attenuated_mip'
    viewer.layers['stent'].attenuation = 1.8
    # viewer.layers['stent'].rendering = 'attenuated_mip'
    # viewer.layers['stent'].attenuation = 1.8
    print(viewer.layers['stent'].attenuation)
