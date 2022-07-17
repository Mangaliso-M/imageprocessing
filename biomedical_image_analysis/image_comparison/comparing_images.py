#comparing images
import imageio
import matplotlib.pyplot as plt
import numpy as np
from skimage import color

"""
Cost functions: produce metrics to be minimized.
Objective functions: produce metrics to be maximized.
"""

"""
 Below the mean squared error is calculated
 
"""
#load the 2 images
im1 = imageio.imread('././datasets/OASISsample/healthybrainscan.jpg')
im2 = imageio.imread('././datasets/OASISsample/brainscan.jpg')
im1 = color.rgb2gray(im1)
im2 = color.rgb2gray(im2)

error = im1 - im2

#plt.imshow(error)
#plt.title('The error')
#plt.show()

#get the absolute values
abs_error = np.abs(error)

mean_abs_error = np.mean(abs_error)

#scalar quantity
print("The mean absolute error is:", mean_abs_error)

"""
 using the intersection of the union: the result is a numerical value [0,1]
 the intersection is divided by the union of the two images

"""

#compute two masks for the images, the 0 used in this example could have been anything.
mask1 = im1 > 0
mask2 = im2 > 0

intersection = mask1 & mask2

union = mask1 | mask2

intersection_of_union = intersection.sum() / union.sum()

plt.imshow(intersection)
plt.title("Intersecion of the two images")
plt.show()

plt.imshow(union)
plt.title("Union of the two images")
plt.show()


print("Intersection of union",intersection_of_union)
