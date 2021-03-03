"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
import dask.array as da
import napari 


pyramid = [4*da.from_zarr(f'data/covid19/9822151/{i}.zarr')[::-1, :].astype('uint16') for i in range(11)]
print([p.shape for p in pyramid])

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()

    # add the images
    viewer.add_image(pyramid)
