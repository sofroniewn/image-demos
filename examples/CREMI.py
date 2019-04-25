"""
View 2D slices of electron microscopy data
"""

import numpy as np
import h5py
from napari import ViewerApp
from napari.util import app_context

filename = 'data/CREMI/sample_A_20160501.hdf'
data = h5py.File(filename,'r')
raw = np.asarray(data['volumes/raw'])
neuron_labels = np.asarray(data['volumes/labels/neuron_ids'])
cleft_labels = np.asarray(data['volumes/labels/clefts'])
coords = np.asarray(data['annotations/locations'])
types = np.asarray(data['annotations/types'])
resolution = data['volumes/raw'].attrs['resolution']
coords = (coords / resolution).astype(np.int)
pres = coords[types == 'presynaptic_site']
posts = coords[types == 'postsynaptic_site']

with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    raw_layer = viewer.add_image(raw.transpose(1, 2, 0), name='raw')
    raw_layer.colormap = 'gray'

    neuron_labels_layer = viewer.add_labels(neuron_labels.transpose(1, 2, 0),
                                            opacity=0.4, name='neurons')

    cleft_labels_layer = viewer.add_labels(cleft_labels.transpose(1, 2, 0),
                                           opacity=0.4, name='clefts')

    pre_layer = viewer.add_markers(pres[:, [2, 1, 0]], face_color='cyan',
                                   edge_color='cyan', size=[10, 10, 4],
                                   n_dimensional=True, name='presynaptic')

    post_layer = viewer.add_markers(posts[:, [2, 1, 0]], face_color='magenta',
                                    edge_color='magenta', size=[10, 10, 4],
                                    n_dimensional=True, name='postsynaptic')
