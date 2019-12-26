import numpy as np
import zarr
from scipy.ndimage import zoom

file_name_base = 'data-njs/lymph_nodes/TCZYX_test_data.zarr'
file_name = 'data-njs/lymph_nodes/TCZYX_pyr.zarr'

lymph = zarr.open(file_name_base, mode='r')
root = zarr.open_group(file_name, mode='a')
print('init')

for i in range(0, 6):
    print(i, 6, lymph.shape)
    z1 = root.create_dataset(str(i), shape=lymph.shape, chunks=(1, 1, 64, 64, 64),
                             dtype=np.uint8)
    z1[:] = lymph
    print('getting size')
    new_lymph = np.zeros((lymph.shape[0], lymph.shape[1]) + zoom(np.asarray(lymph[0, 0]), 0.5).shape)
    for k in range(lymph.shape[0]):
        for j in range(lymph.shape[1]):
            print('downsampling', k, j)
            new_lymph[k, j] = zoom(np.asarray(lymph[k, j]), 0.5)
    lymph = new_lymph
