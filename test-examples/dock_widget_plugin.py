import numpy as np
import napari


with napari.gui_qt():
    v = napari.Viewer()
    v.window.add_plugin_dock_widgets('io-test')