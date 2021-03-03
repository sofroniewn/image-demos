from magicgui import magicgui
import numpy as np
import napari
from qtpy.QtWidgets import QWidget



@magicgui(call_button="execute")
def threshold(image: napari.layers.Image) -> napari.layers.Labels:
    """Threshold an image."""
    return image.data > 0.5


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((10, 10)))
    # instantiate the widget
    gui = threshold.Gui()
    viewer.window.add_dock_widget(gui) 

    threshold(viewer.layers[0])
    threshold(viewer.layers[0])
