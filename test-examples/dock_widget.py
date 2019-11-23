import numpy as np
import napari
from skimage import data
from qtpy.QtWidgets import QLabel


blobs_raw = data.binary_blobs(length=64, n_dim=2, volume_fraction=0.1)

with napari.gui_qt():
    viewer = napari.view_image(blobs_raw)
    widg1 = QLabel('TEST WIDGET 1')
    widg2 = QLabel('TEST WIDGET 2')
    widg3 = QLabel('TEST WIDGET 3')
    viewer.window.add_dock_widget(widg1, area='bottom', name='test 1')
    viewer.window.add_dock_widget(widg2, area='left', name='ttt 2')
    viewer.window.add_dock_widget(widg3, area='right')
