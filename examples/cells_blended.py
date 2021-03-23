"""
Displays the cytoplasm, nucleus, and cell membrane of a field of cells in
three different color channels
"""

from skimage.io import imread
import numpy as np
import napari

cells = imread('data/cells/cells.tif')
cells[470:, 320:, :] = cells[470, 320, :]

# create an empty viewer
viewer = napari.Viewer()

# add and color the membrane
membrane = viewer.add_image(cells[:, :, 0], name='membrane', colormap='magenta', contrast_limits = [0.0, 255.0], blending='additive')

# add and color the cytoplasm
cytoplasm = viewer.add_image(cells[:, :, 1], name='cytoplasm', contrast_limits=[0.0, 255.0], colormap='yellow', blending='additive')

# add and color the nucleus
nucleus = viewer.add_image(cells[:, :, 2], name='nucleus', contrast_limits=[0.0, 255.0], colormap='cyan', blending='additive')

# Create empty rgba image
blended = np.zeros(viewer.layers[0].data.shape + (4,))
# Set alpha value to max
blended[..., 3] = 1
for layer in viewer.layers:
    # normalize data by clims
    normalized_data = (layer.data - layer.contrast_limits[0]) / (layer.contrast_limits[1] - layer.contrast_limits[0])
    colormapped_data = layer.colormap.map(normalized_data.flatten())
    colormapped_data = colormapped_data.reshape(normalized_data.shape + (4,))

    # perform an "additive" blending
    f_dest = normalized_data[..., None]
    f_source = 1 - f_dest
    blended = blended * f_source + colormapped_data

viewer.add_image(blended, name='blended', contrast_limits=[0.0, 1.0])

napari.run()