"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
import dask.array as da
import napari 


pyramid = [da.from_zarr(f'data/covid19/9822151/{i}.zarr')[::-1, :] for i in range(11)]
print([p.shape[:2] for p in pyramid])

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the images
    viewer.add_image(pyramid)
