"""
Displays an MRI volume
"""

from napari import Viewer, gui_qt
import numpy as np
import zarr

file_name = 'data/MRI/synthesized_FLASH25.zarr'
mri = zarr.open(file_name, mode='r')

print(mri.shape)

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mri
    layer = viewer.add_image(mri, name='mri', colormap='gray', clim_range=[0, 1])

    @viewer.bind_key('s')
    def swap(viewer):
        """Swaps dims
        """
        viewer.dims.order = np.roll(viewer.dims.order, 1)
