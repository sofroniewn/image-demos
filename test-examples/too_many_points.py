import numpy as np
import napari

with napari.gui_qt():
	myViewer = napari.Viewer()

	# works up to 1024 points but crashes if >1024 points
	s = (1025,3)
	# (1025,3) random integers in the range [10, 100)
	myPoints = np.random.randint(10, 100, s)
	pointLayer = myViewer.add_points(myPoints)
