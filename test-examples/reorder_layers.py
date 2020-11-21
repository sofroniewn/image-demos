import numpy as np
import napari
import collections
from qtpy.QtCore import QPoint
import gc

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(np.random.random((10, 10)))
    viewer.add_image(np.random.random((10, 10)))
    gc.collect()

    # Check layout and layers list match after rearranging layers
    viewer.layers[:] = [viewer.layers[i] for i in (1, 0)]
    # Do another reorder and check layout and layers list match
    # after swapping layers again
    viewer.layers[:] = [viewer.layers[i] for i in (1, 0)]

    viewer.layers[:] = [viewer.layers[i] for i in (1, 0)]
    viewer.layers[1].selected=True
    viewer.layers[0].selected=True
    # viewer.layers[1].selected=False
    # viewer.layers[0].selected=False
    Event = collections.namedtuple('Event', field_names=['pos'])
    event = Event(pos=lambda : QPoint(10, 10))
    viewer.window._qt_viewer.layers.mousePressEvent(event)
    viewer.window._qt_viewer.layers.mouseReleaseEvent(event)
    #viewer.window._qt_viewer.update()

    viewer.window.show()
    viewer.layers[0].visible=False

    viewer.layers[1].visible=False
    gc.collect(generation=1)