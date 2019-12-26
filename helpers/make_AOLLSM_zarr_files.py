import numpy as np
from glob import glob
from skimage.io import imread
import pandas as pd
import zarr


image_path = '/Volumes/GoogleDrive/My Drive/d/'
image_file = 'ex6-2_CamA_ch1_CAM1_stack*_560nm_*Abs_000x_000y_000z_0000t_decon.tif'
image_files = glob(image_path + image_file)
n_files = len(image_files)
print(image_files)
df = pd.DataFrame(image_files)
df.to_csv('./data/AOLLSM_order.csv')

# file_name = '/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm-6.zarr'
# ### For one file
# # shape = (768, 1024, 201)
# # z1 = zarr.open(file_name, mode='w', shape=shape, chunks=(None, None, 10), dtype='f4')
# # z1[:] = imread(image_files[0]).transpose(2, 1, 0)
#
# ### For many files
# shape = (768, 1024, 201, n_files)
# z1 = zarr.open(file_name, mode='a', shape=shape, chunks=(None, None, 1, 1), dtype='f4')
#
# for i, f in enumerate(image_files):
#     print(i, n_files)
#     z1[:, :, :, i] = imread(f).transpose(2, 1, 0)
