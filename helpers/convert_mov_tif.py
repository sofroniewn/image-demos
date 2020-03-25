import numpy as np
import napari
import imageio
from glob import glob
from skimage.io import imsave
from os.path import basename, splitext

folder = 'data-njs/anipose/hand-demo/2019-08-02/'

for path in sorted(glob(folder + 'videos-raw/*.MOV')):
    print(path)
    save_path = folder + 'videos-raw-tif/' + splitext(basename(path))[0] + '.tif'
    print(save_path)
    vid = imageio.get_reader(path,  'ffmpeg')
    movie = np.array([im for im in vid.iter_data()])
    imsave(save_path, movie)
