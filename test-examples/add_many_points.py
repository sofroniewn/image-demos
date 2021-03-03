"""
Display many points layers
"""

import numpy as np
import napari
from time import time

data = []
for i in range(100):
    data.append(np.random.random((10, 2)))

# viewer = napari.components.ViewerModel()
with napari.gui_qt():
    viewer = napari.Viewer()
    # with viewer.blocking_repaint():
    for i, points in enumerate(data):
        # add the points
        viewer.add_points(points)
    print(f'added 100')
    viewer.layers[0].selected = True
    start = time()
    a = viewer.layers.active
    end = time()
    print(f'run {i} in time {end - start}')