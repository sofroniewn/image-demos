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


file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]


def theshold_block(block, thresh):
    return block[:, :, 0] < thresh
     

@magicgui(auto_call=True,
          value={'widget_type': QSlider, 'minimum': 0, 'maximum': 255, 'orientation':Qt.Horizontal})
def threshold(layer: napari.layers.Image, value: int = 100) -> napari.layers.Labels:
    pyramid = layer.data
    segmented = [ar.map_blocks(lambda block: theshold_block(block, value), drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]
    return segmented


with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the pyramid
    viewer.add_image(pyramid, name='slide', multiscale=True)
    viewer.window.add_dock_widget(threshold.Gui());
