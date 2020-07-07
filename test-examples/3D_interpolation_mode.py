import numpy as np
import napari

volume = np.random.random((5, 768, 1024))


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    layer_norm = viewer.add_image(
        volume,
        visible=False,
    )
    layer_norm.interpolation = 'linear'
