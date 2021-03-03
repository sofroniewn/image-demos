import numpy as np
import napari

gl_max_texture_size = 16384 # insert hardware specific gl_max_texture_size
img = np.zeros((gl_max_texture_size*2, gl_max_texture_size*2), dtype=np.uint16) # create an empty image twice as large
img[img.shape[0]//2:, img.shape[1]//2:] = 1 # set the bottom right corner to 1

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(img, colormap='viridis')