"""
Displays covid19 data from omero
"""

import napari
import dask.array as da

path = 'https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/9822151.zarr'
resolutions = [(da.from_zarr(path, component=str(i))[0, 0, 0]).astype('uint16') for i in list(range(11))]
viewer = napari.Viewer()
viewer.add_image(resolutions)
napari.run()
