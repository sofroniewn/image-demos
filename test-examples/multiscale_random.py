"""
Dynamically load irregularly shapes images of ants and bees
"""

import dask.array as da
import napari 

shapes = [(167424, 79360), (83712, 39680), (41856, 19840), (20928, 9920), (10464, 4960), (5232, 2480), (2616, 1240), (1308, 620), (654, 310), (327, 155), (163, 77)]
pyramid = [da.random.random(s) for s in shapes]

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.Viewer()
    viewer.add_image(pyramid)
