import napari
import numpy as np

with napari.gui_qt():
    viewer=napari.Viewer()

    viewer.add_image(np.random.random((400, 400)))
    points = np.array([[100, 100], [200, 200], [300, 100]])
    viewer.add_points(points, size=30)