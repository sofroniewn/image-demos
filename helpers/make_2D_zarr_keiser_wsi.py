import numpy as np
import zarr
from openslide import OpenSlide

slide = OpenSlide('data/ndcn/keiser/slides/NA4009-02_AB.svs')
file_name = 'data/ndcn/keiser/slides/NA4009-02_AB.zarr'

print(slide.level_count)
print(slide.dimensions)
print(slide.level_dimensions)
print(slide.level_downsamples)


root = zarr.open_group(file_name, mode='a')
ds = [0, 2, 4]

for i in range(2, slide.level_count):
    print(i, slide.level_count)

    shape = (slide.level_dimensions[i][0], slide.level_dimensions[i][1], 4)
    z1 = root.create_dataset(str(i), shape=shape, chunks=(300, 300, None),
                             dtype='uint8')

    image = np.asarray(slide.read_region((0, 0), i,
                       slide.level_dimensions[i])).transpose(1, 0, 2)
    z1[:] = image

    # for j in range(slide.level_dimensions[i][0]//1743):
    #     print(j, slide.level_dimensions[i][0]/1743)
    #     image = np.asarray(slide.read_region((j*1743*(2**ds[i]), 0), i,
    #                        (1743, slide.level_dimensions[i][1]))).transpose(1, 0, 2)
    #     z1[j*1743:(j+1)*1743] = image
