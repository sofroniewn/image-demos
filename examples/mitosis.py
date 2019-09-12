"""
Displays a timeseries of a z-stack during mitosis
"""

from skimage.io import imread
from napari import Viewer, gui_qt

mitosis = imread('data/mitosis/mitosis.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the first channel to a red channel
    red = viewer.add_image(mitosis[:, :, 0, :, :], name='red', contrast_limits=(1500.0, 15000.0), colormap='red',
    scale=[1, 10, 1, 1])
    red.blending = 'additive'

    # add the first channel to a green channel
    green = viewer.add_image(mitosis[:, :, 1, :, :], name='green', contrast_limits=(1500.0, 15000.0), colormap='green',
    scale=[1, 10, 1, 1])
    green.blending = 'additive'
