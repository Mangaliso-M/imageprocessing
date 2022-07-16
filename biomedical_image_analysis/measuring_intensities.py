#@author: Mangaliso M. Mngomezulu
#description: Measuring intensities in images

""""
scipy.ndimage.measurements functions, summarize the data from the image from all dimensions

ndi.mean()
ndi.median()
ndi.sum()
ndi.maximum()
ndi.standard_deviation()
ndi.variance()

ndi.labeled_comprehension() - used to summarize the data, a custom function
"""

import imageio
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

#load the image
image = imageio.imread('./datasets/sunnybrook-cardiac-mr/SCD2001_005')


#apply a gaussian filter on the image
filt = ndi.gaussian_filter(image, sigma=2)

#apply a mask on the noise removed image
mask = filt > 150

#put the labels on the mask
labels, nlabels = ndi.label(mask) #nlables shows how many segmented elements are in the image

#put the labels on the mask
labels, nlabels = ndi.label(image) #nlables shows how many segmented elements are in the image

#the mean of all the image pixels, from the masked image
print("Mean of pixels: ",ndi.mean(mask))

#since the labels and nlables are for a segmented version of the image, specifyging the labels when computing the mean will ommit 0 values
print("Mean of segments:", ndi.mean(mask, labels))

#get a mean intensity for a certain label (segments)
print("Mean of first label:", ndi.mean(mask, labels, index=1))

#get the mean for certain labels, specify them ina list
print("Mean of 1...3 labels:", ndi.mean(mask,labels, index=[1,2,3]))

#get the histogram distributions for each of the selected labels
#ndi.hist.histogram(mask, min=0, max=255, bins=256) #this is how its normally done
objects_histograms = ndi.histogram(mask, min=0, max=255, bins=256, labels=labels, index=[1,2])
plt.hist(objects_histograms)
plt.show()