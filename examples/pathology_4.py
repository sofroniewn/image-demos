"""
Painting on an image pyramid of pathology slide
"""
import os
import tensorstore as ts
import numpy as np
import dask.array as da
import napari
import zarr

file_name = './data/camelyon16/tumor_001.zarr'
labels_file = './data/camelyon16/tumor_001_annotation.zarr'
pyramid = [da.from_zarr(file_name + '/' + str(i)) for i in range(10)]

if os.path.exists(labels_file):
    labels_temp = zarr.open(labels_file, mode='r')
    metadata = {
            'dtype': labels_temp.dtype.str,
            'order': labels_temp.order,
            'shape': labels_temp.shape,
            'chunks': labels_temp.chunks,
            }
else:
    metadata = {'dtype': '<u4',
                'shape': pyramid[0].shape[:-1],
                'order': 'C',
                'chunks':(64, 64),
                'compressor': {'id': 'blosc'}}


dir, name = os.path.split(labels_file)
labels_ts_spec = {
    'driver': 'zarr',
    'kvstore': {
    'driver': 'file',
    'path': dir,
    },
    'path': name,
    'metadata': metadata,
}

labels = ts.open(labels_ts_spec, open=True, create=True).result()

# create an empty viewer
viewer = napari.Viewer()

# add the pyramid
viewer.add_image(pyramid, name='slide')
viewer.add_labels(labels, name='annotations')
viewer.camera.zoom = 0.5
viewer.layers[1].display.show_grid = False
napari.run()