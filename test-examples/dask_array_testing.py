import dask.array as da
import napari


data = da.random.random((10367, 2501, 2501), chunks=(1, 2501, 2501))
print(data)

with napari.gui_qt():
    viewer = napari.view_image(data, contrast_limits=[0, 1], is_pyramid=False)
