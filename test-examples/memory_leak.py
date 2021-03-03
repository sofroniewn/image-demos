import napari
import numpy as np
import psutil
import os

with napari.gui_qt():
    v = napari.Viewer()

    def get_process_memory():
        return psutil.Process(os.getpid()).memory_info().rss / 1e6

    for i in range(100):
        v.add_image(np.random.rand(1024, 1024))
        v.layers.pop(0)
        print(f"Mem used after {i:3} layers: {get_process_memory():0.2f} (MB)")