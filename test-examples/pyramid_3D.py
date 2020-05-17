import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    data = [np.random.random((5, 2**s, 2**s)) for s in range(13, 8, -1)]
    viewer.add_image(data)
    # check that this doesn't crash
    # viewer.dims.ndisplay = 3
    # viewer.layers[0].refresh()
