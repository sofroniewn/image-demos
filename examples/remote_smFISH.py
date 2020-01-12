"""
Dynamically load irregularly shapes images of bees from s3
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
import napari

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_path = 's3://sofroniewn/image-data/smFISH/raw.zarr'
# smFISH = da.from_zarr(file_path)
# print(smFISH.shape)


with napari.gui_qt():
    # create an empty viewer
    napari.view_image(path=file_path, name='smFISH', contrast_limits=(140.0, 1300.0))
