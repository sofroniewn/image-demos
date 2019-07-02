"""
Displays calcium timeseries from neurofinder
"""

from skimage.io import imread
from skimage.measure import label
import numpy as np
from napari import Viewer
from napari.util import app_context
from vispy.color import Colormap

movie = imread('data/neurofinder/timeseries.tif')
mean = imread('data/neurofinder/mean.tif')
mask = imread('data/neurofinder/mask.tif')
localcorr = imread('data/neurofinder/localcorr.tif')
centers = np.loadtxt("data/neurofinder/centers.csv", delimiter=",")
polygons = np.load('data/neurofinder/polygons_edit.npy')

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the timeseries
    movie_layer = viewer.add_image(movie, name='timeseries')
    movie_layer.clim = (0.0, 600.0)
    movie_layer.colormap = 'gray'

    mean_layer = viewer.add_image(mean, name='mean')
    mean_layer.clim = (0.0, 600.0)
    mean_layer.colormap = 'gray'
    mean_layer.visible = False

    lc_layer = viewer.add_image(localcorr, name='localcorr')
    lc_layer.clim = (0.35, 1.0)
    lc_layer.colormap = 'gray'
    lc_layer.visible = False

    centers_layer = viewer.add_points(centers, name='centers')
    centers_layer.edge_width = 0
    centers_layer.face_color = 'green'
    centers_layer.opacity = 0.5
    centers_layer.visible = False

    shapes_layer = viewer.add_shapes(polygons, shape_type='polygon',
                                     edge_width=0, face_color='green',
                                     opacity=0.5, name='neurons')
    shapes_layer.visible = False

    labels = label(mask)
    labels_layer = viewer.add_labels(labels, name='rois')

# polygons_edit = shapes_layer.data.to_list()
# np.save('data/neurofinder/polygons_edit.npy', polygons_edit)
