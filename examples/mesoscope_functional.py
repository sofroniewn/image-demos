"""
Displays functional data from the mesoscope
"""

from skimage.io import imread
from napari import Viewer, gui_qt

mean = imread('data/mesoscope/functional/mean.tif')[65:-65, 65:-65]
localcorr = imread('data/mesoscope/functional/localcorr.tif')[65:-65, 65:-65]
rsq = imread('data/mesoscope/functional/rsqOverlayLC.tif')[65:-65, 65:-65]
tune = imread('data/mesoscope/functional/tuneCorPos.tif')[65:-65, 65:-65]
movie = imread('data/mesoscope/functional/movie.tif')[:, 65:-65, 65:-65]


with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the timeseries
    movie_layer = viewer.add_image(movie, name='timeseries', colormap='gray')

    # add the mean image
    mean_layer = viewer.add_image(mean, name='mean', colormap='gray', contrast_limits=(0.0, 1000.0))


    # add the local correlation image
    lc_layer = viewer.add_image(localcorr, name='localcorr', contrast_limits=(0.25, 0.75), colormap='gray')

    # add the rsq image
    rsq_layer = viewer.add_image(rsq, name='rsq')

    # add the tuning image
    tune_layer = viewer.add_image(tune, name='tune')
