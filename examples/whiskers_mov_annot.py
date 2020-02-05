"""
Displays an MRI volume
"""

import imageio
from napari import Viewer, gui_qt
import numpy as np

# vid = imageio.get_reader('data-njs/whiskers/IMG_6783.mov',  'ffmpeg')
# mov = np.array([im for im in vid.iter_data()])
# mov = mov[35:]
# mov = mov.mean(axis=-1)
# print(mov.shape)
mov = np.random.random((10, 400, 400))

with gui_qt():
    # create an empty viewer
    viewer = Viewer()

    # add the mov
    layer = viewer.add_image(mov, name='whiskers')

    points = np.array([[100, 100], [200, 200], [333, 111]])

    # create properties for each point
    properties = {
        'class': np.array([1, 2, 3]),
    }

    # define the color cycle for the face_color annotation
    face_color_cycle = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']

    # create a points layer where the face_color is set by the good_point property
    # and the edge_color is set via a color map (grayscale) on the confidence property.
    points_layer = viewer.add_points(
        points,
        properties=properties,
        size=10,
        edge_width=1,
        edge_color='white',
        face_color='class',
        face_color_cycle=face_color_cycle,
        name='points'
    )

    # bind a function to toggle the good_point annotation of the selected points
    current_class = 1
    points_layer.help = str(current_class)

    @viewer.bind_key('1')
    def toggle_1(viewer):
        current_class = 1
        points_layer.help = str(current_class)

    @viewer.bind_key('2')
    def toggle_1(viewer):
        current_class = 2
        points_layer.help = str(current_class)
        
    @viewer.bind_key('3')
    def toggle_1(viewer):
        current_class = 3
        points_layer.help = str(current_class)
        
    @viewer.bind_key('4')
    def toggle_1(viewer):
        current_class = 4
        points_layer.help = str(current_class)

    @viewer.bind_key('5')
    def toggle_1(viewer):
        current_class = 5
        points_layer.help = str(current_class)
        
    @viewer.bind_key('6')
    def toggle_1(viewer):
        current_class = 6
        points_layer.help = str(current_class)
