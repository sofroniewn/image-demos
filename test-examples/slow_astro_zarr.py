import os
from typing import List

import dask.array as da
import napari


def get_pyramid(path: str) -> List[da.Array]:
    levels = ["base"] + sorted(
        [s for s in os.listdir(path) if (not s.startswith(".")) and (s != "base")]
    )
    return [da.from_zarr(f"{str(path)}/{level}").rechunk() for level in levels]


pyramid = get_pyramid("./data-njs/zarr-demo/image.zarr")

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(pyramid)  # [0])  # add this in to load only the base layer