import dask.array as da
import napari

# column, row, slice
array = da.random.randint(0, 255, (20, 30, 50_000), chunks=(20, 30, 1), dtype='uint16')

# slice, column, row
array2 = da.random.randint(0, 255, (50_0, 200, 300), chunks=(1, 200, 300), dtype='uint16')

# with napari.gui_qt():
#     viewer = napari.Viewer()
#     viewer.add_image(array2, is_pyramid=False)

with napari.gui_qt():
    viewer = napari.Viewer(order=[2, 0, 1])
    viewer.add_image(array, is_pyramid=False, contrast_limits=[0, 255])

# # Correct dask arrays to slice, row, column
# array = da.transpose(array)
# array2 = da.moveaxis(array2, 2, 1)
