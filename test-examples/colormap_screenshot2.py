import numpy as np
import napari


with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=2)

    data = np.ones((6, 15, 15))
    viewer.add_image(data, channel_axis=0, blending='translucent')
    
    # enter grid view
    viewer.grid_view()
    
    
    # check screenshot
    screenshot = viewer.screenshot(canvas_only=True)
    # sample 6 squares of the grid and check they have right colors
    pos = [
        (1 / 3, 1 / 3),
        (1 / 3, 1 / 2),
        (1 / 3, 2 / 3),
        (1 / 2, 1 / 3),
        (1 / 2, 1 / 2),
        (1 / 2, 2 / 3),
    ]
    # BGRMYC color order
    color = [
        [0, 0, 255, 255],
        [0, 255, 0, 255],
        [255, 0, 0, 255],
        [255, 0, 255, 255],
        [255, 255, 0, 255],
        [0, 255, 255, 255],
    ]
    for c, p in zip(color, pos):
        coord = tuple(
            np.round(np.multiply(screenshot.shape[:2], p)).astype(int)
        )
        np.testing.assert_almost_equal(screenshot[coord], c)