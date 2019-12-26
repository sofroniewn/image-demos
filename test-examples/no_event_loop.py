"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
from skimage import data
import napari


astro = data.astronaut()
# add the image
viewer = napari.view_image(astro, rgb=True)
# add the points
points = np.array([[100, 100], [200, 200], [300, 100]])
viewer.add_points(points, size=30)
