#@author: Mangaliso M. Mngomezulu
#labelling objects after segmentation

import imageio
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

image = imageio.imread('./datasets/sunnybrook-cardiac-mr/SCD2001_005')
  
#apply a gaussian filter on the image
filt = ndi.gaussian_filter(image, sigma=2)

#apply a mask on the noise removed image
mask = filt > 150

#put the labels on the mask
labels, nlabels = ndi.label(mask) #nlables shows how many segmented elements are in the image

#now display the labels, rainbow is for making the segments multi-colored
plt.imshow(labels, cmap='rainbow')
plt.title('SunnyBrok Cardiac .. Data')
plt.show()
       
#one can select individual labels from labels i.e
#np.where(labels -- 1, image, 0)

#choosing elements in some range of values
#np.where(labels < 4, image, 0) #choose the 1..3 objects

#a bounding box is the smalleest box that can fit the element
boxes = ndi.find_objects(labels) #boxes are slices with co-ords
