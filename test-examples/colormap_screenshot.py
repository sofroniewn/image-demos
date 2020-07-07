import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=2)

    data = np.ones((20, 20, 20))
    layer = viewer.add_image(data, contrast_limits =[0, 1])

    screenshot = viewer.screenshot()

    center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int)) 
    print(center, screenshot.shape, screenshot[center], np.repeat(255, 4))
    np.testing.assert_almost_equal(screenshot[center], np.repeat(255, 4))
