"""
Displays an 100GB zarr file of lattice light sheet data
"""

import numpy as np
from napari import Viewer
from napari.util import app_context
from timeit import timeit
from pandas import DataFrame
import zarr

#cache = Cache(2e9)  # Leverage two gigabytes of memory

base_name = '/Users/nicholassofroniew/Documents/DATA-imaging/zarr_benchmarks/'

image_sizes = [2**x for x in range(8, 13)]
chunk_sizes = [2**x for x in range(4)]
locations = ['local', 'in-memory']
clim_range = [0, 1.0]
opp_caching = ['off', 'on']

df = DataFrame()

def update(ind):
    if ind is None:
        pass
    else:
        viewer.dims.indices[2] = ind
    layer.refresh()

with app_context():

    for N in image_sizes:
        for loc in locations:
            if loc == 'in-memory':
                chunk_sizes_used = [chunk_sizes[0]]
                opp_caching_used = [opp_caching[0]]
            else:
                chunk_sizes_used = chunk_sizes
                opp_caching_used = opp_caching
            for c in chunk_sizes_used:

                file_name = base_name + 'image_' + str(N) + '_chunk_' + str(c) + '.zarr'

                store = zarr.DirectoryStore(file_name)

                for opc in opp_caching_used:

                    if opc == 'off':
                        data = zarr.open(store, mode='r')
                    else:
                        cache = zarr.LRUStoreCache(store, max_size=2e9)
                        data = zarr.open(cache, mode='r')

                    if loc == 'local':
                        print('local zarr')
                        pass
                    elif loc == 'in-memory':
                        print('convert to in memory')
                        data = np.asarray(data)
                    else:
                        raise ValueError('Unrecognized location')


                    print(data.shape)

                    d = {'N': N, 'c': c, 'shape': data.shape, 'location': loc, 'opp_caching': opc}

                    # create an empty viewer
                    viewer = Viewer()
                    layer = viewer.add_image(data, multichannel=False, name='zarr benchmarks',
                                             clim_range=clim_range)

                    # Start profiling - do one refresh without measuring to blank
                    update_cmd = 'update(ind)'
                    glbls = {'update': update, 'ind': None}
                    result = timeit(update_cmd, number=1, globals=glbls)


                    glbls = {'update': update, 'ind': 0}
                    result = timeit(update_cmd, number=1, globals=glbls)
                    print(glbls['ind'], result)
                    d['refresh_time'] = result

                    glbls = {'update': update, 'ind': 1}
                    result = timeit(update_cmd, number=1, globals=glbls)
                    print(glbls['ind'], result)
                    d['move_in_time'] = result

                    glbls = {'update': update, 'ind': 8}
                    result = timeit(update_cmd, number=1, globals=glbls)
                    print(glbls['ind'], result)
                    d['move_new_time'] = result

                    glbls = {'update': update, 'ind': 1}
                    result = timeit(update_cmd, number=1, globals=glbls)
                    print(glbls['ind'], result)
                    d['move_back_time'] = result

                    df = df.append(d, ignore_index=True)

    df.to_csv('data/benchmarks/zarr_3D_zarr_2.csv')
