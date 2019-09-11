"""
Displays calcium timeseries from neurofinder
"""

from skimage.io import imread
from skimage.measure import label
import numpy as np
from napari import Viewer, gui_qt

movie = imread('data/neurofinder/timeseries.tif')
mean = imread('data/neurofinder/mean.tif')
mask = imread('data/neurofinder/mask.tif')
localcorr = imread('data/neurofinder/localcorr.tif')
centers = np.loadtxt("data/neurofinder/centers.csv", delimiter=",")
polygons = np.load('data/neurofinder/polygons_edit.npy')

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the timeseries
    movie_layer = viewer.add_image(movie, name='timeseries', contrast_limits=(0.0, 600.0), colormap='gray')

    mean_layer = viewer.add_image(mean, name='mean', contrast_limits=(0.0, 600.0), colormap='gray', visible=False)

    lc_layer = viewer.add_image(localcorr, name='localcorr', contrast_limits=(0.35, 1.0), colormap='gray', visible=False)

    centers_layer = viewer.add_points(centers, name='centers', edge_width=0, face_color='green', visible=False, opacity=0.5)

    shapes_layer = viewer.add_shapes(polygons, shape_type='polygon',
                                     edge_width=0, face_color='green',
                                     opacity=0.5, name='neurons', visible=False)

    labels = label(mask)
    labels_layer = viewer.add_labels(labels, name='rois')

# polygons_edit = shapes_layer.data
# np.save('data/neurofinder/polygons_edit.npy', polygons_edit)
