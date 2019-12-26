"""
Displays neuron morphology
"""

import napari
from neurom.io import swc
import numpy as np

def parse_swc(data):
    break_points = [0] + list(np.nonzero(np.diff(data[:, 6]) < 0)[0]+1) + [len(data)-1]
    paths = []
    for i in range(len(break_points)-1):
        if break_points[i+1] - break_points[i] > 2:
            paths.append(data[break_points[i]:break_points[i+1], :3])
    return paths

# def parse_swc_extra(data):
#     break_points = [0] + list(np.nonzero(np.diff(data[:, 6]) < 0)[0]+1) + [len(data)-1]
#     paths = []
#     for i in range(1, len(break_points)-1):
#         if break_points[i+1] - break_points[i] > 2:
#             paths.append(data[[break_points[i-1], break_points[i]], :3])
#     return paths

data = swc.read('data/neuromorphology/204-2-6nj.CNG.swc').data_block
paths = parse_swc(data)
# extra_paths = parse_swc_extra(data)

with napari.gui_qt():
    # create an empty viewer
    viewer = napari.view_shapes(paths, shape_type='path',
                                edge_color='blue', ndisplay=3)
    # viewer.add_shapes(extra_paths, shape_type='path',
    #                             edge_color='red')
