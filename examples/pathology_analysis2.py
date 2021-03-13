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
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]


def theshold_block(block):
    return block[:, :, 0] > 220
     
segmented = [ar.map_blocks(theshold_block, drop_axis=2, chunks=ar.chunksize[:-1], dtype=np.int)[:ar.shape[0], :ar.shape[1]] for ar in pyramid]


# create an empty viewer
viewer = napari.Viewer()

# add the pyramid
# viewer.add_image(pyramid, name='slide', multiscale=True)
viewer.add_labels(segmented, name='thresholded')
napari.run()
