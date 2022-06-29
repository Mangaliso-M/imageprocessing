#@Author: Mangaliso M. Mngomezulu
#description: image segmentation(partition images into regions that are more simpler to analyzed) and image regions

#simple linear iterative clustering (unsupervised machine learning segmentation algorithm, uses k means clustering)
from matplotlib import pyplot as plt
from skimage.segmentation import slic
from skimage.color import label2rgb
from skimage import data
from custom_lib import plot_comparison

#load the image 
image = data.coffee()

#compute the segments
segments = slic(image)

#put segments on top of the original image
segmented_image = label2rgb(segments, image, kind='avg')

#display the original image and the segmented image
plot_comparison(image, segmented_image, "Segmented image")

#more segments can be applied on the image
specified_segments = slic(image, n_segments=400) #by default 100 segments are computed

#put the segments over the image
result = label2rgb(specified_segments,image, kind='avg')

plot_comparison(image, result, "400 segments")