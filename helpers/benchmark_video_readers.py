import numpy as np
import napari
import imageio
from dask import delayed
import dask.array as da
from pandas import read_csv
from dask.cache import Cache

# cache = Cache(2e9)  # Leverage two gigabytes of memory
# cache.register()


# import pdb; pdb.set_trace()


def dask_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    shape = vid.get_meta_data()['size'][::-1] + (3,)
    lazy_imread = delayed(vid.get_data)
    return da.stack([da.from_delayed(lazy_imread(i), shape=shape, dtype=np.uint8) for i in range(vid.count_frames())])


def np_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    return np.array([im for im in vid.iter_data()], dtype=np.uint8)


folder = 'data-njs/anipose/hand-demo/2019-08-02/'
n = 'camA'


movie = np_from_mov(folder + 'videos-raw/2019-08-02-vid01-' + n + '.MOV')
