"""
Displays an MRI volume
"""

from napari import Viewer, gui_qt
import numpy as np
import zarr

file_name = 'data-njs/lymph_nodes/TCZYX_pyr.zarr'
lymph = zarr.open(file_name, mode='r')

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_multichannel(lymph['3'][0], channel=0, name='lymph node', contrast_limits=[0, 255], scale=[8, 1, 1])
