import napari
from skimage import data
from skimage.transform import warp, AffineTransform
from skimage.color import rgb2gray
import numpy as np


fixed = rgb2gray(data.astronaut())
tform = AffineTransform(scale=(0.9, 0.9), rotation=0.2, translation=(20, -10))
moving = warp(fixed, tform.inverse, output_shape=fixed.shape)
moving = rgb2gray(moving)

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(fixed)
    viewer.add_points(face_color='blue', name='fixed pts', size=20, properties={'matches':[np.nan]})
    viewer.add_image(moving)
    viewer.add_points(face_color='red', name='moving pts', size=20, properties={'matches':[np.nan]})
    viewer.grid_view(n_column=2, n_row=2, stride=2)

    @viewer.bind_key('m')
    def match_points(viewer):        
        current_moving = viewer.layers['moving pts'].selected_data
        if len(current_moving) == 1:
            current_moving = list(current_moving)[0]
        else:
            current_moving = np.nan

        current_fixed = viewer.layers['fixed pts'].selected_data
        if len(current_fixed) == 1:
            current_fixed = list(current_fixed)[0]
        else:
            current_fixed = np.nan

        if not np.isnan(current_fixed):
            viewer.layers['fixed pts'].properties[current_fixed] = current_moving

        if not np.isnan(current_moving):
            viewer.layers['moving pts'].properties[current_moving] = current_fixed

        print(f'Match between moving {current_moving} and fixed {current_fixed}')


