"""
SHOW A LABELS PYRAMID!!!!!!!!!!
"""

import dask.array as da
import napari

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i))[:, :, 1] for i in range(10)]

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt='%H:%M:%S',
)


# create an empty viewer
viewer = napari.Viewer()

# add the pyramid
viewer.add_labels(pyramid, name='slide')
viewer.camera.zoom = 0.5

napari.run()