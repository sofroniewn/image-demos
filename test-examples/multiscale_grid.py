import numpy as np
import napari

with napari.gui_qt():
    pyramid0 = [np.random.random((4096 // 2**i, 4096 // 2**i)) for i in range(5)]
    pyramid1 = [np.random.random((4096 // 2**i, 4096 // 2**i)) for i in range(5)]
    for x in pyramid1:
        x[-100:, -100:] = 0
    v = napari.Viewer()
    v.add_image(pyramid0, colormap='green')
    v.add_image(pyramid1, colormap='magenta', blending='additive')
