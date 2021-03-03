import numpy as np
import napari

regions = [np.array([[1248, 6698],
       [1246, 6697],
       [1242, 6698],
       [1248, 6698],
       [1242, 6694]])]

with napari.gui_qt():
    viewer = napari.Viewer()
    _ = viewer.add_shapes(regions, shape_type='polygon', edge_color='red')