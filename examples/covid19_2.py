"""
Displays covid19 data from omero
"""

import napari
import dask.array as da

path = 'https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/9822151.zarr'
image = (da.from_zarr(path, component=str(0))[0, 0, 0]).astype('uint16')
viewer = napari.Viewer()
viewer.add_image(image)
viewer.camera.zoom = 0.5
viewer.camera.center=(0.0, 85014.87696148254, 33918.66295457239)
napari.run()

