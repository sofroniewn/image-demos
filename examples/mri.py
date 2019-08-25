"""
Displays an MRI volume
"""

from skimage.io import imread
from napari import Viewer, gui_qt
import numpy as np

mri = imread('data/MRI/mri.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mri, name='mri', colormap='gray')

    @viewer.bind_key('s')
    def swap(viewer):
        """Swaps dims
        """
        viewer.dims.order = np.roll(viewer.dims.order, 1)
