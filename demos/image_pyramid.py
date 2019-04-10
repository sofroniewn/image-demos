"""
Image pyramid of pathology slide
"""

from openslide import OpenSlide
import numpy as np
from napari import ViewerApp
from napari.util import app_context

slide = OpenSlide('data/camelyon16/normal_001.tif')

pyramid = ([np.asarray(slide.read_region((0, 0), i,
                       slide.level_dimensions[i])).transpose(1, 0, 2)
                       for i in range(0, 10)])

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the pyramid
    layer = viewer.add_pyramid(pyramid, name='slide')
