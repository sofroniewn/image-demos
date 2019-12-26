"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import napari


with np.load('data/vispy_volumes/stent.npz') as array:
    stent = array["data"]

# with np.load('data/vispy_volumes/mri.npz') as array:
#     mri = array["data"]

#vessel_tree = np.load('data/vispy_volumes/vessel_tree_noise.npy')
#vessel_tree = np.load('data/vispy_volumes/skeleton_vessel_tree_noise.npy')


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)

    # # add an image first
    # viewer.add_image(stent)

    # add the volume
    print(stent.shape)
    viewer.add_image(stent, name='stent')

    # add an image second first
    #viewer.add_image(np.random.random((10, 100, 200)))
