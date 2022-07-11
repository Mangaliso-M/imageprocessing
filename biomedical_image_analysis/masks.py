#@author: Mangaliso M. Mngomezulu
#descrip: image masks -  a binary array that serves as a screen to remove undesirable pixels

import imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

mask1 = mat > 5 #tests each value in the matrix if it is greater than 5 or not
#print(mask1)

mask2 = mat < 5
#print(mask2)

mask3 = mask1 & ~mask2 #in mask1 and not in mask2
#print(mask3)

#applying masks with conditions using numpy
#np.where(condition, x, y) returns x when true and y when false given the condition args can be arrays

im = imageio.imread('./datasets/rsna_hand_radiograph.png')

#im_specific_features = np.where(im > 64, im, 0) #return whats there or 0
im_specific_features = np.where(im > 64, 1, 0) #returns 1 or 0


plt.imshow(im, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()


plt.imshow(im_specific_features, cmap='gray')
plt.title('Image focused on specific features')
plt.axis('off')
plt.show()

#dialtion is done using the binary_dilation function from the ndi library
im_specific_features = ndi.binary_dilation(im_specific_features, iterations=3)
plt.imshow(im_specific_features, cmap='gray')
plt.title('Image focused on specific features, dilated')
plt.axis('off')
plt.show()

#ndi.(....) gives access to useful funtions like erosion and fill holes
