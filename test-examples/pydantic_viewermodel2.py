import napari
import numpy as np


class MyViewer(napari.Viewer):
    my_additional_method: str = 'hello'


with napari.gui_qt():
    v = MyViewer()