"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data, measure
import napari
import scipy.ndimage as ndi


image = data.binary_blobs(128, n_dim=3)
verts, faces, normals, values = (
    measure.marching_cubes_lewiner(image.astype(float), level=0.7)
)
labels = ndi.label(image)[0]
vertex_labels = ndi.map_coordinates(labels, verts.T, order=0).astype(int)


with napari.gui_qt():

    viewer = napari.view_surface((verts, faces, values))
    surf_layer = viewer.add_surface((verts, faces, vertex_labels),
                                    colormap='gist_earth')
    viewer.dims.ndisplay = 3
