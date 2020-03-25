import dask.array as da
import napari


data = da.random.random((8000, 4000, 7000), chunks=(1, 4000, 7000))
print(data)

with napari.gui_qt():
    #viewer = napari.view_image(data, contrast_limits=[0, 1], is_pyramid=False)
    #viewer = napari.view_image(data, is_pyramid=False)
    viewer = napari.view_image(data)
