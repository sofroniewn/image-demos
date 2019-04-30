import numpy as np
import dask.array as da
import zarr



file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
#data = da.from_zarr(file_name)
orig_shape = (768, 1024, 201, 199) # data.shape
print(orig_shape)

file_name_2 = 'data/LLSM/AOLLSM_m4_560nm-2.zarr'

### For many files
shape = tuple([orig_shape[i] for i in [2, 3, 0, 1]])
print(shape)
z0 = zarr.open(file_name, mode='a', shape=orig_shape, chunks=(None, None, 1, 1), dtype='f4')
z2 = zarr.open(file_name_2, mode='a', shape=shape, chunks=(1, 1, None, None), dtype='f4')

for i in range(61, 201): #shape[0]
    print(i)
    z2[i, :, :, :] = np.asarray(z0[:, :, i, :]).transpose(2, 0, 1)
    z0[:, :, i, :] = 0
