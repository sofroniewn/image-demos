"""
Crop image after mouse click and print max value
"""
import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.view_image(np.random.random((512, 512)))
    layer = viewer.layers[0]

    @layer.mouse_drag_callbacks.append
    def get_max_of_crop(layer, event):
        crop_size = 32
        cords = np.round(layer.coordinates).astype(int)
        min_vals = np.maximum([0]*len(cords), cords - crop_size // 2)
        max_vals = np.minimum(layer.data.shape, cords + crop_size // 2)
        crop = layer.data[tuple(slice(n, x) for n, x in zip(min_vals, max_vals))]
        print('Center coordinate:', cords,'Cropped shape:', crop.shape, ' Cropped max value:', np.max(crop))
