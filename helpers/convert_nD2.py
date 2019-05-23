from skimage.io import imsave
from glob import glob
import bioformats
import javabridge
javabridge.start_vm(class_path=bioformats.JARS)

#from pims import ND2_Reader as ND2Reader
#from nd2reader import ND2Reader
#image = ND2Reader(file_name)[0]

files = glob('data/ndcn/kampmann/*.nd2')

for f in files:
    images = bioformats.load_image(f)

    imsave(f[:-3] + 'tif', images.astype('float32'), plugin='tifffile',
           photometric='minisblack')
