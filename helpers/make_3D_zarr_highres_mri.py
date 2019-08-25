import numpy as np
import zarr
from scipy.ndimage import zoom

file_name_base = 'data/MRI/synthesized_FLASH25.zarr'
file_name = 'data/MRI/synthesized_FLASH25_pyr.zarr'

mri = zarr.open(file_name_base, mode='r')
root = zarr.open_group(file_name, mode='a')
print('init')
mri = np.asarray(mri)
print('in memory')
mri = zoom(mri, 0.5)

for i in range(1, 6):
    print(i, 6, mri.shape)
    z1 = root.create_dataset(str(i), shape=mri.shape, chunks=(100, 100, 100),
                             dtype='f4')
    z1[:] = mri
    mri = zoom(mri, 0.5)
