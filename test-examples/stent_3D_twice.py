"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import scipy.ndimage as ndi
import napari


with np.load('data/vispy_volumes/stent.npz') as array:
    stent = array["data"]

stent_small = ndi.zoom(stent, 0.5)

print(stent.shape, stent_small.shape)

# with np.load('data/vispy_volumes/mri.npz') as array:
#     mri = array["data"]

#vessel_tree = np.load('data/vispy_volumes/vessel_tree_noise.npy')
#vessel_tree = np.load('data/vispy_volumes/skeleton_vessel_tree_noise.npy')


with napari.gui_qt():
    viewer = napari.Viewer(axis_labels='zyx')

    # # add an image first
    # viewer.add_image(stent)

    # add the volume
    print(stent.shape)
    viewer.add_image(stent, name='stent')
    viewer.add_image(stent_small, name='stent_small', scale=[2, 2, 2], translate=[128, 0, 128])
    viewer.add_image(stent_small, name='stent_small_2', scale=[2, 2, 2], translate=[0, 0, 256])
    viewer.ndisplay = 2
    
    # add an image second first
    #viewer.add_image(np.random.random((10, 100, 200)))
