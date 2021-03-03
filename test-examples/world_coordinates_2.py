"""
Display one 3-D volume layer using the add_volume API
"""
import numpy as np
import napari


#affine = np.array([[1, 2, 5], [0, 2, 3], [0, 0, 1]])
affine = np.array([[1, -1, 4], [2, 3, 2], [0, 0, 1]])

corners = np.array([[0, 0], [4, 0], [0, 4], [4, 4]])
corners_h = np.concatenate([corners, np.ones((4, 1))], axis=1)

with napari.gui_qt():
    viewer = napari.Viewer()
    # viewer.add_image(np.random.random((21, 21)), name='background', colormap='red', opacity=.5, translate=(-10, -10))
    viewer.add_image(np.random.random((5, 5)), name='background', colormap='red', opacity=.5)
    viewer.add_points(corners_h[:, :-1], size=0.5, opacity=.5, face_color=[0.8, 0, 0, 0.8], name='bg corners')

    viewer.add_image(np.random.random((5, 5)), colormap='blue', opacity=.5, name='moving', affine=affine)
    viewer.add_points((corners_h @ affine.T)[:, :-1], size=0.5, opacity=.5, face_color=[0, 0, 0.8, 0.8], name='mv corners')
    viewer.reset_view()