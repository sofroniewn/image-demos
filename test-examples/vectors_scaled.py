import numpy as np
import napari


with napari.gui_qt():
    v = napari.Viewer(ndisplay=3)

    # one vector for each of two 3D slices.
    vectors = np.array([
    [[0,0,0,0], [0,1,1,1]],
    [[1,0,0,0], [1,10,10,10]],
    ])

    #v.add_vectors(vectors) # works fine
    v.add_vectors(vectors, length=[1, 10, 10, 10]) # creates 10 slices instead of 2.