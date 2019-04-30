"""
Image pyramid of pathology slide
"""

import numpy as np
import dask.array as da
from dask.cache import Cache
import xml.etree.ElementTree as ET
from napari import ViewerApp
from napari.util import app_context

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

file_name = 'data/camelyon16/tumor_001.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

tree = ET.parse('data/camelyon16/lesion_annotations/tumor_001.xml')
root = tree.getroot()

shape_1 = np.array([[float(c.attrib['X']), float(c.attrib['Y'])] for c in root[0][0][0]])
shape_2 = np.array([[float(c.attrib['X']), float(c.attrib['Y'])] for c in root[0][1][0]])
tumors = [shape_1, shape_2]

print([p.shape[:2] for p in pyramid])

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the pyramid
    layer = viewer.add_pyramid(pyramid, name='slide')
    viewer.camera.rect = (-4000, 0, pyramid[0].shape[1]+8000,
                          pyramid[0].shape[0])

    tumor_layer = viewer.add_shapes(tumors, shape_type='polygon', edge_width=50,
                                    edge_color='blue', face_color=[0, 0, 1, 0.5],
                                    opacity=0.5, name='tumors')
