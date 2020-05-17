import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    shapes = [(4000, 3000), (2000, 1500), (1000, 750), (500, 375)]
    np.random.seed(0)
    data = [np.random.random(s) for s in shapes]
    _ = viewer.add_image(data, is_pyramid=True)
