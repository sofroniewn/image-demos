"""
Displays functional data from the mesoscope
"""

from skimage.io import imread
from napari import ViewerApp
from napari.util import app_context

mean = imread('data/mesoscope/functional/mean.tif')
localcorr = imread('data/mesoscope/functional/localcorr.tif')
rsq = imread('data/mesoscope/functional/rsqOverlayLC.tif')
tune = imread('data/mesoscope/functional/tuneCorPos.tif')
movie = imread('data/mesoscope/functional/movie.tif')


with app_context():
    # create an empty viewer
    viewer = ViewerApp()

    # add the timeseries
    movie_layer = viewer.add_image(movie, name='timeseries')
    movie_layer.colormap = 'gray'

    # add the mean image
    mean_layer = viewer.add_image(mean, name='mean')
    mean_layer.clim = (0.0, 1000.0)
    mean_layer.colormap = 'gray'

    # add the local correlation image
    lc_layer = viewer.add_image(localcorr, name='localcorr')
    lc_layer.clim = (0.25, 0.75)
    lc_layer.colormap = 'gray'

    # add the rsq image
    rsq_layer = viewer.add_image(rsq, name='rsq')

    # add the tuning image
    tune_layer = viewer.add_image(tune, name='tune')
