"""
Displays an MRI volume
"""

from napari import Viewer, gui_qt
import numpy as np
import zarr

file_name = 'data/MRI/synthesized_FLASH25_pyr.zarr'
mri = zarr.open(file_name, mode='r')
mri = np.asarray(mri['3'])
mri = np.clip(mri, 10, 10000) - 10
print(mri.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mri, name='mri', colormap='gray')
