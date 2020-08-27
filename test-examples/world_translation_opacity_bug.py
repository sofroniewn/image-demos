"""
Display one 3-D volume layer using the add_volume API
"""
import numpy as np
import napari


translate = (10,) * 3
with napari.gui_qt():
    data = np.random.randint(0,255, (10,10,10), dtype='uint8')
    viewer = napari.Viewer()
    viewer.add_image(data, name='raw', opacity=.5)
    viewer.add_image(data, translate=translate, name=f'translated_{translate}', colormap='blue', opacity=.5)