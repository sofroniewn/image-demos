"""
Displays an 100GB zarr file of lattice light sheet data
"""

import dask.array as da
import napari

file_name = 's3://sofroniewn/image-data/LLSM/AOLLSM_m4_560nm.zarr'
data = da.from_zarr(file_name)

with napari.gui_qt(startup_logo=True):
    # create an empty viewer
    viewer = napari.Viewer(title='remote', axis_labels='tzyx')
    viewer.add_image(data, name='AOLLSM_m4_560nm', scale=[1, 3, 1, 1],
                contrast_limits=[0, 150_000], colormap='magma')
