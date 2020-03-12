"""
Display one shapes layer ontop of one image layer using the add_shapes and
add_image APIs. When the window is closed it will print the coordinates of
your shapes.
"""

import numpy as np
import napari
from pandas import read_csv


def points_from_csv(path):
    points = read_csv(path, header=[0], index_col=-1)

    n_points = len(points.columns) // 6
    img_coords = [points.values[:, [6*i+2, 6*i+1, 6*i]] for i in range(n_points)]
    img_coords = [np.concatenate([np.expand_dims(points.index.values, axis=1), c], axis=1) for c in img_coords]
    vals = np.concatenate(img_coords, axis=0)
    bodyparts = np.array([[points.columns[6 * i][:-2]] * len(points.index) for i in range(n_points)]).flatten()
    properties = {'bodyparts' : bodyparts}
    print([bodyparts[::len(points.index)]])
    return vals, properties

def lines_from_points(points):
    n_pts = 20 # 20 points per hand
    n_frames = len(points) // 20 # number of frames
    lines = []
    coords = [[14, 4], [14, 5], [14, 6], [14, 7], [14, 8],
        [4, 9], [9, 15],
        [5, 10], [10, 0], [0, 16],
        [6, 11], [11, 1], [1, 17],
        [7, 12], [12, 2], [2, 18],
        [8, 13], [13, 3], [3, 19]]
    for j in coords:
         lines.append(np.stack([points[np.arange(n_frames) + j[0] * n_frames], points[np.arange(n_frames) + j[1] * n_frames]], axis=1))
    lines = np.concatenate(lines, axis=0)
    lines[:, 1, :] = lines[:, 1, :] - lines[:, 0, :]
    return lines


folder = 'data-njs/anipose/hand-demo/2019-08-02/'

points = points_from_csv(folder + 'pose-3d/2019-08-02-vid01.csv')
lines = lines_from_points(points[0])


base_colors = [[0, 1, 0], [1, 0, 1], [0, 1, 1], [1, 0, 0], [0, 0, 1]]
digit_colors = base_colors[1:] + base_colors + base_colors + [[1, 1, 1]] + base_colors
multipliers = np.array([3] * 4 + [1] * 5 + [2] * 5 + [1] + [4] * 5)
colors = np.expand_dims((5 - multipliers) / 4, axis=1) * digit_colors

with napari.gui_qt():
    viewer = napari.Viewer(title='2019-08-02-vid01', ndisplay=3)
    viewer.add_vectors(lines, name='lines', edge_color='white', edge_width=4)
    viewer.add_points(points[0], name='spots', properties=points[1], face_color='bodyparts', face_color_cycle=colors)
        
