"""
Remote multiscale data from of a zarr file pathology slide
"""

import dask.array as da
import napari

file_name = 's3://sofroniewn/image-data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i) + '/') for i in range(10)]

print([p.shape for p in pyramid])

with napari.gui_qt():
    viewer = napari.Viewer()
    layer = viewer.add_image(pyramid, name='slide')
