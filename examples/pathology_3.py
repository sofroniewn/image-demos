"""
Analysis on an image pyramid of pathology slide
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
pyramid = [da.from_zarr(file_name + '/' + str(i))[:, :, 1] for i in range(10)]

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt='%H:%M:%S',
)


with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the pyramid
    viewer.add_labels(pyramid, name='slide')
    viewer.camera.zoom = 0.5