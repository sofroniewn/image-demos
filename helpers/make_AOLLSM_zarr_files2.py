import numpy as np
import dask.array as da
import zarr
import pandas as pd

# file_order_name = 'data/LLSM/AOLLSM_order.csv'
# file_order = pd.read_csv(file_order_name, index_col=0)
# order = np.argsort([name[0] for name in file_order.values])

file_name = 'data/LLSM/AOLLSM_m4_560nm.zarr'
#data = da.from_zarr(file_name)
#file_name_2 = 'data/LLSM/AOLLSM_m4_560nm-2.zarr'

### For many files
# shape = (199, 20, 768, 1024)
# print(shape)

z0 = zarr.open(file_name, mode='a')
print(z0.shape)
z0[:, 10, :, :] = (z0[:, 11, :, :] + z0[:, 9, :, :]) / 2

#z2 = zarr.open(file_name_2, mode='a', shape=shape, chunks=(1, 1, None, None), dtype='f4')

# for i in range(0, 199):
#     j = order[i]
#     print(i, j)
#     z2[i, :, :, :] = np.asarray(z0[:, j, :, :])
#     z0[:, j, :, :] = 0
