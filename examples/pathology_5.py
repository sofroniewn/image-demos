"""
Analysis on an image pyramid of pathology slide
"""

import dask.array as da
import napari
# Import magicgui and qt functionality

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

# create an empty viewer
viewer = napari.Viewer()

# add the pyramid
viewer.add_image([p[:, :, 0] for p in pyramid], name='red', colormap='red', blending='additive')
viewer.add_image([p[:, :, 1] for p in pyramid], name='green', colormap='green', blending='additive')
viewer.add_image([p[:, :, 2] for p in pyramid], name='blue', colormap='blue', blending='additive')
napari.run()