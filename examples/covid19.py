"""
Displays covid19 data from omero
"""
# import s3fs
# import zarr
# 
# s3 = s3fs.S3FileSystem(anon=True, client_kwargs={'endpoint_url': 'https://s3.embassy.ebi.ac.uk/'})
# store = s3fs.S3Map(root='idr/zarr/v0.1/9822151.zarr', s3=s3, check=False)
# root = zarr.group(store=store)
# resolutions = [root['/' + str(i)] for i in list(range(11))]


import napari
import dask.array as da

path = 'https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/9822151.zarr'
resolutions = [da.from_zarr(path, component=str(i))[0, 0, 0] for i in list(range(11))]

for i, r in enumerate(resolutions):
    print('res ', i, len(resolutions))
    r.to_zarr('data/covid19/9822151/' + str(i) + '.zarr')

# with napari.gui_qt(startup_logo=True):
#     viewer = napari.Viewer()
#     viewer.add_image(resolutions)
