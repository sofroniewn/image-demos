import numpy as np
import napari


with napari.gui_qt():
    v = napari.Viewer(ndisplay=3)
    # 2 points in each of three 3D slices, spaced out differently to easily spot them
    points = np.array([
    [0,0,0,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,5,5,5],
    [2,0,0,0],
    [2,10,10,10],
    ])
    v.add_points(points) # This displays only 2 slices. The last two points are missing!