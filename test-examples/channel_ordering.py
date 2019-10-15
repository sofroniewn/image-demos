import numpy as np
import napari


randoms = np.random.randint(0, 20, 1024*1024*5)
channels_first = randoms.reshape((5, 1024, 1024))
channels_last = randoms.reshape((1024, 1024, 5))

# example code for trying out napari functionality
with napari.gui_qt():
    viewer = napari.view_image(channels_last, rgb=False, name='channels_last', order=[2, 0, 1])
