"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import Viewer, gui_qt

stack = imread('data/mesoscope/anatomical/volume_zoomed.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    layer = viewer.add_image(stack, name='stack', clim=(0.0, 3000.0), clim_range=(0.0, 6000.0), colormap='gray')
