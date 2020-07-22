"""
Display one shapes layer ontop of one image layer using the add_shapes and
add_image APIs. When the window is closed it will print the coordinates of
your shapes.
"""

import napari
import numpy as np
import imageio
from dask import delayed
import dask.array as da
from pandas import read_csv
#from dask.cache import Cache
from dask_image.imread import imread as da_imread
# cache = Cache(2e9)  # Leverage two gigabytes of memory
# cache.register()


# import pdb; pdb.set_trace()


def dask_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    shape = vid.get_meta_data()['size'][::-1] + (3,)
    lazy_imread = delayed(vid.get_data)
    return da.stack([da.from_delayed(lazy_imread(i), shape=shape, dtype=np.uint8) for i in range(vid.count_frames())])


def np_from_mov(path):
    vid = imageio.get_reader(path,  'ffmpeg')
    return np.array([im for im in vid.iter_data()], dtype=np.uint8)


def points_from_csv(path):
    points = read_csv(path, header=[0, 1, 2], index_col=0)
    n_points = len(points.columns) // 3
    img_coords = [points.values[:, [3*i+1, 3*i]] for i in range(n_points)]
    img_coords = [np.concatenate([np.expand_dims(points.index.values, axis=1), c], axis=1) for c in img_coords]
    vals = np.concatenate(img_coords, axis=0)
    bodyparts = np.array([[points.columns[3 * i][1]] * len(points.index) for i in range(n_points)]).flatten()
    properties = {'bodyparts' : bodyparts}
    print([bodyparts[::len(points.index)]])
    return vals, properties

def lines_from_points(points):
    n_pts = 20 # 20 points per hand
    n_frames = len(points) // 20 # number of frames
    lines = []
    coords = [[0, 1], [0, 4], [0, 8], [0, 12], [0, 16],
        [1, 2], [2, 3],
        [4, 5], [5, 6], [6, 7],
        [8, 9], [9, 10], [10, 11],
        [12, 13], [13, 14], [14, 15],
        [16, 17], [17, 18], [18, 19]]
    for j in coords:
         lines.append(np.stack([points[np.arange(n_frames) + j[0] * n_frames], points[np.arange(n_frames) + j[1] * n_frames]], axis=1))
    lines = np.concatenate(lines, axis=0)
    lines[:, 1, :] = lines[:, 1, :] - lines[:, 0, :]
    return lines


folder = 'data-njs/anipose/hand-demo/2019-08-02/'

video_names = ['camA', 'camB', 'camC']
movies = []
points = []
lines = []
for n in video_names:
    # for in memory loading use numpy reader
    #movies.append(np_from_mov(folder + 'videos-raw/2019-08-02-vid01-' + n + '.MOV'))
    # for lazy loading use dask reader
    movies.append(da_imread(folder + 'videos-raw/2019-08-02-vid01-' + n + '.MOV'))
    p = points_from_csv(folder + 'pose-2d/2019-08-02-vid01-' + n + '.csv')
    points.append(p)
    lines.append(lines_from_points(p[0]))


#multipliers = np.array([1 + i for i in range(4)] + list(range(5)) + list(range(5)) + [4] + list(range(5)))
#base_colors = np.array([[0, 1, 0]] * 4 + [[1, 0, 1]] * 5 + [[0, 1, 1]] * 5 + [[1, 1, 1]] + [[1, 1, 0]] * 5)
base_colors = [[0, 1, 0], [1, 0, 1], [0, 1, 1], [1, 0, 0], [0, 0, 1]]
digit_colors = base_colors[1:] + base_colors + base_colors + [[1, 1, 1]] + base_colors
multipliers = np.array([3] * 4 + [1] * 5 + [2] * 5 + [1] + [4] * 5)
colors = np.expand_dims((5 - multipliers) / 4, axis=1) * digit_colors
#print([m.shape for m in movies])

with napari.gui_qt():
    viewer = napari.Viewer(title='2019-08-02-vid01')
    for n, m, p, l in zip(video_names, movies, points, lines):
        print('   adding ' + n)
        viewer.add_image(m, name=n)
        viewer.add_vectors(l, name=n+'-lines', edge_color='red', edge_width=5)
        #print(p[1])
        #viewer.add_points(p[0], name=n+'-spots', properties=p[1], face_color='bodyparts', face_color_cycle=colors)
        
    viewer.grid_view()
    viewer.grid_view(n_column=2, n_row=2, stride=2)
