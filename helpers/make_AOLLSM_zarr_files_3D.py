import numpy as np
import dask.array as da
import zarr
from scipy.ndimage import zoom



file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
#data = da.from_zarr(file_name)
#print(data.shape)
orig_shape = (201, 199, 768, 1024)
print(orig_shape)

file_name_2 = 'data/LLSM/AOLLSM_m4_560nm-3D.zarr'

### For many files
shape = (199, 50, 192, 256)
print(shape)
z0 = zarr.open(file_name, mode='a', shape=orig_shape, chunks=(1, 1, None, None), dtype='f4')
z3D = zarr.open(file_name_2, mode='a', shape=shape, chunks=(1, None, None, None), dtype='f4')

for i in range(0, 199):
    print(i)
    z3D[i, :, :, :] = zoom(np.asarray(z0[:, i, :, :]), 0.25)
    #z0[:, :, i, :] = 0
