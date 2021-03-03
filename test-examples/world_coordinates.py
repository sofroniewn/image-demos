"""
Display one 3-D volume layer using the add_volume API
"""
import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((11, 11)), colormap='red', opacity=.5, scale=(2, 2), name='half', rotate=30)
    viewer.add_image(np.random.random((21, 21)), colormap='blue', opacity=.5, name='full')
    #viewer.add_image(np.random.random((11, 11)), colormap='red', opacity=.5, name='half')
    viewer.add_points([[0, 0], [10, 10]], size=0.5, opacity=.5)
