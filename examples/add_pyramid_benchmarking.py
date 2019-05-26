"""
Displays an image pyramid
"""

from skimage import data
from skimage.color import rgb2gray
from skimage.transform import pyramid_gaussian
import napari
from napari.util import app_context
import numpy as np
import dask.array as da
from dask.cache import Cache
import zarr
from timeit import timeit


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

image = data.astronaut()
rows, cols, dim = image.shape

# create pyramid from astronaut image
astronaut = data.astronaut().mean(axis=2) / 255
base = np.tile(astronaut, (16, 16))
pyramid = list(pyramid_gaussian(base, downscale=2, max_layer=5,
                                multichannel=False))
pyramid = [(255*p).astype('uint8') for p in pyramid]
print('orig', [p.shape[:2] for p in pyramid])

# Convert pyramid to zarr
file_name = 'data/astro_pyramid.zarr'
# root = zarr.open_group(file_name, mode='a')
# for i in range(0, len(pyramid)):
#     print(i, len(pyramid))
#     shape = pyramid[i].shape
#     z1 = root.create_dataset(str(i), shape=shape, chunks=(300, 300),
#                              dtype='uint8')
#     z1[:] = pyramid[i]

pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(len(pyramid))]
print('zarr', [p.shape[:2] for p in pyramid])

def update(scale):
    camera.rect = (-.1*pyramid[0].shape[1]*scale, 0, 1.2*pyramid[0].shape[1]*scale,
                   pyramid[0].shape[0]*scale)

update_cmd = 'update(scale)'

with app_context():
    # create the viewer
    viewer = napari.Viewer()

    # add image pyramid
    viewer.add_pyramid(pyramid)

    camera = viewer.window.qt_viewer.view.camera
    camera.rect = (-.1*pyramid[0].shape[1], 0, 1.2*pyramid[0].shape[1],
                   pyramid[0].shape[0])

    glbls = {'update': update, 'scale': 1}
    result = timeit(update_cmd, number=1, globals=glbls)

    glbls = {'update': update, 'scale': 1}
    result = timeit(update_cmd, number=1, globals=glbls)
    print(glbls['scale'], result)

    glbls = {'update': update, 'scale': 1/2}
    result = timeit(update_cmd, number=1, globals=glbls)
    print(glbls['scale'], result)

    glbls = {'update': update, 'scale': 1/4}
    result = timeit(update_cmd, number=1, globals=glbls)
    print(glbls['scale'], result)

    glbls = {'update': update, 'scale': 1/8}
    result = timeit(update_cmd, number=1, globals=glbls)
    print(glbls['scale'], result)
