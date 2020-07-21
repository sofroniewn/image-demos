"""
Display one 3-D volume layer using the add_volume API
"""

import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    data = np.zeros((100, 10, 10))
    data[-1] = 1
    viewer.add_image(data, contrast_limits=[0, 1])
    viewer.layers[0].rendering = 'attenuated_mip'
    viewer.layers[0].attenuation = 2.0
    screenshot = viewer.screenshot(canvas_only=True)
    center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # Check that rendering has not been attenuated
    assert screenshot[center + (0,)] > 200

    viewer.layers[0].attenuation = 0.02
    screenshot = viewer.screenshot(canvas_only=True)
    center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # Check that rendering has been attenuated
    assert screenshot[center + (0,)] < 60

    # viewer.layers[0].rendering = 'mip'

    # # Check the max intensity projection value
    # screenshot = viewer.screenshot(canvas_only=True)
    # center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # # Note right now this value is approximately half of the expected value
    # # given contrast limits and max data value. It looks like some attenuation
    # # is happening even in mip mode.
    # assert screenshot[center + (0,)] < 150 and screenshot[center + (0,)] > 120



    #screenshot = viewer.screenshot(canvas_only=True)
    #center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # Check that rendering has been attenuated
    #assert screenshot[center + (0,)] < 60

    #viewer.layers[0].attenuation = 2.0
   # screenshot = viewer.screenshot(canvas_only=True)
    #center = tuple(np.round(np.divide(screenshot.shape[:2], 2)).astype(int))
    # Check that rendering has not been attenuated
    #assert screenshot[center + (0,)] > 200