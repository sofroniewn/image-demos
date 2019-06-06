"""
Displays the allen brain reference atlas at 10 um resolution
"""

from napari import Viewer
from napari.util import app_context
import dask.array as da
from dask.cache import Cache
import numpy as np


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base = da.random.randint(0, 255, (100, 2000, 5000), dtype='uint8')
pyramid = [base]
image = pyramid[0]
for i in range(4):
    image = da.coarsen(np.mean, image, {0: 1, 1:2, 2:2},
                       trim_excess=True)
    pyramid.append(image)
print('pyramid level shapes: ', [p.shape for p in pyramid])

with app_context():
    # create an empty viewer
    viewer = Viewer()
    # layer = viewer.add_image(base, name='base')
    layer = viewer.add_pyramid(pyramid, name='pyramid')

    base_shape = pyramid[0].shape[-2:]
    viewer.camera.rect = (-0.1 * base_shape[1], -0.1 * base_shape[0],
                          1.2 * base_shape[1], 1.2 * base_shape[0])
