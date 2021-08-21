import numpy as np
import napari


viewer = napari.Viewer()
viewer.open_sample(plugin='scikit-image', sample='cell')
viewer.dims.ndisplay = 1
napari.run()