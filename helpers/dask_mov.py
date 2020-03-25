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

# v = pims.Video(file)
# print(v)
# a = v.get_frame(10)
# print(a.shape)

def np_from_mov_pyav(path):
    container = av.open(path)
    return np.array([f.to_ndarray() for f in container.decode(video=0)])

def dask_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    shape = vid.get_meta_data()['size'][::-1] + (3,)
    lazy_imread = delayed(vid.get_data)
    return da.stack([da.from_delayed(lazy_imread(i), shape=shape, dtype=np.uint8) for i in range(vid.count_frames())])

def np_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    return np.array([im for im in vid.iter_data()], dtype=np.uint8)

mov4 = imread(file)
print('mov', mov4.shape)
f = np.asarray(mov4[0])
print('f', f.shape)

# t = time.time()
# mov1 = np_from_mov_pyav(folder + 'videos-raw/2019-08-02-vid01-camA.MOV')
# #mov2 = imread(folder + 'videos-raw/2019-08-02-vid01-camA.MOV')
# #mov3 = np_from_mov(folder + 'videos-raw/2019-08-02-vid01-camA.MOV')
# print(time.time() - t)
