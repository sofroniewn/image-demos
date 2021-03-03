"""
Displays an 100GB zarr file of lattice light sheet data
"""

from paintedlife import GameOfLife
import numpy as np
import napari


shape = (50, 50)
gol = GameOfLife(shape)
show_corners=False
backlit=True

if show_corners:
    gol._grid[gol.corner_squares()] = True
    gol._update()
with napari.gui_qt():
    gol.viewer = napari.Viewer()
    if backlit:
        square = [[0, 0], 
                    [0, gol.shape[1]], 
                    [gol.shape[0], gol.shape[1]],
                    [gol.shape[0], 0]]
        gol.viewer.add_shapes(square, name='backlight', opacity=0.05)
    gol._add_GOL_to_viewer()
    gol.viewer.bind_key('u', gol._update)
    gol._evolve_gui()

    
    input_pattern = np.zeros(shape)
    high_values = [[6, 2], [7, 2], [6, 3], [7, 3], [6, 12], [7, 12], [8, 12], [5, 13], [9, 13],
                   [4, 14], [10, 14], [4, 15], [10, 15], [7, 16], [5, 17], [9, 17], [6, 18], [7, 18], [8, 18],
                   [7, 19], [4, 22], [5, 22], [6, 22], [4, 23], [5, 23], [6, 23], [3, 24], [7, 24],
                   [2, 26], [3, 26], [7, 26], [8, 26], [4, 36], [5, 36], [4, 37], [5, 37]]
    for v in high_values:
        input_pattern[tuple(v)] = 1

    gol.viewer.layers[1].data[0] = input_pattern
