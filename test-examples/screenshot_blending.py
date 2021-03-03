"""
Test adding 4D followed by 5D image layers to the viewer

Intially only 2 sliders should be present, then a third slider should be
created.
"""

import numpy as np
from skimage import data
import napari


with napari.gui_qt():

    data = np.ones((10, 10))

    viewer = napari.Viewer()
    viewer.add_image(data, colormap='red')
    viewer.add_image(data, colormap='blue')
    screenshot = viewer.screenshot(canvas_only=True)
    center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # Check that blue is visible
    np.testing.assert_almost_equal(screenshot[center], [0, 0, 255, 255])

    # # Switch to 3D rendering
    # viewer.dims.ndisplay = 3
    # screenshot = viewer.screenshot(canvas_only=True)
    # center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # # Check that blue is still visible
    # np.testing.assert_almost_equal(screenshot[center], [0, 0, 255, 255])

    # # Switch back to 2D rendering
    # viewer.dims.ndisplay = 2
    # screenshot = viewer.screenshot(canvas_only=True)
    # center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # # Check that blue is still visible
    # np.testing.assert_almost_equal(screenshot[center], [0, 0, 255, 255])