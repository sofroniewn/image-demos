import numpy as np
import dask.array as da
import zarr



file_name = '/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm-6.zarr'
data = da.from_zarr(file_name)
print(data.shape)

file_name_2 = '/Users/nicholassofroniew/Documents/DATA-imaging/ExM/AOLLSM_m4_560nm-7.zarr'

### For many files
shape = (768, 1024, 201, 199)
z1 = zarr.open(file_name_2, mode='a', shape=shape, chunks=(None, None, 1, 1), dtype='f4')

for i in range(100, 200):
    print(i)
    z1[:, :, :, i] = data[:, :, :, i]
