import numpy as np
import zarr
from openslide import OpenSlide

slide = OpenSlide('data/camelyon16/tumor_001.tif')
file_name = 'data/camelyon16/tumor_001.zarr'

root = zarr.open_group(file_name, mode='a')


for i in range(0, 3):
    print(i, 10)
    shape = (slide.level_dimensions[i][0], slide.level_dimensions[i][1], 4)
    z1 = root.create_dataset(str(i), shape=shape, chunks=(300, 300, None),
                             dtype='uint8')

    # image = np.asarray(slide.read_region((0, 0), i,
    #                    slide.level_dimensions[i])).transpose(1, 0, 2)
    # z1[:] = image

    for j in range(slide.level_dimensions[i][0]//1528):
        print(j, slide.level_dimensions[i][0]/1528)
        image = np.asarray(slide.read_region((j*1528*(2**i), 0), i,
                           (1528, slide.level_dimensions[i][1]))).transpose(1, 0, 2)
        z1[j*1528:(j+1)*1528] = image
