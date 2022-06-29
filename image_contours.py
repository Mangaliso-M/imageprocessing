#@Author: Mangaliso M. Mngomezulu
#description: finding image contours (closed shape of edges)
#the input must be a binary image (thresholding) the background remains black, while the objects of intrest should be white


from skimage import data, color, filters
from skimage.filters import threshold_otsu
from skimage import measure
from custom_lib import plot_comparison, show_image
import numpy as np

image = data.coffee()

#preprocessing the image

#make it grayscale
image = color.rgb2gray(image)


#binarize the image (using a threshold)
thresh = threshold_otsu(image)
thresholded_image = image > thresh

#find the contours, a list of lists that each define a closed boundary using a set of co-ordinates
contors = measure.find_contours(thresholded_image, 0.8) #0.8 is a constant value, the closer it is to 1, the more effective 

#show_image_contour(image, contour)
#print(contors)

#practical example, count the number of dots from the dots image
image = data.coins() #already in grayscale

#find the optimal threshold
thresh = filters.threshold_otsu(image)

#compute the binary image
binary = image > thresh

#find the contors in the image
contours = measure.find_contours(binary, 0.8)

#shape contours
shape_contours = [contour.shape[0] for contour in contours]

#set the max size of the shape to be detected, this was set through trial and error with the aid of the image visualization
#this bound works well
min_coin_size = 45

#set the min and max bounds for each shape
coins_contours = [contour for contour in contours if np.shape(contour)[0] > min_coin_size and np.shape(contour)[0]< 200]

print("{} coins found in the image", format(len(coins_contours)))
