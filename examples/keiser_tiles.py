"""
Dynamically load irregularly shapes images of ants and bees
"""

import numpy as np
from dask_image.imread import imread
from dask.cache import Cache
from napari import Viewer
from napari.util import app_context
from pandas import read_csv
from glob import glob


cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()

base_dir = 'data/ndcn/keiser/'
slide_name = 'NA4009-02_AB'
file_name = base_dir + 'annotations-train.csv'
image_paths = glob(base_dir + 'tiles/' + slide_name + '/*.jpg')
#image_paths.sort()
image_names = [p[len(base_dir)+6:] for p in image_paths]

tiles = imread(base_dir + 'tiles/' + slide_name + '/*.jpg')
print(tiles.shape)

annotations = read_csv(file_name).set_index('imagename').loc[image_names]
annot_types = ['cored', 'diffuse', 'CAA', 'negative']
id = annotations[annot_types].values.argmax(axis=1)

border = 5
shapes = [[[i, -border, -border],
           [i, border + tiles.shape[1], border + tiles.shape[2]]]
          for i in range(len(tiles))]
base_cols = ['red', 'green', 'blue', 'white']

colors = [base_cols[i] for i in id]

with app_context():
    # create an empty viewer
    viewer = Viewer()

    # add the images
    layer = viewer.add_image(tiles, name=slide_name, clim_range=[0, 255])

    # add borders
    viewer.add_shapes(np.array(shapes), shape_type='rectangle',
                      face_color=[0, 0, 0, 0], edge_color=colors,
                      edge_width=border*2, opacity=0.75, name='annotation')

    viewer.layers.unselect_all()

    def cored(viewer):
        """Set the current annotation to cored
        """
        msg = 'cored'
        shapes = viewer.layers['annotation']
        shapes._data_view.update_edge_color(0, base_cols[annot_types.index(msg)])
        shapes.refresh()
        print(msg)

    def diffuse(viewer):
        """Set the current annotation to diffuse
        """
        msg = 'diffuse'
        shapes = viewer.layers['annotation']
        shapes._data_view.update_edge_color(0, base_cols[annot_types.index(msg)])
        shapes.refresh()
        print(msg)

    def CAA(viewer):
        """Set the current annotation to CAA
        """
        msg = 'CAA'
        shapes = viewer.layers['annotation']
        shapes._data_view.update_edge_color(0, base_cols[annot_types.index(msg)])
        shapes.refresh()
        print(msg)

    def negative(viewer):
        """Set the current annotation to negative
        """
        msg = 'negative'
        shapes = viewer.layers['annotation']
        shapes._data_view.update_edge_color(0, base_cols[annot_types.index(msg)])
        shapes.refresh()
        print(msg)

    # def forward(viewer):
    #     """Increments the current view by one
    #     """
    #     current = viewer.dims.indices[0]
    #     if current + 1 < viewer.dims.range[0][1]:
    #         viewer.dims.set_point(0, current + 1)
    #
    # def backward(viewer):
    #     """Decrements the current view by one
    #     """
    #     current = viewer.dims.indices[0]
    #     if current - 1 >= viewer.dims.range[0][0]:
    #         viewer.dims.set_point(0, current - 1)

    custom_key_bindings = {'c': cored, 'd': diffuse, 'a': CAA, 'n': negative}
    viewer.key_bindings = custom_key_bindings
