"""
Displays an MRI volume in 3D
"""

from skimage.io import imread
from napari import Viewer, gui_qt

mri = imread('data/MRI/mri.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_volume(mri, name='mri')
