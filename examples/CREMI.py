"""
View 2D slices of electron microscopy data
"""

import numpy as np
import h5py
from napari import Viewer, gui_qt
# from timeit import timeit
# from cProfile import Profile
# pr = Profile()

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

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    raw_layer = viewer.add_image(raw, name='raw', colormap='gray')

    neuron_labels_layer = viewer.add_labels(neuron_labels, opacity=0.4,
                                            name='neurons', num_colors=300)

    cleft_labels_layer = viewer.add_labels(cleft_labels, opacity=0.4,
                                           name='clefts', num_colors=10)

    pre_layer = viewer.add_points(pres, face_color='cyan',
                                   edge_color='cyan', size=[10, 10, 4],
                                   n_dimensional=True, name='presynaptic')

    post_layer = viewer.add_points(posts, face_color='magenta',
                                    edge_color='magenta', size=[10, 10, 4],
                                    n_dimensional=True, name='postsynaptic')

    @viewer.bind_key('s')
    def swap(viewer):
        """Swaps dims
        """
        dims = np.array(viewer.dims.order[-2:])
        dims = (dims + 1) % 3
        print('swapping', dims)
        viewer.dims.swap(dims[0], dims[1])

    # For profiling code
    # update_cmd = 'layer.refresh()'

    # glbls = {'layer': neuron_labels_layer}
    # result = pr.runctx(update_cmd, glbls, None)
    # stats = result.print_stats(sort='time')
    # print(stats)
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': neuron_labels_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': neuron_labels_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': neuron_labels_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)

    # glbls = {'layer': raw_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': raw_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': raw_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
    # glbls = {'layer': raw_layer}
    # result = timeit(update_cmd, number=1, globals=glbls)
    # print(result)
