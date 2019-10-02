"""
Displays an MRI volume
"""

from napari import Viewer, gui_qt
import numpy as np
import zarr

file_name = 'data-njs/lymph_nodes/TCZYX_test_data.zarr'
lymph = zarr.open(file_name, mode='r')
print(lymph.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(lymph[0, 0], name='lymph node', contrast_limits=[0, 1], scale=[8, 1, 1])
