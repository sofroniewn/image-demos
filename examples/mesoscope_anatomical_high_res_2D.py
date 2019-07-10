
"""
Displays anatomical data from the mesoscope
"""

from skimage.io import imread
from napari import Viewer, gui_qt

image = imread('data/mesoscope/anatomical/plane.tif')


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the image
    layer = viewer.add_image(image[0], name='plane', clim=(-72.0, 1300.0), colormap='gray')
