import napari
import numpy as np
import dask.array as da

with napari.gui_qt():
    viewer = napari.view_image(np.random.random((2,10,10,10)), channel_axis=0)  # works
    viewer.add_image(da.random.random((2,10,10,10)), channel_axis=0)  # Attribute Error
