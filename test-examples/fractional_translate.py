import numpy as np
import napari


im = np.ones((3,3,3))
im[1,1,1] = 0


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(im, colormap='blue', rgb=False)
    viewer.add_image(im, translate=[0.1, 0, 0], blending='additive', colormap='red', rgb=False)