from segmentify import Viewer, gui_qt
from skimage.io import imread

path = '/Users/nicholassofroniew/Downloads/test_segmentify.png'

full_image = imread(path)
from scipy.ndimage import zoom
#img = zoom(full_image, 0.5).astype(float)
img = full_image.astype(float)

with gui_qt():
    viewer = Viewer(img)
