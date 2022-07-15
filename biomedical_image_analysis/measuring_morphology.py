#@author: Mangaliso M. Mngomezulu
#descrip: Measuring morphology: shape and size

import imageio
import scipy.ndimage as ndi

#this volume contains 3 chest scan images
vol = imageio.volread('./datasets/tcia-chest-ct-sample/sample_volume')

#calculate the volume per voxel, first get the dimensions from the metadata of the dicom images
d0,d1,d2 = vol.meta['sampling']

dvoxel = d0 * d1 * d2 

print(dvoxel) #the dimensions are in cubic milimeters

#count label voxels
#nvoxels = ndi.sum(1, label, index=1)

#volume = nvoxels * dvoxel


#distance of each voxel to the nearest background value
#create a left ventricle mask
#mask = np.where(labels == 1, 1, 0)
#distance = ndi.distance_transform_edt(mask) #eucledian distance, an array, where non zero voxels have been replaced by the distance to the closest background voxel
#distance.max() is the maximum of the distances 

#center of mass(intensity values, larger values pull the center towards them)
#com=ndi.center_of_mass(vol, labels, index=1)
#print(com) #shows a tuple of the co-ordinates that are each a center of each dimensions
