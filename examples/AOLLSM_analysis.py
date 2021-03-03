"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
import napari
import dask.array as da
from skimage import filters
from cellpose import models

file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
data = da.from_zarr(file_name)[:, :, ::4, ::4]

model = models.Cellpose(gpu=False, model_type='cyto', net_avg=False)

# # fit and predict
# if base_image.ndim > 2 and base_image.shape[2] in [3, 4]:
#     # for rgb data
#     chan = [2, 3]
# else:
#     chan = [0, 0]

# # print("processing")  

# # # normalize image based on clims
# # clims = (base_image.min(), base_image.max())
# # data = (data - clims[0]) / (clims[1] - clims[0])

# # print("about to segments", data.shape, data.dtype)  

def segment(block):
    masks, flows, styles, diams = model.eval(block[0, 0], diameter=None, channels=[0, 0], net_avg=False)
    return np.expand_dims(np.expand_dims(masks, 0), 0)


with napari.gui_qt():
    viewer = napari.Viewer(axis_labels='tzyx')
    viewer.add_image(data, name='AOLLSM_m4_560nm', multiscale=False, scale=[1, 3, 1, 1],
                contrast_limits=[0, 150_000], colormap='magma')
    viewer.add_image(data.map_blocks(filters.sobel), name='sobel', scale=[1, 3, 1, 1],
                contrast_limits=[0, 10_000], visible=False)
    viewer.add_labels(data.map_blocks(segment, dtype=np.int), name='segment', scale=[1, 3, 1, 1], visible=False)