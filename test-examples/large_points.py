import napari
import numpy as np

with napari.gui_qt():
    v = napari.Viewer(ndisplay=3)
    # lots of overlapping points with coordinates between 0 and 1, and default size of 10
    #v.add_points(np.random.rand(10000, 3))
    pl = napari.layers.Points(np.random.rand(10000,3))
    v.layers.append(pl)
    v.reset_view()