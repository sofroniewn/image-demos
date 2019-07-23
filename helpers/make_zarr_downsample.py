import numpy as np
import zarr
import dask.array as da

file_name = 'data/ndcn/keiser/slides/NA4009-02_AB.zarr'
image = da.from_zarr(file_name + '/1')
root = zarr.open_group(file_name, mode='a')

for i in range(2, 8):
    print('start', i, image.shape)
    image = da.coarsen(np.mean, image, {0: 2, 1:2, 2:1},
                       trim_excess=True)
    print('coarsen', i, image.shape)
    z1 = root.create_dataset(str(i), shape=image.shape, chunks=(300, 300, None),
                             dtype='uint8')
    z1[:] = image

    # for j in range(slide.level_dimensions[i][0]//1743):
    #     print(j, slide.level_dimensions[i][0]/1743)
    #     image = np.asarray(slide.read_region((j*1743*(2**ds[i]), 0), i,
    #                        (1743, slide.level_dimensions[i][1]))).transpose(1, 0, 2)
    #     z1[j*1743:(j+1)*1743] = image
