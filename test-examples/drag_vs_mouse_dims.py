"""
Display a points layer on top of an image layer using the add_points and
add_image APIs
"""

import numpy as np
import napari

scale = (.5,) * 3

with napari.gui_qt():
    data = np.random.randint(0,255, (10,10,10), dtype='uint8')
    viewer = napari.Viewer()
    viewer.add_image(data, name='raw')
    viewer.add_image(data, scale=scale, name=f'scaled_{scale}', colormap='blue')