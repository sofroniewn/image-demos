"""
Display a labels layer above of an image layer using the add_labels and
add_image APIs
"""
import numpy as np
from skimage import data
from scipy import ndimage as ndi
import napari


with napari.gui_qt():
    blobs = data.binary_blobs(length=128, volume_fraction=0.1, n_dim=2)
    labeled = ndi.label(blobs)[0]
    viewer = napari.view_labels(labeled, name='blob IDs')
    selection_layer = viewer.add_shapes([[[0, 0], [128, 128]]],
        shape_type='rectangle',
        face_color=[1, 1, 1, 0], edge_color=[0, 0.6, 1, 1],
        edge_width=1, name='selection box')

    @viewer.mouse_drag_callbacks.append
    def get_unique_labels(viewer, event):
        yield

        # on move
        while event.type == 'mouse_move':
            labels_layer = viewer.layers[0]
            shapes_layer = viewer.layers[1]
            coords = np.round(shapes_layer.data[0]).astype(int)
            top_left = np.min(coords, axis=0)
            bottom_right = np.max(coords, axis=0)
            top_left = np.max([top_left, [0, 0]], axis=0)
            bottom_right = np.min([bottom_right, labels_layer.data.shape], axis=0)
            cutout = labels_layer.data[top_left[0]:bottom_right[0], top_left[1]:bottom_right[1]]
            print(np.unique(cutout))
            yield
