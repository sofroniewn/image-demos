import nibabel as nib
import zarr


mri = nib.load('data/MRI/synthesized_FLASH25.nii.gz')
file_name = 'data/MRI/synthesized_FLASH25.zarr'
print(mri.shape)

z1 = zarr.open(file_name, mode='a', shape=mri.shape, chunks=(None, 1, 1), dtype='f4')

z1[:] = mri.get_fdata()
# for s in range(mri.shape[0]):
#     print('s', s, mri.shape[0])
#     ar = mri.slicer[s: s+1]
#     print('    ar', ar.shape)
#     z1[s] = ar[0]
