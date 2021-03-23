"""
Dynamically load and process data
"""

import fsspec
import zarr
import dask.array as da
import napari

url = "https://gist.githubusercontent.com/manzt/436fc2966c484205a2c60824f659b412/raw/cdc69f2ce645d953185f10d7552501bfd459dd12/Vanderbilt-Spraggins-Kidney-MxIF.ome.tif.json"
store = fsspec.get_mapper("reference://", references=url, target_protocol="http")
grp = zarr.open(store)
pyramid = [
    da.from_zarr(store, component=d["path"])
    for d in grp.attrs["multiscales"][0]["datasets"]
]
viewer = napari.Viewer()
viewer.add_image(pyramid, channel_axis=0)
napari.run()