import napari
import numpy as np
import dask.array as da
import numpy as np
import imageio
from dask import delayed
import dask.array as da
#from dask.cache import Cache
from dask_image.imread import imread
import time
import pims
import av

# cache = Cache(2e9)  # Leverage two gigabytes of memory
# cache.register()


folder = 'data-njs/anipose/hand-demo/2019-08-02/'
file = folder + 'videos-raw/2019-08-02-vid01-camA.MOV'
file = 'data-njs/whiskers/IMG_7988.mov'

movie = imread(file)
print(movie.shape)


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(movie)  # Attribute Error
