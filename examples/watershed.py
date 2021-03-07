"""
Perform interactive semantic segmentation
"""

"""
Display a labels layer above of an image layer using the add_labels and
add_image APIs
"""

from napari import Viewer, gui_qt
import numpy as np
from scipy import ndimage as ndi
from skimage import data
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from dask_image.imread import imread
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square, remove_small_objects


base_name = 'data/kaggle-nuclei/fixes/stage1_train/*'

images = imread(base_name + '/images/image_gray.tif')
labels = imread(base_name + '/labels/label.tif')

image = np.asarray(images[0])
gt = np.asarray(labels[0])

# apply threshold
thresh = threshold_otsu(image)
blobs = closing(image > thresh, square(4))
blobs = remove_small_objects(blobs, 20)

# # Generate an initial image with blobs
# blobs = data.binary_blobs(length=256, blob_size_fraction=0.1, n_dim=2,
#                           volume_fraction=.2, seed=999)


# Now we want to separate the two objects in image
# Generate the markers as local maxima of the distance to the background
distance = ndi.distance_transform_edt(blobs)

local_maxi = peak_local_max(distance, indices=True, footprint=np.ones((5, 5)),
                            labels=blobs)

local_maxi_image = np.zeros(blobs.shape, dtype='bool')
for cord in local_maxi:
    local_maxi_image[tuple(cord)] = True
markers = ndi.label(local_maxi_image)[0]

labels = watershed(-distance, markers, mask=blobs)


with gui_qt():

    # create an empty viewer
    viewer = Viewer()

    @viewer.bind_key('r')
    def rerun(viewer):
        blobs = viewer.layers['input'].data
        distance = viewer.layers['distance'].data
        local_maxi = viewer.layers['markers'].data
        print('Number of markers: ', len(local_maxi))
        local_maxi_image = np.zeros(blobs.shape, dtype='bool')
        for cord in local_maxi:
            local_maxi_image[tuple(np.round(cord).astype(int))] = True
        markers = ndi.label(local_maxi_image)[0]
        labels = watershed(-distance, markers, mask=blobs)
        viewer.layers['output'].data = labels

    # add the raw image
    viewer.add_image(image, name='raw')

    # add the input image
    viewer.add_image(blobs.astype('float'), name='input', visible=False)

    # add the distance image
    viewer.add_image(distance, name='distance', colormap='gray', visible=False)

    # add the resulting labels image
    viewer.add_labels(labels, name='output')

    # # add the ground truth as a labels image
    # viewer.add_labels(gt, name='gt')

    # add the markers
    viewer.add_points(local_maxi, face_color='blue', size=3, name='markers')
