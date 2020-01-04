from skimage import data
import napari
import time

t0 = time.time()
with napari.gui_qt(startup_logo=True):
    napari.view_image(data.astronaut(), rgb=True)
    t1 = time.time()
    print(f'splash took {t1 - t0} seconds')

t2 = time.time()
with napari.gui_qt(startup_logo=False):
    napari.view_image(data.astronaut(), rgb=True)
    t3 = time.time()
    print(f'no splash took {t3 - t2} seconds')
