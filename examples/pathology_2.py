"""
SHOW A SINGLE LAYER IMAGE!!!!!
"""

import numpy as np
import dask.array as da
import napari
# Import magicgui and qt functionality
from qtpy.QtWidgets import QSlider
from qtpy.QtCore import Qt
from magicgui import magicgui
from typing_extensions import Annotated

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

# create an empty viewer
viewer = napari.Viewer()

# add the pyramid
viewer.add_image(pyramid[0], name='slide', multiscale=False)
viewer.camera.zoom = 0.5
napari.run()