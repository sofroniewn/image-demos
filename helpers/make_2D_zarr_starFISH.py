import numpy as np
import zarr
from skimage.io import imread



raw = imread('data-njs/smFISH/raw.tif')
z = zarr.open('data-njs/smFISH/raw.zarr', mode='a', shape=raw.shape, chunks=(1, None, None), dtype='f4')
z[:] = raw
