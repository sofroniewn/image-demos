import numpy as np
import zarr

base_name = '/Users/nicholassofroniew/Documents/DATA-imaging/zarr_benchmarks/'

image_sizes = [2**x for x in range(8, 14)]
chunk_sizes = [2**x for x in range(4)]

for N in image_sizes:
    shape = (16, N, N)
    data = np.random.rand(*shape)
    for c in chunk_sizes:
        print(N, c)
        file_name = base_name + 'image_' + str(N) + '_chunk_' + str(c) + '.zarr'
        z1 = zarr.open(file_name, mode='w', shape=shape, chunks=(c, None, None), dtype='f4')
        z1[:] = data
