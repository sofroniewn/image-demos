import tifffile
import napari

with tifffile.Timer('Loading pyramid:'):
    with tifffile.TiffFile('data/pathology/18-2470_2471_Scan1.qptiff') as tif:
        pyramid = list(reversed(sorted(tif.series, key=lambda p:p.size)))
        size = pyramid[0].size
        pyramid = [p for p in pyramid if size % p.size == 0]
        pyramid = [p.asarray() for p in pyramid]

print('pyramid levels:', [p.shape for p in pyramid])

with napari.gui_qt():
    napari.view_image(pyramid, multiscale=True)
