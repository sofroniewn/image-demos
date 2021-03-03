"""
Display one 3-D volume layer using the add_volume API
"""
import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    viewer.add_image(np.random.random((5, 5, 5)), name='background', colormap='red', opacity=.5)
    viewer.scale_bar.visible = True
    viewer.reset_view()