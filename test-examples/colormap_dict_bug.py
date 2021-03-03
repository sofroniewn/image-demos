import numpy as np
import napari
from skimage import data
from skimage.color import rgb2gray

with napari.gui_qt():
    # add the image
    viewer = napari.view_image(rgb2gray(data.astronaut()))

    points = np.array([[0, 0], [100, 0], [0, 100]])

    # property to colors that I want to achieve:
    color_map_expected = {1: 'green', 2: 'red', 3: 'blue'}

    # how to currently do it in napari
    properties = {'my_colors': [2, 6, 3]}
    viewer.add_points(points, face_color='my_colors', properties=properties, face_color_cycle=color_map_expected)